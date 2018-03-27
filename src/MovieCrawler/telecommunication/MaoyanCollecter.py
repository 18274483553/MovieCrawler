#coding=utf-8
'''
@文件名：maoyanCollecter.py
@创建时间：2018-03-09 15:28:38
@作者：疾风
@功能：从猫眼爬取正在热映电影的信息
'''
import re
import urllib
import requests

def getMaoyanScore(movies):
    '''
    @功能：获取猫眼评分等
    @入参：
        @param movies: list 存储数据对象
    @出参：
        @param movies: list 存储数据对象
    '''
    url = "http://maoyan.com/query"
    #将猫眼评分导入集合
    for movie in movies:
        print("\t处理中  正在抓取猫眼评分内容：" + movie["电影名"])
        querystring = {
            "kw": movie["电影名"],
        }
        headers = {
            'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
        }
        maoyan = requests.request("GET", url, headers=headers, params=querystring)
        #解析字典对象
        movie = getMaoyanData(maoyan, movie)
        if(movie.has_key("猫眼评分") == False or movie["猫眼评分"] == None):
            movie["猫眼评分"] = "暂无评"
    
    return movies

def getMaoyanData(maoyan, movie):
    '''
    @功能：解析字符串
    @入参：
        @param maoyan: response对象
        @param movie: dict 存储字典
    @出参：
        @param movie: dict 存储字典
    '''
    i = 0;
    for data in maoyan.text.split('<div class="channel-detail movie-item-title"'):
        if(i == 0): 
            i = i + 1
            continue
        #判断数据是否正确
        title = re.search('title="(.*?)">', data).group(1)
        rating1 = re.search('<i class="integer">(.*?)</i>', data)
        rating2 = re.search('<i class="fraction">(.*?)</i>', data)
        if(movie["电影名"] == title):
            if(rating1 != None):
                movie["猫眼评分"] = rating1.group(1)
            if(rating2 != None):
                movie["猫眼评分"] += rating2.group(1)
        
        return movie
