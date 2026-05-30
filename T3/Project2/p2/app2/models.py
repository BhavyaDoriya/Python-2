from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=80)
    roll=models.IntegerField()
    mark=models.PositiveBigIntegerField()
    
    def __str__(self):
        return self.name