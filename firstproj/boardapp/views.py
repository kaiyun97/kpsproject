from django.shortcuts import render, redirect
from boardapp import models, forms
from django.contrib.auth import authenticate
from django.contrib import auth
import math

page = 0  #目前頁面,0為第1頁

def showpost(request, pageindex=None):  #首頁
	global page  #重複開啟本網頁時需保留 page1 的值
	pagesize = 3  #每頁顯示的資料筆數
	boardall = models.BoardUnit.objects.all().order_by('-id')  #讀取資料表,依時間遞減排序
	datasize = len(boardall)  #資料筆數
	totpage = math.ceil(datasize / pagesize)  #總頁數
	if pageindex==None:  #無參數
		page = 0
		boardunits = models.BoardUnit.objects.order_by('-id')[:pagesize]
	elif pageindex=='prev':  #上一頁
		start = (page-1)*pagesize  #該頁第1筆資料
		if start >= 0:  #有前頁資料就顯示
			boardunits = models.BoardUnit.objects.order_by('-id')[start:(start+pagesize)]
			page -= 1
	elif pageindex=='next':  #下一頁
		start = (page+1)*pagesize  #該頁第1筆資料
		if start < datasize:  #有下頁資料就顯示
			boardunits = models.BoardUnit.objects.order_by('-id')[start:(start+pagesize)]
			page += 1
	currentpage = page + 1  #將目頁前頁面以區域變數傳回html
	return render(request, "boardapp/showpost.html", locals())

def addpost(request):  #新增留言
	if request.method == "POST":  #如果是以POST方式才處理
		postform = forms.PostForm(request.POST)  #建立forms物件
		if postform.is_valid():  #通過forms驗證
			title = postform.cleaned_data['btitle']  #取得輸入資料
			name =  postform.cleaned_data['bname']
			gender =  request.POST.get('bgender', None)
			email = postform.cleaned_data['bemail']
			content =  postform.cleaned_data['bcontent']
			unit = models.BoardUnit.objects.create(bname=name, bgender=gender, btitle=title, bemail=email, bcontent=content, bresponse='')  #新增資料記錄
			unit.save()  #寫入資料庫
			message = '已儲存...'
			postform = forms.PostForm()
			return redirect('boardapp/showpost/')	
		else:
		  message = '驗證碼錯誤！'	
		  
	else:
		message = '標題、姓名、內容及驗證碼必須輸入！'
		postform = forms.PostForm()
	return render(request, "boardapp/addpost.html", locals())