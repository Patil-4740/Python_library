from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField()
    age=models.IntegerField()
    subject=models.CharField(max_length=100)
    marks=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name
    
  