# Generated by Django 4.1.7 on 2023-11-07 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0002_remove_plant_stage_plant_stages_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stageplanning',
            old_name='humididty',
            new_name='humidity',
        ),
    ]
