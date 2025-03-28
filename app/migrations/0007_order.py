# Generated by Django 5.1.6 on 2025-03-22 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_buy_register"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("product", models.CharField(max_length=255)),
                ("product_name", models.CharField(max_length=255)),
                ("product_id", models.DecimalField(decimal_places=2, max_digits=10)),
                ("product_type", models.CharField(max_length=255)),
                ("buyer_name", models.CharField(max_length=100)),
                ("buyer_email", models.EmailField(max_length=254)),
                ("buyer_phone", models.CharField(max_length=15)),
                ("quantity", models.PositiveIntegerField()),
                ("order_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
