# Generated by Django 5.1.3 on 2024-12-01 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='contet',
            field=models.TextField(default='avval qilsam bolmasmidi'),
            preserve_default=False,
        ),
    ]
