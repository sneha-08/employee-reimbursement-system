from django.db import models

# Create your models here.
class Expense(models.Model):
    item = models.CharField(max_length = 50)
    eid = models.IntegerField()
    amount = models.IntegerField()
    category = models.CharField(max_length=50)
    date = models.DateField()
    status = models.CharField(default= "ON PROCESS",max_length=50)

    def __str__(self):
        return self.name