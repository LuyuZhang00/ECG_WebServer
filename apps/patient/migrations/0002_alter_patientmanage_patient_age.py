# Generated by Django 4.1.7 on 2023-03-18 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientmanage',
            name='patient_age',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='患者年龄'),
        ),
    ]
