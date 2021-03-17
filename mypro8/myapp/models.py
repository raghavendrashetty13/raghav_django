from __future__ import unicode_literals
from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=26,unique=True)
    phone = models.IntegerField(default='91',max_length=12,unique=True)
    mail = models.EmailField(max_length=254,blank=True,unique=True)
    message=models.CharField(max_length=26,unique=True)

    class Meta:
        db_table = "Student"
