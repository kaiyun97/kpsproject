from django.forms import CharField
from django.forms import EmailField
from django.forms import Form
from django.forms import Textarea

class ContactForm(Form):
    """聯絡我們表單
    """

    name = CharField(label='姓名', max_length=150)
    email_address = EmailField(label='信箱', max_length=150, required=False)
    # 不過濾
    phone_number = CharField(label='電話', max_length=20, required=False)
    message = CharField(label='內容', max_length=2000, widget=Textarea)
