from django.urls import path
from django.contrib.auth import views as auth_views
from .views import user_login, dashboard

urlpatterns = [
    # path('',user_login,name='login'),
    path('',auth_views.LoginView.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
]