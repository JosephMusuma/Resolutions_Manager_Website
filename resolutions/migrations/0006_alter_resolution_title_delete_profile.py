# Generated by Django 5.0.6 on 2024-06-21 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resolutions', '0005_alter_profile_first_name_alter_profile_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resolution',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]