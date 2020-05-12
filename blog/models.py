from django.db import models
#from django.utils import Date
class blogging(models.Model):
    head=models.TextField()
    img=models.ImageField(upload_to='pics')
    blo=models.TextField()
    desc=models.DateField(auto_now=True)
# Create your models here.
