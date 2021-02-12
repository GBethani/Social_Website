from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm
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
