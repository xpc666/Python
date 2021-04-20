from django.db import models
from django.shortcuts import reverse

class LibraryUser(models.Model):
    user_id = models.CharField(max_length=32, primary_key=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    phone = models.CharField(max_length=16)
    email = models.CharField(max_length=16)
    password = models.CharField(max_length=128)

    def get_absolute_url(self):
        return reverse('login', args=[])

    def __str__(self):
        return self.user_id
