# Generated by Django 5.0 on 2024-02-07 20:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainGame", "0004_alter_gamesession_gamestate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gamesession",
            name="gameState",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
