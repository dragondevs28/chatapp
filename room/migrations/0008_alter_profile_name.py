# Generated by Django 4.1.5 on 2023-01-06 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0007_alter_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
