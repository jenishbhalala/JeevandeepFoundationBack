# Generated by Django 4.0.5 on 2022-06-23 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_contact_donor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='location',
            field=models.CharField(max_length=100),
        ),
    ]
