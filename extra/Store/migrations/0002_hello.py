# Generated by Django 4.1.5 on 2023-02-27 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='hello',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('pic', models.ImageField(upload_to='folder1/image')),
            ],
        ),
    ]
