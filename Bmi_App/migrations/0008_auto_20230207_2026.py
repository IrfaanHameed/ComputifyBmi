# Generated by Django 3.2.6 on 2023-02-07 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bmi_App', '0007_customer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='height',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='customer',
            name='weight',
            field=models.FloatField(),
        ),
    ]
