from django.db import models


class Data(models.Model):

    name = models.CharField(max_length=50)
    date = models.DateTimeField()
    description = models.CharField(max_length=99999)
   
    def __str__(self):
        return self.name