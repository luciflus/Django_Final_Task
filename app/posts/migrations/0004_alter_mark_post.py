# Generated by Django 3.2 on 2023-01-21 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_mark_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.post'),
        ),
    ]
