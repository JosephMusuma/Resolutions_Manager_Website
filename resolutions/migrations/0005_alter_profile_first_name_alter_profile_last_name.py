# Generated by Django 5.0.6 on 2024-06-21 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resolutions', '0004_alter_profile_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
