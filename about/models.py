from django.db import models
from .fields import IntegerRangeField
import datetime
from django.utils import timezone

class Achievement(models.Model):
    date=models.DateField()
    title=models.CharField(max_length=30)
    def __str__(self):
        return self.title















