import os
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import News,Image,NewsImage
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CommentForm
# Create your views here.

def index(request):
	return render(request,'news_app/index.html')
def konwladge(request):
	return render(request,'news_app/konwladge.html')
def group(request):
	return render(request,'news_app/group.html')
def news(request):
	text = News.objects.order_by('date_added')
	isrc = NewsImage.objects.order_by('date_added')
	context = {'text':text,'isrc':isrc}
	return render(request,'news_app/news.html',context)
def new(request,new_id):
	text = News.objects.get(id=new_id)
	isrc = NewsImage.objects.order_by('date_added')
	context = {'text':text,'isrc':isrc}
	return render(request,'news_app/new.html',context)
def culture(request):
	return render(request,'news_app/culture.html')
def beatiful(request):
	imgsrc = Image.objects.order_by('date_added')
	context = {'imgsrc':imgsrc}
	return render(request,'news_app/beatiful.html',context)
def home(request):
	return render(request,'news_app/home.html')
def come(request):
	return render(request,'news_app/come.html')
def old(request):
	text = News.objects.order_by('date_added')
	context = {'text':text}
	return render(request,'news_app/old.html',context)
def talk(request):
	return render(request,'news_app/talk.html')
def comment(request):
	if request.method != 'POST':
		form = CommentForm()
	else:
		form = CommentForm(data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('news_app:index'))
	context = {'form':form}
	return render(request,'news_app/comment.html',context)