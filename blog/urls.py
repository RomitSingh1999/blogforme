from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns=[
    path('', views.Blog, name='Blog'),
    #path('static/noobie.html/', views.Blog, name='Blog'),
    path('index.html', views.index, name='index'),
    path('categori.html', views.categori, name='categori'),
    path('about.html', views.about, name='about'),
    path('latest_news.html', views.latest, name='latest'),
    path('contact.html', views.contact, name='contact'),
    path('texting',views.text_datas,name='text_datas')
    

]