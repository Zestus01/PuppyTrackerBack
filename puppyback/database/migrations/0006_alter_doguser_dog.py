# Generated by Django 4.1.3 on 2022-11-29 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_dog_breed_dog_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doguser',
            name='dog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.dog', unique=True),
        ),
    ]
