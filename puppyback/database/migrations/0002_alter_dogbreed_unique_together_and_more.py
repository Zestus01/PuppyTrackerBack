# Generated by Django 4.1.3 on 2022-11-28 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='dogbreed',
            unique_together={('dog', 'breed')},
        ),
        migrations.AlterUniqueTogether(
            name='doguser',
            unique_together={('dog', 'user')},
        ),
    ]