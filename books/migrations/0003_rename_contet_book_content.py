# Generated by Django 5.1.3 on 2024-12-05 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_contet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='contet',
            new_name='content',
        ),
    ]
