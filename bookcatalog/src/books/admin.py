from django.contrib import admin
from books import models

# Register your models here.
# admin.site.register(models.Publisher)
# admin.site.register(models.Book)
# admin.site.register(models.Author)
# admin.site.register(models.BookCopy)

class BookCopyInline(admin.TabularInline):
    model = models.BookCopy
    extra = 0

class BookInline(admin.TabularInline):
    model = models.Book
    fields = ('title', 'pub_date', 'language')
    extra = 0

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'language')
    inlines = [BookCopyInline]

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]

admin.site.register(models.Author, AuthorAdmin)

class PublisherAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Publisher, PublisherAdmin)

@admin.register(models.BookCopy)
class BookCopyAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'status', 'due_back')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )



admin.site.register(models.Genre)
admin.site.register(models.Language)
