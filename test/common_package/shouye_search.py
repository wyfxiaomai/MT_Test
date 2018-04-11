#!/usr/bin/python
#-*- coding:UTF-8 -*-

"""
验证首页搜索框及联想词、点击联想词的正确性
"""

from selenium.webdriver.common.by import By
from test.common_package.basic import Page
from lib.readtxt import readtxt
from time import sleep
import requests

class ShouYeSearch(Page):
    url = '/'
    thinkwordid = 'SearchTips'
    search_kuang_id = 'ico-search'
    search_hou_text_id = 'SearchHouseTerm'

    #点击联想词
    def thingkword_click(self,thinkword_list,stext,sname):
        self.script(self.find_element(*(By.ID, self.thinkwordid)))
        for link in thinkword_list:
            self.find_element(*(By.PARTIAL_LINK_TEXT, link)).click()
            link_hou_text = self.find_element(*(By.ID, self.search_hou_text_id)).text
            #print(link_hou_text)
            linkhoutext = [name for name in link_hou_text.split('\n')]
            del linkhoutext[1:]
            #print(linkhoutext)
            try:
                for linkhoutext_del in linkhoutext:
                    assert linkhoutext_del in link
                    print("%s 包含在 %s" % (linkhoutext_del, link))
            except Exception as e:
                print("%s 不包含在 %s" % (linkhoutext_del, link))
            self.driver.back()
            self.find_element(*(By.ID,sname)).click()
            sleep(2)
            self.find_element(*(By.ID, self.search_kuang_id)).send_keys(stext)
            sleep(2)
    #判断联想词
    def xunhuan(self,stext,thinkword_list,snameindex):
        for word in thinkword_list:
            if snameindex == 3:
                try:
                    assert ' 1' in word
                    print("%s 联想词正确！！！" % word)
                except Exception as e:
                    print("%s 联想词有误！！！" % word)
            else:
                try:
                    assert stext in word
                    print("%s 联想词正确！！！" % word)
                except Exception as e:
                    print("%s 联想词有误！！！" % word)

    #搜索联想词判断及点击搜索后的正确性
    def search(self,city_name,searchtext,sname,snameindex):
        search_anniu_id = 'btSearch'    #搜索按钮ID'
        self.find_element(*(By.ID, sname)).click()
        sleep(1)
        for stext in searchtext:
            self.find_element(*(By.ID, self.search_kuang_id)).clear()
            self.find_element(*(By.ID, self.search_kuang_id)).send_keys(stext)
            #print(stext)
            sleep(2)
            thinkword = self.find_element(*(By.ID, self.thinkwordid)).text
            #print(thinkword)
            thinkword_linkname = ['待售','待租',' ']
            if thinkword is None:
                    print('%s 没有联想词！！！'% stext)
            if snameindex == 0:
                thinkword_list = [think for think in thinkword.split('\n')  if thinkword_linkname[0] not in think]
                self.xunhuan(stext=stext, thinkword_list=thinkword_list, snameindex=snameindex)
                self.thingkword_click(thinkword_list, stext,sname)
                #print(thinkword_list)
            elif snameindex == 1:
                if city_name == '北京':
                    thinkword_list = [think for think in thinkword.split('\n') if thinkword_linkname[1] not in think]
                    self.xunhuan(stext=stext, thinkword_list=thinkword_list,snameindex=snameindex)
                    self.thingkword_click(thinkword_list, stext,sname)
                    #print(thinkword_list)
                else:
                    thinkword_list = [think for think in thinkword.split('\n') if thinkword_linkname[0] not in think]
                    self.xunhuan(stext=stext, thinkword_list=thinkword_list, snameindex=snameindex)
                    self.thingkword_click(thinkword_list, stext,sname)
                    #print(thinkword_list)
            elif snameindex == 2:
                if city_name == '北京':
                    thinkword_list = [think for think in thinkword.split('\n') if '待售' and '待租' not in think]
                    self.xunhuan(stext=stext, thinkword_list=thinkword_list, snameindex=snameindex)
                    self.thingkword_click(thinkword_list, stext,sname)
                    #print(thinkword_list)
                else:
                    thinkword_list = [think for think in thinkword.split('\n') if thinkword_linkname[0] not in think]
                    self.xunhuan(stext=stext, thinkword_list=thinkword_list, snameindex=snameindex)
                    self.thingkword_click(thinkword_list, stext,sname)
                    #print(thinkword_list)
            else:
                thinkword_list_zhaoguwen = [think for think in thinkword.split('\n') if thinkword_linkname[2] in think]
                #print(thinkword_list_zhaoguwen)
                self.xunhuan(stext=stext, thinkword_list=thinkword_list_zhaoguwen,snameindex=snameindex)
                self.thingkword_click(thinkword_list_zhaoguwen, stext,sname)
            self.find_element(*(By.ID, search_anniu_id)).click()
            sleep(1)
            self.sh_text = self.find_element(*(By.ID, self.search_hou_text_id)).text
            try:
                assert stext == self.sh_text
                print('搜索内容正确！！！')
            except Exception as e:
                print('搜索内容不正确！！！')
            self.driver.back()
            self.find_element(*(By.ID,sname)).click()

    # 定位首页城市并读取文件内容
    def shouye_city_dingwei(self):
        bj_searchnameid = ['zesf', 'zzf', 'zxq', 'zgw']
        fx_searchnameid = ['zesf', 'zbs', 'zxq', 'zgw']
        self.city_loc = (By.CLASS_NAME, 'exchange')
        city_name = self.find_element(*self.city_loc).text
        # print(city_name)
        searchtext = readtxt('shouye_searchtext')
        #print(searchtext)
        searchtext_id = [index for index,name in enumerate(searchtext) if name=='北京'or name=='福州'or name=='厦门']
        #print(searchtext_id)
        if city_name == '北京':
            searchtext = searchtext[1:searchtext_id[1]]
            #print(searchtext)
        elif city_name == '福州':
            searchtext = searchtext[searchtext_id[1]+1:searchtext_id[2]]
            #print(searchtext)
        else:
            searchtext = searchtext[searchtext_id[2]+1:]
            #print(searchtext)
        if city_name == '北京':
            for sname in bj_searchnameid:
                self.search(city_name=city_name,searchtext=searchtext,sname=sname,snameindex=bj_searchnameid.index(sname))
        else:
            for sname in fx_searchnameid:
                self.search(city_name=city_name,searchtext=searchtext, sname=sname,snameindex=fx_searchnameid.index(sname))

    #供外部调用
    def tongyidiaoyong(self):
        #self.open()  # 打开网站
        #sleep(2)
        self.shouye_city_dingwei()



if __name__=="__main__":
    from selenium import webdriver
    import data.urldata as URL
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    #driver.get(URL.maitian_online_url)
    driver.get('http://fz-test.imtfc.com/VIEW/Index/Index2.html')
    #driver.get('http://xm-test.imtfc.com/VIEW/Index/Index2.html')
    ShouYeSearch(selenium_driver=driver).tongyidiaoyong()
    driver.close()