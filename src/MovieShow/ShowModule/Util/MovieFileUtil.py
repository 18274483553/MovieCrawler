# -*- coding: utf-8 -*-
'''
@文件名：MovieFileUtil.py
@创建时间：2018-03-16 21:20
@作者：疾风
@功能：处理电影数据文件及内容
@版本修订：无
'''
import os
import re

def readMovieFile(param=None, isnum=False):
    '''
    @功能说明：读取电影数据文件
    @入参：
        @param param: str 要读取的字段名
        @param excepts: str 要过滤的单位
    @出参：
        @param movies: 读取的数据
    '''
    root = unicode(os.getcwd() + os.path.sep + "result" + os.path.sep, "utf-8")
    filenames = os.listdir(root)
    if(len(filenames) != 0):
        filenames.sort()
        filedir = os.path.join(root, filenames[len(filenames) - 1])
        # 逐行读取文件，系统可以自动关闭流
        with open(filedir, 'rb') as file:
            # 如果没有传参，则默认读取文件所有内容
            if(param == None):
                movies = []
                movie = {}
                for line in file:
                    if("电影名：" in line):
                        if(movie != {}):
                            movies.append(movie)
                        movie = {}
                    if("：" in line and line.endswith("：") != True):
                        movie[re.search('^(.*?)：.*$', line).group(1)] = re.search('^.*?：(.*)$', line).group(1)
                
                return movies
            # 如果传了参数，则只读取参数所指定的内容
            else:
                movies = '{"key":['
                key = ''
                value = ''
                for line in file:
                    if("电影名：" in line):
                        key += '"' + re.search('^.*?：(.*)$', line).group(1) + '",'
                    elif(param in line and isnum == 'True'):
                        if("亿" in line):
                            value += str(float(re.search('^.*?：(\d+\.?\d*).*$', line).group(1)) * 10000) + ','
                        elif(re.search('^.*?：(\d+\.?\d*).*$', line) == None):
                            value += '0' + ','
                        else:
                            value += re.search('^.*?：(\d+\.?\d*).*$', line).group(1) + ','
                    elif(param in line):
                        value += '"' + re.search('^.*?：(.*?)$', line).group(1) + '",'
                        
                movies += key + '],"value":[' + value + ']}'
                
                return movies
        
        file.close()
    else:
        return None
    