from django.shortcuts import render
import random
from django.http import HttpResponse
from datetime import datetime
def student(request):
    std1 = {"name": "SUN", "sid": "1111", "age":"18" }
    std2 = {"name": "KAI", "sid": "1112", "age":"18" }
    std3 = {"name": "PEI", "sid": "1113", "age":"18" }
    stds = [std1,std2,std3]
    return render(request,'std.html',locals())
    
    
def hello(request):

    #return HttpResponse("Hello World");
    return render(request,'hello.html')
    
def hello1(request,username):
    now = datetime.now()
    return render(request,'hello1.html',locals())
#globl全域變數
times = 0;
def hello2(request,username):
    global times
    times = times + 1
    local_times = times
    now = datetime.now()
    dice1 = dice()
    dice2 = dice()
    dice3 = dice()
    
    score = random.randint(0,100)
    #dict1 = {"dice1": dice1, "dice2": dice2, "dice3": dice3}
    return render(request,'hello2.html', locals())
    
def dice():
    return  random.randint(1,6)
    
    

