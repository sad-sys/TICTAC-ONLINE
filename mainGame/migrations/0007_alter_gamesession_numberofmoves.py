# Generated by Django 5.0 on 2024-02-12 21:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainGame", "0006_gamesession_numberofmoves"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gamesession",
            name="numberOfMoves",
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
