# Generated by Django 4.0 on 2023-03-16 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_subscribedusers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='subscribedusers',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]
