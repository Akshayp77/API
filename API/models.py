from django.db import models
from django.db.models.base import Model

class Emp(models.Model):
    name=models.CharField(max_length=50)
    e_id=models.IntegerField()
    salary=models.IntegerField()
