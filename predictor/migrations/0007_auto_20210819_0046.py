# Generated by Django 3.0.5 on 2021-08-18 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0006_doctorhospital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorhospital',
            name='phone_no',
            field=models.CharField(max_length=25),
        ),
    ]