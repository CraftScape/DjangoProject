# Generated by Django 2.0.3 on 2018-04-03 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CraftScapeDatabase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticgameitem',
            name='base_durability',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='staticgameitem',
            name='min_level',
            field=models.IntegerField(default=1),
        ),
    ]
