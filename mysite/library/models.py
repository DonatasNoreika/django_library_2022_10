from django.db import models
import uuid
from django.contrib.auth.models import User
from datetime import date
from tinymce.models import HTMLField
# Create your models here.

class Genre(models.Model):
    name = models.CharField("Pavadinimas", max_length=200, help_text="Įveskite knygos žanrą (pvz. detektyvas)")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Žanras'
        verbose_name_plural = 'Žanrai'


class Author(models.Model):
    first_name = models.CharField("Vardas", max_length=100)
    last_name = models.CharField("Pavardė", max_length=100)
    # description = models.TextField("Aprašymas", max_length=2000, default="")
    description = HTMLField("Aprašymas")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def display_books(self):
        books = self.books.all()
        book_names = list(book.title for book in books)
        books_str = ", ".join(book_names)
        return books_str

    display_books.short_description = "Knygos"

    class Meta:
        verbose_name = 'Autorius'
        verbose_name_plural = 'Autoriai'
        ordering = ['id']


class Book(models.Model):
    title = models.CharField("Pavadinimas", max_length=200)
    summary = models.TextField("Aprašymas", max_length=1000, help_text='Trumpas knygos aprašymas')
    isbn = models.CharField("ISBN", max_length=13, help_text='13 Simbolių <a href="https://www.isbn-international.org/content/what-isbn">ISBN kodas</a>')
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True, related_name="books")
    genre = models.ManyToManyField("Genre", help_text='Išrinkite žanrą(us) šiai knygai')
    cover = models.ImageField("Viršelis", upload_to='covers', null=True)

    def __str__(self):
        return f"{self.author} - {self.title}"

    def display_genre(self):
        genres = self.genre.all()
        genre_names = list(genre.name for genre in genres)
        genres_str = ", ".join(genre_names)
        return genres_str

    display_genre.short_description = "Žanras"

    class Meta:
        verbose_name = 'Knyga'
        verbose_name_plural = 'Knygos'
        ordering = ['-id']

class BookInstance(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, help_text='Unikalus UUID knygos kopijai')
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name='instances')
    due_back = models.DateField("Bus prieinama", blank=True)
    reader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    LOAN_STATUS = (('a', 'Administruojama'), ('p', 'Paimta'), ('g', 'Galima paimti'), ('r', 'Rezervuota'))

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='a', help_text="Statusas")

    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    def __str__(self):
        return f"{self.book} ({self.uuid}) - {self.status} ({self.due_back})"

    class Meta:
        verbose_name = 'Knygos egzempliorius'
        verbose_name_plural = 'Knygų egzemplioriai'
        ordering = ['-due_back']
