# Generated by Django 3.2.16 on 2024-01-19 11:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20240119_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='body',
            field=models.TextField(help_text='Share your experience in 800 Characters', max_length=800),
        ),
        migrations.AlterField(
            model_name='experience',
            name='pet_name',
            field=models.CharField(help_text='Format: Letters only and max 80 characters', max_length=80, validators=[django.core.validators.RegexValidator(code='invalid_letters_only', message='Only letters are allowed.', regex='^[a-zA-Z]*$')]),
        ),
        migrations.AlterField(
            model_name='experience',
            name='size',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1, message='Ensure this value is greater than or equal to 1.'), django.core.validators.MaxValueValidator(100, message='Ensure this value is less than or equal to 100.')]),
        ),
        migrations.AlterField(
            model_name='lizard',
            name='diet_list',
            field=models.TextField(help_text='Format: Letters only and max 400 characters', max_length=400, validators=[django.core.validators.RegexValidator(message='Ensure the body only contains letters, numbers, spaces, commas, periods, and exclamation/question marks.', regex='^[A-Za-z0-9\\s\\.,!?]*$')]),
        ),
    ]