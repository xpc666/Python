from django import forms
from books.models import Publisher, Book

class NewPublisher(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'

class BookForm(forms.ModelForm):
    toBedeteleted = forms.BooleanField()

    class Meta:
        model = Book
        fields = '__all__'
