# Generated by Django 4.1.3 on 2022-12-07 03:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0018_activitylist_verb'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeightChange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(decimal_places=2, default=5, max_digits=5, validators=[django.core.validators.MinValueValidator(0)])),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weight_dog', to='database.dog')),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
        migrations.CreateModel(
            name='HeightChange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.DecimalField(blank=True, decimal_places=2, default=23, max_digits=5, validators=[django.core.validators.MinValueValidator(0)])),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='height_dog', to='database.dog')),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
    ]
