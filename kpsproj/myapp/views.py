from django.shortcuts import render

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