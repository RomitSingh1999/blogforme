from django.shortcuts import render
from blog.models import blogging
from django.utils import timezone 
from .forms import textinger  

def Blog(request):
    cont=blogging.objects.all()

    return render(request,'noobie.html',{'cont':cont})

def index(request):
    return render(request,'index.html')
def categori(request):
    return render(request,'categori.html')      
def about(request):
    return render(request,'about.html')
def latest(request):
    return render(request,'latest_news.html')
def contact(request):
    return render(request,'contact.html')
def text_datas(request):
    if request.method =='POST':
        text_ing=textinger(request.POST)
        if text_ing.is_valid():
            text_data= text_ing.cleaned_data['text_data']        
        
    return render(request, 'noobie.html',{'text_ing':text_ing})                