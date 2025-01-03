from django.db import models



# Create your models here.

#class for testcase
class booktestcase(models.Model):
    title=models.CharField(max_length=50)
    cost=models.IntegerField()

class samplemodel:
    img=str
    name=str
    no=int