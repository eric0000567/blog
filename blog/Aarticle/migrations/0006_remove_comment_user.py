# Generated by Django 2.0.1 on 2018-01-22 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aarticle', '0005_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
    ]
