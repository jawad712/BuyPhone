from django.db import models

# Create your models here.


class Specs(models.Model):
    mobile_ram = models.TextField()
    mobile_cpu= models.TextField()
    mobile_storage= models.TextField()
    mobile_color= models.TextField()
    mobile_other_features = models.TextField()
    date = models.DateField()
    
class Mobile(models.Model):
    mobile_name = models.CharField(max_length=150)
    mobile_img=models.ImageField(upload_to="BuyPhones_images")
    mobile_desc= models.TextField()
    date = models.DateField()
    id = models.OneToOneField(Specs,on_delete=models.CASCADE,primary_key=True)



class Review(models.Model):
    user_name = models.CharField(max_length=150)
    user_comments= models.TextField(max_length=300)
    date = models.DateField()
    mobile = models.ForeignKey(Mobile,on_delete=models.CASCADE,primary_key=True)
