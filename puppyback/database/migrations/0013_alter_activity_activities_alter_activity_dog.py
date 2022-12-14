# Generated by Django 4.1.3 on 2022-12-01 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0012_alter_activity_activities_alter_activity_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activities',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='activitylist', to='database.activitylist'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='dog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dog', to='database.dog'),
        ),
    ]
