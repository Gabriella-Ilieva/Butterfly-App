# Generated by Django 4.2.3 on 2023-08-03 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='story',
            options={'ordering': ('-date_of_publication',)},
        ),
    ]