# Generated by Django 4.0.8 on 2024-01-18 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0018_remove_bed_nurse_alter_bed_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
