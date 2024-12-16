from django.db import models

# Create your models here.
class Userdata(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phno=models.CharField(max_length=10)
    gender_choices=(
        ('M','Male'),
        ('F','Female'),
        ('O','Others')
    )
    gender=models.CharField(max_length=1,choices=gender_choices)
    staddress=models.CharField(max_length=100,blank=False)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=10)
    def __str__(self):
        return self.name
