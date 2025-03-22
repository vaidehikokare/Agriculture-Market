from django.db import models

class Crop(models.Model):
    CROP_TYPES = [
        ('Fruits', 'Fruits'),
        ('Vegetables', 'Vegetables'),
        ('Grains', 'Grains'),
        ('Others', 'Others')
    ]
    
    STATE_CHOICES = [
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Maharashtra', 'Maharashtra'),
        ('West Bengal', 'West Bengal'),
        ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
    ]

    crop_name = models.CharField(max_length=255)
    crop_type = models.CharField(max_length=50, choices=CROP_TYPES)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    contact_name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='crop_photos/', blank=True, null=True)
    state = models.CharField(max_length=50, choices=STATE_CHOICES)
    district = models.CharField(max_length=100)
    street_address = models.CharField(max_length=255)

    class Meta:
        db_table = 'crop'
class Seeds(models.Model):
    SEEDS_TYPES = [
        ('Fruits', 'Fruits'),
        ('Vegetables', 'Vegetables'),
        ('Grains', 'Grains'),
        ('Others', 'Others')
    ]
    
    STATE_CHOICES = [
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Maharashtra', 'Maharashtra'),
        ('West Bengal', 'West Bengal'),
        ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
    ]

    seedName = models.CharField(max_length=255)
    seedType = models.CharField(max_length=50, choices=SEEDS_TYPES)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    contactName = models.CharField(max_length=255)
    contactEmail = models.EmailField()
    contactPhone = models.CharField(max_length=15)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='crop_photos/', blank=True, null=True)
    inputState= models.CharField(max_length=50, choices=STATE_CHOICES)
    inputDistrict = models.CharField(max_length=100)
    streetAddress = models.CharField(max_length=255)

    class Meta:
        db_table = 'seeds'
class Fer(models.Model):
    fertilizer_TYPES = [
        ('Organic', 'Organic'),
        ('Inorganic', 'Inorganic'),
        ('Biofertilizer', 'Biofertilizer'),
        ('Others', 'Others')
    ]
    
    STATE_CHOICES = [
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Maharashtra', 'Maharashtra'),
        ('West Bengal', 'West Bengal'),
        ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
    ]

    fertilizerName = models.CharField(max_length=255)
    fertilizerType = models.CharField(max_length=50, choices=fertilizer_TYPES)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    contactName = models.CharField(max_length=255)
    contactEmail = models.EmailField()
    contactPhone = models.CharField(max_length=15)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='crop_photos/', blank=True, null=True)
    inputState= models.CharField(max_length=50, choices=STATE_CHOICES)
    inputDistrict = models.CharField(max_length=100)
    streetAddress = models.CharField(max_length=255)

    class Meta:
        db_table = 'fer'

class sell_register(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username= models.CharField(max_length=255,unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'sell_register'
class Buy_register(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username= models.CharField(max_length=255,unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'Buy_register'    

class Order(models.Model):
    product_name= models.CharField(max_length=255)
    product_id=models.DecimalField(max_digits=10, decimal_places=2)
    product_type = models.CharField(max_length=255)
    buyer_name = models.CharField(max_length=100)
    buyer_email = models.EmailField()
    buyer_phone = models.CharField(max_length=15)
    quantity = models.PositiveIntegerField()
          