from django.urls import path,include
from . import views
urlpatterns = [
    path('loginpage/',views.loginform,name='loginpage'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout_view,name='logoutpage'),
    path('dashboard/',views.dashboard,name='dashboard')
]