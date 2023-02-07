from django.db import models
import math

# Create your models here.
class Customer(models.Model):
    Gender = (
        ('M','male'),
        ('F','female'),
    )

    name =  models.CharField(max_length=200,null=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=200,choices=Gender)
    height = models.FloatField()
    weight = models.FloatField()


    @property
    def get_bmi(self):
            height_in_meter = self.height/100
            square_height = height_in_meter * height_in_meter
            bmi = self.weight / square_height

            return round(bmi,1)
    
    def __str__(self):
        return self.name

 
 
      
      
    

    
