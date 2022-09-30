from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField("Pavadinimas", max_length=200, help_text="Įveskite knygos žanrą (pvz. detektyvas)")

class Author(models.Model):
    first_name = models.CharField("Vardas", max_length=100)
    last_name = models.CharField("Pavardė", max_length=100)

