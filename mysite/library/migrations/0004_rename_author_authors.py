# Generated by Django 4.1.1 on 2022-09-30 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_rename_first_name_author_f_name_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Author',
            new_name='Authors',
        ),
    ]
