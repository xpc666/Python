from django import forms
from books.models import Publisher, Book, Catalog

class NewPublisher(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'

class BookForm(forms.ModelForm):
    # toBedeteleted = forms.BooleanField()
    class Meta:
        model = Book
        fields = '__all__'

class CatalogForm(forms.ModelForm):
    class Meta:
        model = Catalog
        fields = '__all__'
