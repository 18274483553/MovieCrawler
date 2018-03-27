#coding=utf-8
'''
@文件名：MtimeCollecter.py
@创建时间：2018-03-09 15:28:38
@作者：疾风
@功能：从时光网爬取正在热映电影的信息
'''
import re
import requests

def getMtimeScore(movies):
    '''
    @功能：获取时光网评分等
    @入参：
        @param movies: list 存储数据对象
    @出参：
        @param movies: list 存储数据对象
    '''
    url = "http://service.channel.mtime.com/Search.api"
    #将豆瓣评分导入集合
    for movie in movies:
        print("\t处理中  正在抓取时光网内容：" + movie["电影名"])
        querystring = {
            "Ajax_CallBack":"true",
            "Ajax_CallBackType":"",
            "Ajax_CallBackMethod":"GetSearchResult",
            "t":"0",
            "Ajax_CallBackArgument0":movie["电影名"],
            "Ajax_CallBackArgument4":"1"
        }
        mtime = requests.request("GET", url, params=querystring)
        #解析字典对象
        movie = getMtimeData(mtime, movie)
        if(movie.has_key("时光网评分") == False or movie["时光网评分"] == None):
            movie["时光网评分"] = "暂无评"
        if(movie.has_key("电影时长") == False or movie["电影时长"] == None):
            movie["电影时长"] = "未知"
        if(movie.has_key("电影类型") == False or movie["电影类型"] == None):
            movie["电影类型"] = "未知"
    
    return movies

def getMtimeData(mtime, movie):
    '''
    @功能：解析字符串
    @入参：
        @param mtime: response对象
        @param movie: dict 存储字典
    @出参：
        @param movie: dict 存储字典
    '''
    for data in mtime.text.split('},{"movieId"'):
        #判断数据是否正确
        title = re.search('"movieTitle":"(.*?)\s+', data).group(1)
        rating = re.search('"movieRating":"(.*?)"', data)
        length = re.search('"movieLength":(.*?),', data)
        type = re.search('"genreTypes":"(.*?)"', data)
        if(movie["电影名"] == title):
            if(rating != None):
                movie["时光网评分"] = rating.group(1)
            if(length != None):
                movie["电影时长"] = length.group(1)
            if(type != None):
                movie["电影类型"] = type.group(1)
        
        return movie
