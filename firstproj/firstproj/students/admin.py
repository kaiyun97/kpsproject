from django.contrib import admin
from students.models import student


# Register your models here.

class studentAdmin(admin.ModelAdmin):
        list_display = ('id','stdId','stdSex','stdBirth')
        list_filter =  ('stdId','stdSex',)
        search_fields = ('stdId','stdSex',)
        ording = 'id'
admin.site.register(student,studentAdmin)