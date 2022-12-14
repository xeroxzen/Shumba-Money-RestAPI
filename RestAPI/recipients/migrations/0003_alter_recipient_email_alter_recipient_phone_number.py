# Generated by Django 4.1.1 on 2022-09-27 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipients', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipient',
            name='email',
            field=models.EmailField(blank=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='recipient',
            name='phone_number',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
