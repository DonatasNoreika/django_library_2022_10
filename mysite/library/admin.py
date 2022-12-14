from django.contrib import admin
from .models import (Author,
                     BookInstance,
                     Book,
                     Genre,
                     BookReview,
                     Profile)

# Register your models here.

class BookInstanceInLine(admin.TabularInline):
    model = BookInstance
    extra = 0  # išjungia placeholder'ius
    can_delete = False
    readonly_fields = ("uuid",)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn', 'author', 'display_genre')
    inlines = [BookInstanceInLine]


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ("uuid", "book", "due_back", 'reader')
    list_filter = ("status", "due_back")
    search_fields = ('uuid', 'book__title', 'book__author__last_name')

    fieldsets = (
        ("General", {'fields': ('uuid', 'book')}),
        ("Availability", {'fields': ('status', 'due_back', 'reader')})
    )


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'display_books')

class BookReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'date_created', 'reviewer')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Genre)
admin.site.register(BookReview, BookReviewAdmin)
admin.site.register(Profile)