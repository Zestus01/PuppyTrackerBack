# Generated by Django 4.1.3 on 2022-12-02 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0015_alter_activity_activities_alter_activity_dog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'ordering': ['time']},
        ),
    ]
