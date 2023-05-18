from django import forms
from captcha.fields import CaptchaField

class PostForm(forms.Form):
    btitle = forms.CharField(max_length=100, initial='')
    bname = forms.CharField(max_length=20, initial='')
    bgender = forms.BooleanField()
    bemail = forms.EmailField(max_length=100, initial='', required=False)
    bcontent = forms.CharField(widget=forms.Textarea)
    captcha = CaptchaField()