# Generated by Django 4.1.3 on 2022-11-30 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_alter_doguser_dog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breed',
            name='max_height_female',
            field=models.DecimalField(decimal_places=2, default=25, max_digits=5),
        ),
        migrations.AlterField(
            model_name='breed',
            name='max_height_male',
            field=models.DecimalField(decimal_places=2, default=25, max_digits=5),
        ),
        migrations.AlterField(
            model_name='breed',
            name='max_weight_female',
            field=models.DecimalField(decimal_places=2, default=55, max_digits=5),
        ),
        migrations.AlterField(
            model_name='breed',
            name='max_weight_male',
            field=models.DecimalField(decimal_places=2, default=55, max_digits=5),
        ),
        migrations.AlterField(
            model_name='breed',
            name='min_height_female',
            field=models.DecimalField(decimal_places=2, default=5, max_digits=5),
        ),
        migrations.AlterField(
            model_name='breed',
            name='min_height_male',
            field=models.DecimalField(decimal_places=2, default=5, max_digits=5),
        ),
        migrations.AlterField(
            model_name='breed',
            name='min_weight_female',
            field=models.DecimalField(decimal_places=2, default=5, max_digits=5),
        ),
        migrations.AlterField(
            model_name='breed',
            name='min_weight_male',
            field=models.DecimalField(decimal_places=2, default=5, max_digits=5),
        ),
        migrations.AlterField(
            model_name='dog',
            name='height',
            field=models.DecimalField(blank=True, decimal_places=2, default=23, max_digits=5),
        ),
        migrations.AlterField(
            model_name='dog',
            name='weight',
            field=models.DecimalField(decimal_places=2, default=5, max_digits=5),
        ),
    ]
