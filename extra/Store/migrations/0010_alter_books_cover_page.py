# Generated by Django 4.1.5 on 2023-03-13 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0009_rename_vendor_product_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='cover_page',
            field=models.ImageField(blank=True, null=True, upload_to='stati/books/'),
        ),
    ]
