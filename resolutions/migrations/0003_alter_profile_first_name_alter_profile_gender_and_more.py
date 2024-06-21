# Generated by Django 5.0.6 on 2024-06-21 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resolutions', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=12),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=40),
        ),
    ]