from django.db import models

# Create your models here.

class Stock(models.Model):
	ticker = models.CharField(max_length=4)
	price = models.FloatField(default=0)

class Call(models.Model):
	call_date = models.DateField()
	call_strike = models.FloatField(default=0)
	call_premium = models.FloatField(default=0)

class Put(models.Model):
	put_date = models.DateField()
	put_strike = models.FloatField(default=0)
	put_premium = models.FloatField(default=0)

class Spread(models.Model):
	spread_name = models.CharField(max_length=100)
