# Generated by Django 3.2 on 2023-01-21 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_name_author_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]