# Generated by Django 4.1.1 on 2022-10-03 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_book_genre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Autorius', 'verbose_name_plural': 'Autoriai'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Knyga', 'verbose_name_plural': 'Knygos'},
        ),
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'verbose_name': 'Knygos egzempliorius', 'verbose_name_plural': 'Knygų egzemplioriai'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'Žanras', 'verbose_name_plural': 'Žanrai'},
        ),
    ]