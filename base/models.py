from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email=models.EmailField(null=True)
    REQUIRED_FIELDS =[]
    
    def __str__(self):
        return self.username
    
    
class Post(models.Model):
    host=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.TextField(blank=True,null=True)
    img=models.ImageField(null=True,blank=True,upload_to="images/")
    
    def __str__(self):
        return self.host.username