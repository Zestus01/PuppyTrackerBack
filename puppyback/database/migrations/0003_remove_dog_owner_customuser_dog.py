# Generated by Django 4.1.3 on 2022-11-28 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_alter_dogbreed_unique_together_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='owner',
        ),
        migrations.AddField(
            model_name='customuser',
            name='dog',
            field=models.ManyToManyField(related_name='dog_user', through='database.DogUser', to='database.dog'),
        ),
    ]
