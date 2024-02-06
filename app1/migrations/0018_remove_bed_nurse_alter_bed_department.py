# Generated by Django 4.0.8 on 2024-01-18 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_rename_name_bed_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bed',
            name='nurse',
        ),
        migrations.AlterField(
            model_name='bed',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.nurses'),
        ),
    ]