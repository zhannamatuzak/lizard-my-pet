# Generated by Django 5.0.1 on 2024-02-04 09:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_lizard_diet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='size',
            field=models.IntegerField(default=1, help_text='Min 1, max 100', validators=[django.core.validators.MinValueValidator(1, message='Ensure this value is greater than or equal to 1.'), django.core.validators.MaxValueValidator(100, message='Ensure this value is less than or equal to 100.')]),
        ),
    ]
