# Generated by Django 2.1.2 on 2018-11-29 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutpage',
            name='ab_title',
        ),
    ]
