from django.db import models
from .fields import IntegerRangeField
import datetime
from django.utils import timezone

class Games(models.Model):
    title=models.CharField(max_length=20)
    date=models.DateField()
    about=models.CharField()
    def __str__(self):
        return self.title
class People():
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=20)
    def __str__(self):
        return self.first_name

class Rating():
    stars=IntegerRangeField(min_value=0,max_value=5)
    feedback=models.CharField(max_length=300)
    def __str__(self):
        return self.stars









