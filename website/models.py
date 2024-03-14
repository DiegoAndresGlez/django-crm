from django.db import models

# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) #when created save time and date
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)

    def __str__(self): #if calling a record like in for record in records in views print this
        return(f"{self.first_name} {self.last_name}")