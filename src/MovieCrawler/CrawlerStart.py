#coding=utf-8
'''
@文件名：CrawlerStart.py
@创建时间：2018-03-06 17:32:42
@作者：疾风
@功能：从各个网站爬取正在热映电影的信息
@版本修订：
    @version: v1.1.0.20180306_Alpha
        1. 新增实时票房获取站点-实时电影票房
        2. 新增豆瓣评分获取
        3. 新增时光网评分获取
    @version: v1.1.1.20180309_Alpha
        1. 项目文件重构
        2. 修改实时电影票房获取源，源网站更改为百度糯米
        3. 修改票房部分输出字段
        4. 解决百度糯米偶尔返回数据为空的BUG
        5. 修改结果文件输出目录，由固定目录更改为程序当前工作目录
        6. 新增流程输出，实时汇报爬取进度
    @version: v1.1.2.20180312_Alpha
        1. 修改豆瓣评分获取方式，通过精确搜索
        2. 修改时光网评分获取方式，通过精确搜索
        3. 新增从时光网获取电影时长和电影类型
        4. 优化输出文本
'''
import sys
import time
import threading

from MovieCrawler.telecommunication import PiaofangCollecter
from MovieCrawler.telecommunication import DoubanCollecter
from MovieCrawler.telecommunication import MtimeCollecter
from MovieCrawler.output import MoviePrinter

def CrawlerStart():
    '''
    @功能：启动爬虫线程
    '''
    #设置编码格式
    reload(sys)
    sys.setdefaultencoding('utf-8')
    MyThread(1).start()

class MyThread(threading.Thread):
    '''
    @功能：爬虫线程重写
    '''
    def __init__(self,arg):
        super(MyThread, self).__init__()    # 注意：一定要显式的调用父类的初始化函数。
        self.arg=arg
        
    def run(self):
        
        print("欢迎使用  热映电影全网爬虫工具")
        while(True):
            
            cotime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            print("开始爬取  " + cotime)
            print("处理中  向百度糯米发送请求...")
            movies = PiaofangCollecter.getPiaofangRecords()
            print("处理中  向豆瓣电影发送请求...")
            movies = DoubanCollecter.getDoubanScore(movies)
            print("处理中  向时光网发送请求...")
            movies = MtimeCollecter.getMtimeScore(movies)
            print("处理中  正在写入文件...")
            MoviePrinter.printMovieToFile(movies)
    
            time.sleep(3600)
