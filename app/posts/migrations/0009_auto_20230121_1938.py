# Generated by Django 3.2 on 2023-01-21 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_author_is_staff'),
        ('posts', '0008_mark_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.author'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mark',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marks', to='posts.post'),
        ),
    ]