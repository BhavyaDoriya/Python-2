from django.db import models

# Create your models here.
class Evaluation(models.Model):
    fac_name=models.TextField()
    sub=models.TextField()
    score=models.IntegerField()
    email=models.TextField()
    
    def __str__(self):
        return self.sub