from django.contrib import admin
from . import models

admin.site.register(models.Flower) 
admin.site.register(models.Category) 
admin.site.register(models.Tag)
# Register your models here.
