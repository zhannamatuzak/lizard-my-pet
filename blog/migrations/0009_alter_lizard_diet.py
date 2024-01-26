# Generated by Django 5.0.1 on 2024-01-26 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_lizard_diet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lizard',
            name='diet',
            field=models.CharField(choices=[('0', 'Not defined'), ('1', 'Omnivorous'), ('2', 'Herbivorous'), ('3', 'Insectivorous')], default='0', max_length=25),
        ),
    ]
