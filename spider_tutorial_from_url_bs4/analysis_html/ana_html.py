# -*- coding: utf-8 -*-
# 使用BeautifulSoup解析网页
from bs4 import BeautifulSoup
import codecs
import re
#获取要解析的标签
import os

with codecs.open('test.html','r','utf-8') as wb_data:
    name = os.path.basename('test.html')
    print name
    Soup = BeautifulSoup(wb_data);    #将要解析的文件传入
    # print(Soup);    #打印读入Soup中的内容
    print("!--------------\n")
    tags = Soup.find_all("a","a-tag")# 读取tag 过滤掉没有机场和东京的问题
    flags=[]
    for tag in tags:
        flags.append(tag.get_text())
        # print tag.get_text()
    if u'机场' in flags or u'东京' in flags:
        question = Soup.title
        question = re.sub(u' - 蚂蜂窝','',question.get_text())
        # print 
        answer = Soup.find("div","_j_answer_html")
        # print answer.get_text()
        ding = Soup.find('a',r'btn-ding _js_zan ')
        print question+'|'+answer.get_text()+'|'+ding.get_text()

    # print question+'|'+answer+'|'+ding


    # shot_name = Soup.select('body > div > div > table > tbody > tr > td > a');     #将要解析的标签元素路径传入
    # #shot_name = Soup.select('body > div > div > div > ol > li > a');     #将要解析的标签元素路径传入
    #     #可以从网站上直接复制
    # print(shot_name,sep='\n!!---------------\n');      #打印解析标签元素包含内容
# wb_data.close();

# #解析标签内容-------使用get_text()获得文本内容,使用get('')方法获取标签属性值
# list = [];
# for shot in shot_name:
#     data = shot.get('href').strip('\/');
#     list.append(data);

# with open('shot_names.txt', 'w+') as f:
#     for i in list:
#         f.writelines(i + '\n')