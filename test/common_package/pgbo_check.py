#!/usr/bin/python
# -*- coding:UTF-8 -*-
"""
验证首页底部链接及热线电话的正确性
"""
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import data.usedata
from lib.readtxt import readtxt
from test.common_package.basic import Page

class PageBottomCheck(Page):
    #url = '/'
    #link_text = readtxt()
    botto_loc = (By.CLASS_NAME,"footer")

    #定位首页城市
    def city_dingwei(self):
        self.city_loc = (By.CLASS_NAME, 'exchange')
        city_name = self.find_element(*self.city_loc).text
        #print(city_name)
        return city_name

    #读取页面底部第一行链接名称
    def readfile(self):
        city_name = self.city_dingwei()
        if city_name == '北京':
            link_text = readtxt('bjlinkname')
        elif city_name == '福州':
            link_text = readtxt('fzlinkname')
        else:
            link_text = readtxt('xmlinkname')
        #print(link_text)
        return link_text

    #读取页面底部热门链接名称
    def readfile_three(self):
        city_name = self.city_dingwei()
        if city_name == '北京':
            link_text_three = readtxt('bjlinkname_three')
        elif city_name == '福州':
            link_text_three = readtxt('fzlinkname_three')
        else:
            link_text_three = readtxt('xmlinkname_three')
        #print(link_text_three)
        return link_text_three

    #检查配置文件G:\MT_online_auto\config\linkname 文件中链接名称点击后跳转的是否正确
    def link_check(self):
        self.script(self.find_element(*self.botto_loc)) #定位到页面底部
        self.link_text = self.readfile()
        for linkname in self.link_text:
            self.linktext_loc = (By.LINK_TEXT,linkname)
            self.shoupage_handle = self.driver.current_window_handle
            self.find_element(*self.linktext_loc).click()
            self.all_handle = self.driver.window_handles
            #print(linkname)
            for self.handle in self.all_handle:
                if self.handle !=self.shoupage_handle:
                    self.driver.switch_to.window(self.handle)
                    try:
                        assert 'test.imtfc.com' in self.driver.current_url   #使用域名判断连接是否正确
                    except AssertionError as e:
                        print(linkname +" 所在页面不包含在 %s" % self.driver.current_url)
                    #print(self.driver.current_url)
                    self.driver.close()
                    sleep(1)
                    self.driver.switch_to.window(self.shoupage_handle) #返回首页

    #检查页面底部三个热门链接
    def linkcheck_hot_three(self):
        self.script(self.find_element(*self.botto_loc))  # 定位到页面底部
        sleep(2)
        self.xunating_list = ["//ul[@class='hot-list-title clearFix']/li[1]",
                              "//ul[@class='hot-list-title clearFix']/li[2]",
                              "//ul[@class='hot-list-title clearFix']/li[3]"]
        self.shoupage_handle = self.driver.current_window_handle
        t = 0
        #页面底部三个热门标签依次悬停
        for xuanting_num in self.xunating_list:
            self.xuanting = self.find_element(*(By.XPATH,xuanting_num))
            ActionChains(self.driver).move_to_element(self.xuanting).perform()

            link_text_three = self.readfile_three()
            index_list = [index for index, link in enumerate(link_text_three) if link == '']
            #print(index_list)
            remenlink_three_son = [linknametext for linknametext in link_text_three]
            # print(remenlink_three_son)
            #拆分读取三个热门标签的字标签
            for i in range(len(index_list) + 1):
                #print(i)
                if i == 0:
                    remenlink_three_son[i] = [linknametext for linknametext in remenlink_three_son[:index_list[i]]]
                    #print(remenlink_three_son[i])
                if i == 1:
                    remenlink_three_son[i] = [linknametext for linknametext in remenlink_three_son[index_list[i - 1]
                                                                                               + 1:index_list[i]]]
                    #print(remenlink_three_son[i])
                if i == 2:
                    remenlink_three_son[i] = [linknametext for linknametext in remenlink_three_son[index_list[i - 1] + 1:]]
                    #print(remenlink_three_son[i])
            #分别点击三个热门标签的字标签链接并判断
            for linkname in remenlink_three_son[t]:
                self.find_element(*(By.LINK_TEXT,linkname)).click()
                self.all_handle = self.driver.window_handles
                for self.handle in self.all_handle:
                    if self.handle != self.shoupage_handle:
                        self.driver.switch_to.window(self.handle)
                        try:
                            assert 'test.imtfc.com' in self.driver.current_url  # 使用域名判断连接是否正确
                        except AssertionError as e:
                            print(linkname + " 所在页面不包含在 %s" % self.driver.current_url)
                        #print(self.driver.current_url)
                        self.driver.close()
                        sleep(1)
                        self.driver.switch_to.window(self.shoupage_handle)  # 返回首页
            t += 1

    #检查热线电话的正确性
    def goufangrexian_chenk(self):
        #self.city_loc = (By.CLASS_NAME, 'exchange')
        city_name = self.city_dingwei()
        city_tel = [value for key,value in data.usedata.tel.items() if key ==city_name]
        for tel in city_tel:
            city_hotline_tel = tel
        #print(city_hotline_tel)
        self.script(self.find_element(*self.botto_loc)) #定位到页面底部
        hotline_loc = (By.CLASS_NAME,'hotline')
        hotline_text = self.find_element(*hotline_loc).text
        #print(hotline_text)
        try:
            assert city_hotline_tel in hotline_text #判断热线电话号码是否是该城市的号码
            print(hotline_text + '是 ' + city_name + ' 的热线电话')
        except AssertionError as e:
            print(hotline_text + '不是' + city_name +'热线电话')
        return city_name

#    def three_remen_check(self):
#        city_name = self.goufangrexian_chenk()

    #调用页面底部链接及热线电话的三个方法
    def tongyidiaoyong(self):
        self.link_check()
        self.linkcheck_hot_three()
        self.goufangrexian_chenk()


if __name__=="__main__":
    from selenium import webdriver
    import data.urldata as URL
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get(URL.maitian_online_url)
    #driver.get('http://fz-test.imtfc.com/VIEW/Index/Index2.html')
    #driver.get('http://xm-test.imtfc.com/VIEW/Index/Index2.html')
    PageBottomCheck(selenium_driver=driver).tongyidiaoyong()
    driver.close()