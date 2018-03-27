#coding=utf-8
'''
@文件名：DoubanCollecter.py
@创建时间：2018-03-09 15:25:42
@作者：疾风
@功能：从豆瓣电影爬取正在热映电影的信息
'''
import re
import requests
from MovieCrawler.util import CrawlerUtil

def getDoubanScore(movies):
    '''
    @功能：获取豆瓣评分
    @入参：
        @param movies: list 存储数据对象
    @出参：
        @param movies: list 存储数据对象
    '''
    url = "https://movie.douban.com/j/subject_suggest"
    
    #将豆瓣评分导入集合
    for movie in movies:
        print("\t处理中  正在抓取豆瓣内容：" + movie["电影名"])
        querystring = {"q": movie["电影名"]}
        douban = requests.request("GET", url, params=querystring)
        #解析字典对象
        movie = getDoubanData(douban, movie)
        if(movie.has_key("豆瓣评分") == False or movie["豆瓣评分"] == None):
            movie["豆瓣评分"] = "暂无评"
    
    return movies

def getDoubanData(douban, movie):
    '''
    @功能：解析URL并获取详情页的评分
    @入参：
        @param douban: response对象
        @param movie: dict 存储字典
    @出参：
        @param movie: dict 存储字典
    '''
    for data in douban.text.split("},{"):
        try:
            if(data != "[]" and movie["电影名"] == re.search('"title":"(.*?)"', data).group(1)):
                #解析URL
                url = re.search('"url":"(.*?)\?suggest', data).group(1).replace("\\", "")
                #获取soup对象
                soup = CrawlerUtil.getSoup(url)
                #获取评分所在的标签
                strong = soup.find("strong", class_="ll rating_num")
                #记录评分
                movie["豆瓣评分"] = strong.string
        except AttributeError:
            movie["豆瓣评分"] = "暂无评"
            
        return movie
