# Generated by Django 4.1.4 on 2022-12-11 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0020_alter_breed_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='heightchange',
            options={'ordering': ['time']},
        ),
        migrations.AlterModelOptions(
            name='weightchange',
            options={'ordering': ['time']},
        ),
    ]
