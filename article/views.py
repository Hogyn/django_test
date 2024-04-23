from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def article_list(request):
    return HttpResponse("Hello, world. You're at the article list.")

def year_archive(request,year):
    return HttpResponse(f'Hello, world.year_archive函数接受参数 year:{year}')

def month_archive(request,year,month):
    return HttpResponse(f'month_archive函数接受参数 year:{year},month:{month}')

def article_detail(request,year,month,slug):
    return HttpResponse(f'article_detail接受函数参数 year:{year},month:{month},slug:{slug}')