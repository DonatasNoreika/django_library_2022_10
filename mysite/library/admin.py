from django.contrib import admin
from .models import (Author,
                     BookInstance,
                     Book,
                     Genre)

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
    list_display = ("uuid", "book", "due_back")
    list_filter = ("status", "due_back")

    fieldsets = (
        ("General", {'fields': ('uuid', 'book')}),
        ("Availability", {'fields': ('status', 'due_back')})
    )


admin.site.register(Author)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Genre)
