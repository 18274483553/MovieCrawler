# -*- coding: utf-8 -*-
import json

from ShowModule.Util import MovieFileUtil
from django.shortcuts import render, HttpResponse

def index(request):
    '''
    @功能说明：处理主页访问请求
    '''
    context = {}
    return render(request, 'index.html', context)

def movielist(request):
    '''
    @功能说明：处理电影列表页访问请求
    '''
    context = {}
    context["movies"] = MovieFileUtil.readMovieFile()
    return render(request, 'movielist.html', context)
    
def moviechart(request):
    '''
    @功能说明：处理电影图表页访问请求
    '''
    context = {}
    return render(request, 'moviechart.html', context)

def getpiaofang(request):
    movies = MovieFileUtil.readMovieFile(request.POST.get('param'), request.POST.get('isnum'))
    return  HttpResponse(movies)
