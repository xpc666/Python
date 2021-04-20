from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView
from login import models
from login.forms import UserLoginForm, UserRegisterForm

# Create your views here.
def logout(request):
    # check if user has logged in. If not, direct to the login page.
    return render(request,'login.html')
    # return reverse(request, 'books/index.html')

class UserRegisterView(CreateView):
    template_name = 'login/register.html'
    form_class = UserRegisterForm

class UserLoginView(View):
    def get(self, request):
        loginForm = UserLoginForm()
        context = {'userloginform':loginForm}
        return render(request,'login.html', context)

    def post(self, request):
        print("to do something")
        loginForm = UserLoginForm(request.POST)
        return render(request, 'books/index.html')
