from django.db import models
from django.conf import settings

# Create your models here.
class Add_user(models.Model) :
    ngo_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=12)
    address = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=10)
    image = models.ImageField(upload_to='pics',default="")

    def __str__(self) :
        return self.name

class Postimg(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE)
    caption=models.CharField(max_length=500)
    image=models.ImageField(upload_to="img/%y")
    def __str__(self):
        return str(self.user)

class DonateClothes(models.Model):
    email = models.EmailField()
    quantity = models.IntegerField(default="0")
    type = models.CharField(max_length=500,default="")

class DonateFood(models.Model):
    email = models.EmailField()
    quantity = models.IntegerField(default="0")
    type = models.CharField(max_length=500,default="")

class DonateStationary(models.Model):
    email = models.EmailField()
    quantity = models.IntegerField(default="0")
    type = models.CharField(max_length=500,default="")

class DonateTime(models.Model):
    email = models.EmailField()
    date = models.IntegerField(default="0")
    type = models.CharField(max_length=500,default="")

class DonateBlood(models.Model):
    email = models.EmailField()
    date = models.CharField(max_length=20,default="")
    type = models.CharField(max_length=500,default="")
    disease = models.CharField(max_length=100,default="")



