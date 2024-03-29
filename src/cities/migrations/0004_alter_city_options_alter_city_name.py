# Generated by Django 4.0.5 on 2023-03-28 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0003_alter_city_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['name'], 'verbose_name': 'Місто', 'verbose_name_plural': 'Міста'},
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Місто'),
        ),
    ]
