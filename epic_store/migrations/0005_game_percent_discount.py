# Generated by Django 5.2.1 on 2025-05-11 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epic_store', '0004_alter_game_game_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='percent_discount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
