from django.shortcuts import render

from django.core.mail import send_mail
from django.http import BadHeaderError
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.template.loader import render_to_string

from myapp.form import ContactForm


def contact(request: HttpRequest) -> HttpResponse:
    """聯絡我們

    Args:
        request (HttpRequest): Http 請求

    Returns:
        HttpResponse: Http 回應
    """

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if not form.is_valid():
            return render(
                request,
                'contact.html',
                {
                    'form': form,
                }
            )

        subject = '聯絡我們'

        rendered_email = render_to_string(
            'contact_to_mail.html',
            {
                'email_address': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
                'name': form.cleaned_data['name'],
                'phone_number': form.cleaned_data['phone_number'],
            }
        )

        try:
            send_mail(
                subject=subject,
                message='',
                html_message=rendered_email,
                from_email='admin@example.com',
                recipient_list=['admin@example.com']
            )
        except BadHeaderError:
            return HttpResponse('Invalid header found.')

        return redirect('contact')

    form = ContactForm()

    return render(
        request,
        'contact.html',
        {
            'form': form,
        }
    )

# Create your views here.

from django.http import HttpResponse

def hello(request):
    return render(request, 'hello.html')

def Stype(request):
    return render(request, 'Stype.html')

def Ctype(request):
    return render(request, 'Ctype.html')

def Rtype(request):
    return render(request, 'Rtype.html')

def Etype(request):
    return render(request, 'Etype.html')

def Itype(request):
    return render(request, 'Itype.html')

def Atype(request):
    return render(request, 'Atype.html')

def group(request):
    return render(request, 'group.html')

def question(request):
    return render(request, 'question.html')

def video(request):
    return render(request, 'video.html')