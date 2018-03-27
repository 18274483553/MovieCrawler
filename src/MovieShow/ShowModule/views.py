# -*- coding: utf-8 -*-
import json
import collections

from ShowModule.Util import MovieFileUtil
from django.shortcuts import render, HttpResponse

keywords = "疾风电影数据,疾风电影,热映电影,正在上映的电影,电影票房,电影评分,电影数据分析"
description = "疾风电影数据网，为您提供最需要的电影票房，排片，上座率，口碑评分等数据，采用可视化图表的方式呈现到您的面前。"

def index(request):
    '''
    @功能说明：处理主页访问请求
    '''
    context = {"keywords": keywords, "description": description}
    return render(request, 'index.html', context)

def movielist(request):
    '''
    @功能说明：处理电影列表页访问请求
    '''
    context = {"keywords": keywords, "description": description}
    context["movies"] = MovieFileUtil.readMovieFile()
    return render(request, 'movielist.html', context)
    
def moviechart(request):
    '''
    @功能说明：处理电影图表页访问请求
    '''
    context = {"keywords": keywords, "description": description}
    return render(request, 'moviechart.html', context)

def version(request):
    '''
    @功能说明：处理版本日志页访问请求
    '''
    context = {"keywords": keywords, "description": description}
    #初始化版本字典，对字典按插入顺序排序
    context["versions"] = collections.OrderedDict()
    context["versions"]["Version : v 1 . 2 . 2 . 20180327 _ Beta"] = [
                    "网站导航栏新增版本日志",
                    "解决电影票房表格在大屏幕下没有正确铺满屏幕的bug",
                    "优化网站冗余代码，提升运行效率",
                ]
    context["versions"]["Version : v 1 . 2 . 1 . 20180324 _ Beta"] = [
                    "网站测试版正式上线",
                ]
    context["versions"]["Version : v 1 . 1 . 3 . 20180312 _ Alpha"] = [
                    "修改豆瓣评分获取方式-通过精确搜索",
                    "修改时光网评分获取方式-通过精确搜索",
                    "新增从时光网获取电影时长和电影类型",
                    "优化输出文本",
                ]
    context["versions"]["Version : v 1 . 1 . 2 . 20180309 _ Alpha"] = [
                    "项目文件重构，移除了一些与项目无关的脚本",
                    "修改实时电影票房获取源，源网站更改为百度糯米",
                    "修改票房部分输出字段",
                    "解决百度糯米偶尔返回数据为空的bug",
                    "修改结果文件输出目录，由固定目录更改为程序当前工作目录",
                    "新增流程输出，实时汇报爬取进度",
                ]
    context["versions"]["Version : v 1 . 1 . 1 . 20180306 _ Alpha"] = [
                    "热映电影爬虫工具项目初始化",
                    "新增豆瓣热映电影爬虫脚本",
                    "新增热映电影整合爬虫脚本，自动整合实时电影票房，豆瓣和时光网的电影信息",
                    "新增爬虫工具包",
                ]
    
    return render(request, 'version.html', context)

def getpiaofang(request):
    movies = MovieFileUtil.readMovieFile(request.POST.get('param'), request.POST.get('isnum'))
    return  HttpResponse(movies)
