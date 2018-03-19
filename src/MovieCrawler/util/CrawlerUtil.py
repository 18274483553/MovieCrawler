#coding=utf-8
'''
@文件名：WormUtil.py
@创建时间：2018-03-06 15:32:29
@作者：疾风
@功能：爬虫工具类
@版本修订：无
'''
from bs4 import BeautifulSoup
import urllib2
import time

def getSoup(url, choose = False):
    '''
    @功能：向目标网页发起请求并解析，返回网页的BeautifulSoup对象
    @入参：
        @param url: string 网页地址
        @param choose: Boolean 是否打印网页源代码
    @出参：
        @param soup: bs4.BeautifulSoup 网页soup对象
    '''
    soup = None
    interr = True
    while(interr):
        try:
            #模拟浏览器创建HTML请求
            request = urllib2.Request(url)
            result = urllib2.urlopen(request)
            #根据请求输出网页源代码
            if(choose == True):
                print result.read()
            #解析网页soup对象
            soup = BeautifulSoup(result.read())
            #跳出循环
            interr = False
        except urllib2.URLError, e:
            print("处理中  网络连接错误，正在重新发起请求...")
            time.sleep(1)
    
    return soup
