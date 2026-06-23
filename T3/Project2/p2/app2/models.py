from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=80)
    roll=models.IntegerField()
    mark=models.PositiveBigIntegerField()
    
    def __str__(self):
        return self.name

class Player(models.Model):
    name=models.CharField(max_length=80)
    team=models.CharField(max_length=80)
    runs=models.PositiveIntegerField()
    birth_date=models.DateField()
    id=models.AutoField(primary_key=True)    
    def __str__(self):
        return self.name
