from django.urls import path
from login import views

app_name = 'login'

urlpatterns = [
    # path('userlogin', views.UserLoginView.as_view(), name='userlogin'),
    path('userregister', views.UserRegisterView.as_view(), name='userregister'),
]
