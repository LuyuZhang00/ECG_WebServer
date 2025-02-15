# Generated by Django 4.1.7 on 2023-03-25 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0004_alter_patientmanage_patient_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientmanage',
            name='patient_department',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='挂号科室'),
        ),
        migrations.AlterField(
            model_name='patientmanage',
            name='patient_describe',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='患者描述'),
        ),
        migrations.AlterField(
            model_name='patientmanage',
            name='patient_telephone',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='患者电话'),
        ),
    ]
