# Generated by Django 2.0.3 on 2018-04-04 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CraftScapeDatabase', '0002_auto_20180403_0230'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='static_game_item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='skill', to='CraftScapeDatabase.StaticGameItem'),
            preserve_default=False,
        ),
    ]
