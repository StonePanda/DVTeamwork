"""dvone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,re_path
from screenone import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path(r'index/',views.index),
    path(r'index/keyword',views.keyword),

    path(r'search/',views.search),
    path(r'searchsuggest/',views.searchsuggest),
    path(r'dv/chosedid',views.getchosedid),
    path(r'dvresult/',views.dvresult),

    path(r'views/view1',views.view1),#http://127.0.0.1:8000/views/view1  柱状图
    path(r'views/view2',views.view2),#http://127.0.0.1:8000/views/view2  旭日图
    path(r'views/view3',views.view3),#http://127.0.0.1:8000/views/view3  评论列表
    path(r'views/view35',views.view35),#http://127.0.0.1:8000/views/view3  评论列表
    path(r'views/view34',views.view34),#http://127.0.0.1:8000/views/view3  评论列表
    path(r'views/view33',views.view33),#http://127.0.0.1:8000/views/view3  评论列表
    path(r'views/view32',views.view32),#http://127.0.0.1:8000/views/view3  评论列表
    path(r'views/view31',views.view31),#http://127.0.0.1:8000/views/view3  评论列表
    path(r'views/view4',views.view4),#http://127.0.0.1:8000/views/view4  云文字
    path(r'views/view45',views.view45),#http://127.0.0.1:8000/views/view4  云文字
    path(r'views/view44',views.view44),#http://127.0.0.1:8000/views/view4  云文字
    path(r'views/view43',views.view43),#http://127.0.0.1:8000/views/view4  云文字
    path(r'views/view42',views.view42),#http://127.0.0.1:8000/views/view4  云文字
    path(r'views/view41',views.view41),#http://127.0.0.1:8000/views/view4  云文字
    path(r'views/view5',views.view5),#http://127.0.0.1:8000/views/view5  演员获奖打卡图
    #re_path(r'^index/searchsuggest$',views.keyword)
]
