# Generated by Django 4.2 on 2023-04-19 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0002_employeemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemodel',
            name='address',
            field=models.CharField(max_length=200),
        ),
    ]