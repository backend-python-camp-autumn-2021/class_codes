from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

User = get_user_model()


class HostelCategory(models.Model):
    name = models.CharField(max_length=250)


class HostAddress(models.Model):
    pass


class HostImage(models.Model):
    img = models.ImageField(upload_to="host/", null=True, blank=True)


class Host(models.Model):
    cat = models.ForeignKey(HostelCategory, on_delete=models.CASCADE)
    address = models.ForeignKey(HostAddress, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    reserved = models.BooleanField(default=False)
    img = models.ForeignKey(HostImage, on_delete=models.CASCADE)


class HostComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    rate = models.FloatField(
        validators=[MinValueValidator(0.0),  MaxValueValidator(5.0)])
    text = models.CharField(max_length=500)
