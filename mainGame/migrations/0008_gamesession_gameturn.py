# Generated by Django 5.0 on 2024-02-14 10:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainGame", "0007_alter_gamesession_numberofmoves"),
    ]

    operations = [
        migrations.AddField(
            model_name="gamesession",
            name="gameTurn",
            field=models.IntegerField(default=0, null=True),
        ),
    ]
