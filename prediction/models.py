from django.db import models

# Create your models here.

class Stock(models.Model):
    stocker = models.CharField(max_length=50)
    stock_date = models.DateField()
    stock_price = models.FloatField()
    stock_high = models.FloatField()
    stock_low = models.FloatField()
    no_shares = models.FloatField()
    stock_final_price = models.FloatField()
    
    
