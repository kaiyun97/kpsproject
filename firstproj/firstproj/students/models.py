from django.db import models

class student(models.Model):
    stdName = models.CharField(max_length = 50, null = False)
    stdId = models.CharField(max_length = 10, null = False)
    stdSex =  models.CharField(max_length = 50, default = 'M', null = False)
    stdBirth =  models.DateField(null = False)
    stdAddress =  models.CharField(max_length = 255, blank = True, default = "")
    stdPhone =  models.CharField(max_length = 10, blank = True,default = "")
    stdEmail =  models.CharField(max_length = 255, blank = True, default = "")

    def __str__(self):
        return self.stdName



# Create your models here.