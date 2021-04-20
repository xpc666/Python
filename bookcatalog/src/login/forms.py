from django import forms
from login.models import LibraryUser

class UserLoginForm(forms.ModelForm):
    # toBedeteleted = forms.BooleanField()
    class Meta:
        model = LibraryUser
        fields = ('user_id', 'password')

class UserRegisterForm(forms.ModelForm):
    # toBedeteleted = forms.BooleanField()
    class Meta:
        model = LibraryUser
        fields = '__all__'
