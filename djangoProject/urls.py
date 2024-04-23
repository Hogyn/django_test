"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.urls import path,re_path
from django.urls import path, include

import index.views
from article import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/',include('article.urls')),
    # path('articles',views.article_list),
    # path('articles/<int:year>/',views.year_archive),
    # path('articles/<int:year>/<int:month>/',views.month_archive),
    # path('articles/<int:year>/<int:month>/<slug:slug>/',views.article_detail),
    path('', index.views.index, name='index'),
]
