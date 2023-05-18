from django import forms

class PostForm(forms.Form):
    stdName = forms.CharField(max_length = 50, initial = "" , required=True)
    stdId = forms.CharField(max_length = 10, initial = "" ,required=True)
    stdSex =  forms.CharField(max_length = 2, initial = "M" )
    stdBirth =  forms.DateField()
    stdAddress =  forms.CharField(max_length = 255, initial = "",required=True)
    stdPhone =  forms.CharField(max_length = 10, initial = "",required=False)
    stdEmail =  forms.CharField(max_length = 255, initial = "", required=False)
