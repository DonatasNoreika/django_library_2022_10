# Generated by Django 4.1.1 on 2022-10-11 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0016_alter_bookreview_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookreview',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.book'),
        ),
    ]