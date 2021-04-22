from django.db import models

from user.models import HandProductSuplier

from .validators import  file_size_validator
class HandProductCat(models.Model):
    name = models.CharField(max_length=255)


class HandProductCity(models.Model):
    city = models.CharField(max_length = 255)


class HandProduct(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(HandProductCat , on_delete=models.CASCADE, related_name='hand_product')
    city = models.ForeignKey(HandProductCity, on_delete=models.CASCADE, related_name="hand_product")
    supplier = models.ForeignKey(HandProductSuplier, on_delete=models.CASCADE)
    price = models.FloatField()
    img_one = models.ImageField(upload_to="hand_product/")
    img_two = models.ImageField(upload_to="hand_product/", null=True, blank=True)
    img_three = models.ImageField(upload_to="hand_product/", null=True, blank=True)
    video_description = models.FileField(upload_to='hand_product_video/', null=True, blank=True, validators=[file_size_validator])

class HandProductComment(models.Model):
    hand_product= models.ForeignKey(HandProduct, on_delete=models.CASCADE, related_name='comment')
    text = models.TextField(null=True, blank=True)
    rate = models.IntegerField(null=True, blank=True)