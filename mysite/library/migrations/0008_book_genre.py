# Generated by Django 4.1.1 on 2022-09-30 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_bookinstance'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='Išrinkite žanrą(us) šiai knygai', to='library.genre'),
        ),
    ]
