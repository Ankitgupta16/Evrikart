from django.db import models
class Urstore(models.Model):
    user_id = models.IntegerField(default=0)
    banner = models.ImageField(upload_to='products/')
    profile_pic = models.ImageField(upload_to='products/')
    store_name = models.CharField(max_length=58)
    address1 = models.CharField(max_length=58)
    address2 = models.CharField(max_length=58)
    city = models.CharField(max_length=28)
    zipcode = models.CharField(max_length=20)
    country = models.CharField(max_length=28)
    state = models.CharField(max_length=28)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    # Create / Insert / Add - POST
    # Retrieve /  Fetch - GET
    # Update / Edit - PUT
    # Delete / Remove - DELETE



# Create your models here.
