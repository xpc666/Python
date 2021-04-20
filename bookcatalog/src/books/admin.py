from django.contrib import admin
from books.models import Publisher, Book, Catalog

# Register your models here.
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Catalog)
