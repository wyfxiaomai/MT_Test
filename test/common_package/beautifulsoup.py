#!/usr/bin/python
from urllib import request
from bs4 import BeautifulSoup
import re
from test.common_package.basic import Page
from selenium import webdriver
from time import sleep
import json
class GetBiaoId(object):
    def get_id(self,url):
        html = request.urlopen(url) #打开网页
        soup = BeautifulSoup(html.read(), "html.parser")
        sleep(1)
        print(soup)
        #str_lianjie = str(soup)
        #print(str_lianjie)
        html_json = driver.page_source  #获取页面返回的内容
        re_html = "var [\w]* = \$.parseJSON\('\[(\{.*\})"   #匹配json的正则表达式
        all = re.compile(re_html)       #编译正则表达式
        re_all = re.findall(all, html_json) #从HTML中找到每个出现匹配的部分
        re_all_str = ''.join(re_all)    #转换为字符串
        print(re_all_str)
        if 'way' in url:
            re_id = r'"StationNO":"([\w]*)"'#北京二手房、租房、小区---地铁房
        else:
            re_id = r'"CycleNO":"([\w]*)"'  # 北京|福州|厦门----二手房、租房、小区、房产顾问---全部二手房
        all = re.compile(re_id)       #编译正则表达式
        re_json_all = re.findall(all,re_all_str) #找到每个出现匹配的部分
        print(re_json_all)
        print(len(re_json_all))


if __name__=="__main__":
    from selenium import webdriver
    driver = webdriver.PhantomJS()
    driver.implicitly_wait(3)
    driver.maximize_window()
    url = 'http://xm-test.imtfc.com/esfall/R1'
    driver.get(url)
    GetBiaoId().get_id(url=url)
    driver.close()