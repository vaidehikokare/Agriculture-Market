# Generated by Django 5.1.6 on 2025-03-20 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_alter_sell_register_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sell_register",
            name="username",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
