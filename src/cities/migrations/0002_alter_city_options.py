# Generated by Django 4.0.5 on 2022-06-28 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['name'], 'verbose_name': 'Город', 'verbose_name_plural': 'Города'},
        ),
    ]
