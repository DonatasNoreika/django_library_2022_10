from django.contrib import admin
from .models import (Author,
                     BookInstance,
                     Book,
                     Genre)

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'isbn', 'author', 'display_genre')

admin.site.register(Author)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance)
admin.site.register(Genre)
