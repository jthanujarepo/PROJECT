# Generated by Django 4.1.7 on 2023-03-21 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Booksapp', '0014_finalorder_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='finalorder',
            name='order',
        ),
    ]
