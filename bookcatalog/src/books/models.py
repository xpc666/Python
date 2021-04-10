from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=128)
    phone = models.CharField(max_length=16)
    id = models.CharField(max_length=16, primary_key=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    published_date = models.DateField()
    bookid = models.CharField(max_length=64,unique=True)
    publisher_id = models.ForeignKey(Publisher,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
