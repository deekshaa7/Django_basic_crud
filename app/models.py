from django.db import models

class Student_details(models.Model):
    name = models.CharField(max_length=30)
    phone = models.IntegerField(max_length=13,blank=True,null=True)
    email = models.EmailField(max_length=100)
    roll_no=models.CharField(max_length=10)
    city = models.CharField(max_length=50,default="Bhopal")


class Marks(models.Model):
    hindi = models.IntegerField(default=0)
    english = models.IntegerField(default=0)
    mathe = models.IntegerField(default=0)
    biology = models.IntegerField(default=0)
    physics = models.IntegerField(default=0)
    date = models.DateField(auto_now=True)
    amount = models.FloatField()
    roll_no = models.ForeignKey(to=Student_details,on_delete=models.CASCADE)

    def __str__(self):
        return self.roll_no.name + " : " + self.date