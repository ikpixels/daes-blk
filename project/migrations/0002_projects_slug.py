# Generated by Django 2.2.6 on 2019-12-28 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
