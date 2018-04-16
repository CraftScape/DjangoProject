# Generated by Django 2.0.3 on 2018-04-14 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CraftScapeDatabase', '0007_remove_gameitemtype_static_game_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='staticgameitem',
            name='item_types',
            field=models.ManyToManyField(related_name='static_game_item', to='CraftScapeDatabase.GameItemType'),
        ),
    ]
