import uuid  # Required for unique book instances
from datetime import date
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User  # Required to assign User as a borrower

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('died', null=True, blank=True)

    class Meta:
        ordering = ['first_name', 'last_name']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Publisher(models.Model):
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=128)
    phone = models.CharField(max_length=16)
    id = models.CharField(max_length=16, primary_key=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    pub_date = models.DateField()
    pub = models.ForeignKey(Publisher,on_delete=models.RESTRICT)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN', max_length=13,
                            unique=True,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn'
                                      '">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['title', 'author']

    def display_genre(self):
        """Creates a string for the Genre. This is required to display genre in Admin."""
        # print("genre: " + genre.name for genre in self.genre.all())
        # print("genre: " + genre.name for genre in self.genre.all()[:3])
        return ', '.join([genre.name for genre in self.genre.all()[:3]])

    display_genre.short_description = 'Genre'

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self):
        return self.title

class BookCopy(models.Model):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                              help_text="Unique ID for this particular book across whole library")
        book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
        imprint = models.CharField(max_length=200)
        due_back = models.DateField(null=True, blank=True)
        borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

        @property
        def is_overdue(self):
            if self.due_back and date.today() > self.due_back:
                return True
            return False

        LOAN_STATUS = (
            ('d', 'Maintenance'),
            ('o', 'On loan'),
            ('a', 'Available'),
            ('r', 'Reserved'),
        )

        status = models.CharField(
            max_length=1,
            choices=LOAN_STATUS,
            blank=True,
            default='d',
            help_text='Book availability')

        class Meta:
            ordering = ['due_back']
            permissions = (("can_mark_returned", "Set book as returned"),)

        def __str__(self):
            return f'{self.id} ({self.book.title})'
