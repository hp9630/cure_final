# Generated by Django 4.0.8 on 2024-01-19 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0024_doctor_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='department',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, to='app1.department'),
            preserve_default=False,
        ),
    ]