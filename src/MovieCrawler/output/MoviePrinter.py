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
        text += "电影名：" + movie["电影名"] + "\n"
        text += "电影时长：" + movie["电影时长"] + "分钟" + "\n"
        text += "电影类型：" + movie["电影类型"] + "\n"
        text += "上映天数：" + movie["上映天数"] + "天" + "\n"
        text += "累计票房：" + movie["累计票房"] + "元（人民币）" + "\n"
        text += "实时票房：" + movie["实时票房"] + "元（人民币）" + "\n"
        text += "票房占比：" + movie["票房占比"] + "%" + "\n"
        text += "排片占比：" + movie["排片占比"] + "%" + "\n"
        text += "上座率：" + movie["上座率"] + "%" + "\n"
        text += "排座占比：" + movie["排座占比"] + "%" + "\n"
        text += "场次：" + movie["场次"] + "场" + "\n"
        text += "人次：" + movie["人次"] + "人" + "\n"
        text += "场均人次：" + movie["场均人次"] + "人" + "\n"
        text += "场均收入：" + movie["场均收入"] + "元（人民币）" + "\n"
        text += "平均票价：" + movie["平均票价"] + "元（人民币）" + "\n"
        text += "豆瓣评分：" + movie["豆瓣评分"] + "分" + "\n"
        text += "时光网评分：" + movie["时光网评分"] + "分" + "\n"
    
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
                
