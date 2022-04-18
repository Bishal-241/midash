from django.db import models
# from pytz import timezone
from django.utils.timezone import datetime

# Create your models here.
class Product(models.Model):
    pId = models.AutoField
    pName = models.CharField(max_length=50)
    pClass = models.IntegerField()
    pDate = models.DateField(default=datetime.now)
    
    pDesc = models.CharField(max_length=300)
    


