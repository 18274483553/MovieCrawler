#coding=utf-8
'''
@文件名：MoviePrinter.py
@创建时间：2018-03-09 15:34:23
@作者：疾风
@功能：输出电影信息到文件
'''
import os
import time

#文件输出目录
ROOT_DIR = unicode(os.getcwd() + os.path.sep + "result" + os.path.sep, "utf-8")

def printMovieToFile(movies):
    '''
    @功能：将电影信息格式化输出到文件
    @入参：
        @param movies: list 存储数据对象
    @出参：
        @param movies: list 存储数据对象
    '''
    #格式化获取系统时间
    titime = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))
    cotime = time.strftime('%Y年%m月%d日%H点',time.localtime(time.time()))
    
    text = "\n" + cotime + " 院线热映电影详细信息 爬取结果：\n"
    for movie in movies:
        text += "\n"
        text += "name：" + movie["电影名"] + "\n"
        text += "length：" + movie["电影时长"] + "分钟" + "\n"
        text += "type：" + movie["电影类型"] + "\n"
        text += "day：" + movie["上映天数"] + "天" + "\n"
        text += "allboxoffice：" + movie["累计票房"] + "元" + "\n"
        text += "boxoffice：" + movie["实时票房"] + "元" + "\n"
        text += "boxofficerate：" + movie["票房占比"] + "%" + "\n"
        text += "rowpiecerate：" + movie["排片占比"] + "%" + "\n"
        text += "seatoccupancyrate：" + movie["上座率"] + "%" + "\n"
        text += "seatrate：" + movie["排座占比"] + "%" + "\n"
        text += "session：" + movie["场次"] + "场" + "\n"
        text += "allpeople：" + movie["人次"] + "人" + "\n"
        text += "people：" + movie["场均人次"] + "人" + "\n"
        text += "income：" + movie["场均收入"] + "元" + "\n"
        text += "price：" + movie["平均票价"] + "元" + "\n"
        text += "douban：" + movie["豆瓣评分"] + "分" + "\n"
        text += "mtime：" + movie["时光网评分"] + "分" + "\n"
        text += "maoyan：" + movie["猫眼评分"] + "分" + "\n"
    
    if(os.path.exists(ROOT_DIR) == False):
        print("处理中  创建目录 " + ROOT_DIR)
        os.mkdir(ROOT_DIR)
    addfile = ROOT_DIR + unicode("电影信息_" +  titime + ".txt", "utf-8")
    file = open(addfile, "wb")
    file.write(text)
    print("爬取完毕  写入文件 " + addfile)
    file.close()
    
    FileClear(10)
    
def FileClear(filenum):
    '''
    @功能：清理多余的历史文件
    @入参：
        @param filenum: int 文件数量
    @出参：无
    '''
    morefile = True
    while(morefile):
        files = os.listdir(ROOT_DIR)
        if(len(files) > filenum):
            # 按默认排序
            files.sort()
            filedir = os.path.join(ROOT_DIR, files[0])
            # 判断文件格式
            if(os.path.isfile(filedir) and os.path.splitext(filedir)[1] == ".txt"):
                print("处理中  清理历史文件：" + filedir)
                # 删除文件
                os.remove(filedir)
        else:
            morefile = False
            print("清理完毕  等待下一次处理")
                
