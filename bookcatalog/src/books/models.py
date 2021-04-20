from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=128)
    phone = models.CharField(max_length=16)
    id = models.CharField(max_length=16, primary_key=True)

    def __str__(self):
        return self.name

class Catalog(models.Model):
    catalog_id = models.CharField(max_length=8, primary_key=True)
    catalog_name = models.CharField(max_length=128)

    def get_absolute_url(self):
        return reverse('books:catalogpage')

    def __str__(self):
        return self.catalog_name

class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    published_date = models.DateField()
    bookid = models.CharField(max_length=64,unique=True)
    publisher_id = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    cat_id = models.ForeignKey(Catalog,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title
