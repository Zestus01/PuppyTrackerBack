# Generated by Django 4.1.3 on 2022-12-01 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0011_alter_activity_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activities',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='activity_activitylist', to='database.activitylist'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='description',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='activity',
            name='dog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dog_activity', to='database.dog'),
        ),
        migrations.AlterField(
            model_name='activitylist',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
