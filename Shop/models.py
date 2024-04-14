from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    poster = models.ImageField(upload_to='images/')
    description = models.TextField()
    reting = models.PositiveIntegerField()
    is_available = models.BooleanField()
    price = models.FloatField()
    discount = models.PositiveSmallIntegerField()
    stock = models.PositiveIntegerField()

class Review(models.Model):
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)
    photo = models.ImageField(upload_to='images/reviews/photos/', blank=True, null=True)
    text = models.TextField()