from django import forms
from books import models

class NewPublisher(forms.ModelForm):
    class Meta:
        model = models.Publisher
        fields = '__all__'

class BookForm(forms.ModelForm):
    # toBedeteleted = forms.BooleanField()
    class Meta:
        model = models.Book
        fields = '__all__'

class GenreForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = '__all__'
