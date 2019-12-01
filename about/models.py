from django.db import models
from .fields import IntegerRangeField
import datetime
from django.utils import timezone
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
class Achievement(models.Model):
    date=models.DateField()
    title=models.CharField(max_length=100)
    def __str__(self):
        return self.title
class Project(models.Model):
    date=models.DateField()
    name=models.CharField(max_length=30)
    link=models.URLField()
    imgUrl=models.CharField(max_length=30)
    def __str__(self):
        return self.name


class Skill(models.Model):
    info=models.CharField(max_length=30)

    def __str__(self):
        return self.info

class Interest(models.Model):
    info=models.CharField(max_length=30)

    def __str__(self):
        return self.info

class School(models.Model):
    start_year=models.IntegerField(validators=[MinValueValidator(1998),MaxValueValidator(2100)])
    end_year=models.IntegerField(validators=[MinValueValidator(1998),MaxValueValidator(2100)])
    name=models.CharField(max_length=30)


    def __str__(self):
        return self.name

class Club(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Experience(models.Model):
    date=models.DateField()
    info=models.CharField(max_length=100)
    def __str__(self):
        return self.info




# need a certifications model

# also need to look at model relationship thingy by reviewing model documentation in django














