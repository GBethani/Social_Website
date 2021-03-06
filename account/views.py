from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm
# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user=user)
                    return HttpResponse("Login Successful!")
                else:
                    return HttpResponse("Disabled Account")
            else:
                return HttpResponse("Invalid Login!")
    else:
        form = LoginForm()
    context = {
        'form':form
    }
    return render(request,'account/login.html',context=context)

@login_required
def dashboard(request):
    return render(request,'account/dashboard.html',{'section':'dashboard'})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = form.save(commit=False)
            # Set the chosen password
            new_user.set_password(form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request,'account/register_done.html',{'new_user': new_user})
    else:
        form = UserRegistrationForm()
    return render(request,'account/register.html',{'form': form})

