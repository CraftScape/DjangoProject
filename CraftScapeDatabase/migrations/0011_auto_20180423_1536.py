# Generated by Django 2.0.3 on 2018-04-23 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CraftScapeDatabase', '0010_equipment_shoulders'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='x_pos',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='y_pos',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
