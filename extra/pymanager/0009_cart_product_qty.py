# Generated by Django 4.1.7 on 2023-03-20 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booksapp', '0008_remove_cart_product_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product_qty',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
