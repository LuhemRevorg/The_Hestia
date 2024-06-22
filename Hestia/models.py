from django.db import models
from django.conf import settings
from datetime import date


class Client(models.Model):
    """
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    email = models.EmailField(max_length=100, unique=True, null=False)
    uni_email = models.EmailField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    university = models.CharField(max_length=100, blank=True)
    

    def __str__(self):
        return self.user.username



class Property(models.Model):
    prop_id = models.AutoField(primary_key=True)
    street1 = models.CharField(max_length=30, null=False)
    street2 = models.CharField(max_length=30, blank=True)
    zip_code = models.CharField(max_length=7, null=False)
    province = models.CharField(max_length=2, null=False)
    city = models.CharField(max_length=20, null=False, default='Waterloo')
    university = models.CharField(max_length=50, null=False)
    apartment = models.CharField(max_length=20, null=False, default='Apartment')
    rooms = models.IntegerField(null=False)
    price = models.IntegerField(null=False)
    duration = models.IntegerField(null=False)
    date = models.DateField(default=date.today)
    description = models.CharField(max_length=255, blank=True,null=False)
    cover_image = models.ImageField(upload_to='images/', null = False)
    image_01 = models.ImageField(upload_to='images/', null = True)
    image_02 = models.ImageField(upload_to='images/', null = True)
    image_03 = models.ImageField(upload_to='images/', null = True)
    image_04 = models.ImageField(upload_to='images/', null = True)
    image_05 = models.ImageField(upload_to='images/', null = True)
    furnished = models.CharField(max_length=3)
    bathrooms = models.IntegerField(null = False)
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='properties'
    )
    

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

class Cart(models.Model):
    item_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        Client,
        on_delete=models.CASCADE
    )

    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
    )
    
    

    def __str__(self):
        return f"Property for {self.user}"

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'
