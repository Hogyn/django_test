from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    # test=request.GET.get('test')
    # return HttpResponse("Hello, <a href='https://www.google.com'>"+test+".</a> You're at the polls index.")
    return HttpResponse("Hello, <a href='https://www.google.com'>U.</a> You're at the polls index.")