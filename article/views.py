from django.shortcuts import render
from article.models import Article,User
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def article_list(request):
    return HttpResponse("Hello, world. You're at the article list.")

def year_archive(request,year):
    return HttpResponse(f'Hello, world.year_archive函数接受参数 year:{year}')

def month_archive(request,year,month):
    return HttpResponse(f'month_archive函数接受参数 year:{year},month:{month}')

def article_detail(request,year,month,slug):
    return HttpResponse(f'article_detail接受函数参数 year:{year},month:{month},slug:{slug}')

def get_current_datetime(request):
    today = datetime.today()
    formatted_today = today.strftime('%Y-%m-%d')
    html = f"<html><body>今天是{formatted_today}</body></html>"
    return HttpResponse(html)

def article_list(request):
    articles = Article.objects.all()#调用数据库中article表
    return  render(request, 'article_list.html', {"articles":articles})