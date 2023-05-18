from django.shortcuts import render,redirect

from students.models import student
from students.form import PostForm

def listone(request):
    try:
        unit = student.objects.get(stdName="s1")
    except:
        errormessage = "讀取錯誤!"
    return render(request, "student/listone.html",locals())

def listall(request):
    allStudents = student.objects.all().order_by('id')
    return render(request,"student/listall.html",locals())


def post(request):
    if request.method == "POST":
        mess = request.POST['stdName']
        mess = mess + " " + request.POST['stdId']
        mess = mess + " " + request.POST['stdSex']
        mess = mess + " " + request.POST['stdBirth']
        mess = mess + " " + request.POST['stdAddress']
        mess = mess + " " + request.POST['stdPhone']
        mess = mess + " " + request.POST['stdEmail']

    else:
        mess = "資料表單尚未送出!"
    return render(request, "student/addstudent.html", locals())

def post1(request):
    if request.method == "POST":
        stdName = request.POST['stdName']
        stdId = request.POST['stdId']
        stdSex = request.POST['stdSex']
        stdBirth =  request.POST['stdBirth']
        stdAddress =  request.POST['stdAddress']
        stdPhone =  request.POST['stdPhone']
        stdEmail =  request.POST['stdEmail']
        unit = student.objects.create(stdName=stdName, stdId=stdId,stdSex=stdSex,stdBirth=stdBirth, stdAddress=stdAddress,stdPhone=stdPhone,stdEmail=stdEmail)
        unit.save()
        return redirect('/post1')
    else:
        mess = "請輸入資料(資料不作驗證)"

    return render(request, "student/addstudent1.html",  locals())    

def postform(request):
    stdform = PostForm()
    return render(request, "student/stdform.html",  locals())


def delete(request, stdId = None):
    if stdId != None:
        if request.method == "POST":
            stdId = request.POST["stdId"]
        try:
            unit = student.objects.get(stdId=stdId)
            unit.delete()
            return redirect('student/delete.html')
        except:
            mess = "查無該學號"
    return render(request, "student/delete.html",  locals())

def edit(request, stdId = None ,mode= None):
    if mode == "edit":
        unit = student.objects.get(stdId=stdId)
        unit.stdName = request.GET["stdName"]
        unit.stdId = request.GET["stdId"]
        unit.stdSex = request.GET["stdSex"]
        unit.stdBirth = request.GET["stdBirth"]
        unit.stdEmail = request.GET["stdEmail"]
        unit.stdPhone = request.GET["stdPhone"]
        unit.stdAddress = request.GET["stdAddress"]
        unit.save()
        mess = "已修改完成"
        return redirect('hello')
    else:
        try:
            unit = student.objects.get(stdId=stdId)
            strDate = str(unit.stdBirth)
            strDate2 = strDate.replace(" 年 ", "-")
            strDate2 = strDate.replace(" 月 ", "-")
            strDate2 = strDate.replace(" 日 ", "-")
            unit.stdBirth = strDate2
        except:
            mess = "該學號不存在"
    return render(request, "student/edit.html",  locals())


