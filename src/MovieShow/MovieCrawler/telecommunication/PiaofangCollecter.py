#coding=utf-8
'''
@文件名：PiaofangCollecter.py
@创建时间：2018-03-09 15:24:59
@作者：疾风
@功能：从百度糯米爬取正在热映电影的票房信息
'''
import time
import json
import requests

def getPiaofangRecords():
    '''
    @功能：解析百度糯米电影票房信息
    @入参：无
    @出参：
        @param movies: list 电影信息列表
    '''
    #构建Post请求参数
    url = "http://dianying.nuomi.com/movie/boxrefresh"
    headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER",
    }
    #解析Post请求
    piaofang = requests.request("POST", url, headers=headers)
    jsons = json.loads(piaofang.text)
    while(jsons["real"]["data"]["detail"] == []):
        print("处理中  百度糯米数据异常，正在尝试重新获取...")
        time.sleep(1)
        piaofang = requests.request("POST", url, headers=headers)
        jsons = json.loads(piaofang.text)
        piaofang.keep_alive = False
    #解析json票房数据
    movies = []
    movies = getPiaofangJson(jsons, movies)
    
    return movies

def getPiaofangJson(jsons, movies):
    '''
    @功能：解析百度糯米电影信息json数据
    @入参：
    @param jsons: json json对象
        @param movies: list 存储数据对象
    @出参：
        @param movies: list 存储数据对象
    '''
    for json in jsons["real"]["data"]["detail"]:
        movie = {}
        movie["电影名"] = json["movieName"]
        for i in range(1, 13):
            movie[str(json["attribute"][str(i)]["attrName"])] = str(json["attribute"][str(i)]["attrValue"])
        movies.append(movie)
    
    return movies
