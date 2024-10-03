from django.db import models
from embed_video.fields import EmbedVideoField
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Manager(models.Model):
    name = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    whatsapp = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name


class PriceRange(models.Model):
    name = models.CharField(max_length=50, blank=True, default=1)

    def __str__(self):
        return self.name

class Rooms(models.Model):
    room = models.CharField(max_length=100, blank=True)
    price = models.CharField(max_length=100, blank=True)
    description =  models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.room
    
class Amenities(models.Model):
    name = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    rate = models.CharField(max_length=10)
    price = models.DecimalField(default=0 , decimal_places=2, max_digits=9)
    description = models.TextField()
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    vicinity = models.CharField(max_length=100)
    rooms = models.ManyToManyField(Rooms,blank=True)
    amenities = models.ManyToManyField(Amenities,blank=True)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, default=None)
    image1 = models.ImageField(upload_to='uploads/products/')
    image2 = models.ImageField(upload_to='uploads/products/', null=True)
    image3 = models.ImageField(upload_to='uploads/products/', null=True)
    image4 = models.ImageField(upload_to='uploads/products/', null=True)
    image5 = models.ImageField(upload_to='uploads/products/', null=True)
    pricerange = models.ForeignKey(PriceRange, on_delete=models.CASCADE, blank=True,null=True)
    rules = models.TextField(default=000, blank=True, null=True)
    condition = models.TextField(default=000, blank=True,null=True)
    map = models.URLField(max_length=500, null=True, default=0)
    landmark = models.TextField(max_length=200, null=True, default=0)
    video = EmbedVideoField(blank=True,null=True)

    def __str__(self):
        return self.name
    
