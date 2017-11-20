# -*- coding: utf-8 -*-
# 使用BeautifulSoup解析网页
import codecs
import re
#获取要解析的标签
import os
import urllib
import time
import datetime
import random


def getHtml(url):
    html = urllib.urlopen(url)
    print "The access state is: ", html.getcode()
    if html.getcode() == 403:
        time.sleep(1800)
    theTime = datetime.datetime.now()  
    print theTime
    html = html.read()
    return html
# html = getHtml(url)
# saveHtml(param, html)# 保存种子网页

def saveHtml(dir_name,file_name, file_content):
    #    注意windows文件命名的禁用符，比如 /
    with open("./"+dir_name+"/"+file_name+".html", "w") as f:
        #   写文件用bytes而不是str，所以要转码
        f.write(file_content)


def saveXml(dir_name, file_name, file_content):
    with open("./"+dir_name+"/"+file_name+".xml","wb") as f:
        f.write(file_content)


num = 36612
count =num
for i in range(4):
    with codecs.open(str(i)+'.txt','r','utf-8') as wb_data:
        for tag in wb_data:
            if num>0:
                num-=1
            else:
                try:
                    print "we are accessing", tag
                    param = re.findall(r"\d",tag)
                    param = ''.join(param)
                    s = random.gauss(4,1)
                    time.sleep(abs(s))
                    html = getHtml(tag)
                    print tag
                    saveHtml(str(i),param, html)# 保存种子网页
                    count+=1
                    print "We have download :",count,"pages"
                except:
                    print "There might be some problems"
