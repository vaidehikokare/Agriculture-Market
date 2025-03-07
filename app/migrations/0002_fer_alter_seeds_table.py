# Generated by Django 5.1.6 on 2025-03-07 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fertilizerName', models.CharField(max_length=255)),
                ('fertilizerType', models.CharField(choices=[('Organic', 'Organic'), ('Inorganic', 'Inorganic'), ('Biofertilizer', 'Biofertilizer'), ('Others', 'Others')], max_length=50)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('contactName', models.CharField(max_length=255)),
                ('contactEmail', models.EmailField(max_length=254)),
                ('contactPhone', models.CharField(max_length=15)),
                ('description', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='crop_photos/')),
                ('inputState', models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Maharashtra', 'Maharashtra'), ('West Bengal', 'West Bengal'), ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands')], max_length=50)),
                ('inputDistrict', models.CharField(max_length=100)),
                ('streetAddress', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'fer',
            },
        ),
        migrations.AlterModelTable(
            name='seeds',
            table='seeds',
        ),
    ]
