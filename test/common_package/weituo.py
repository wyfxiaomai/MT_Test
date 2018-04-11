#!/usr/bin/python
# -*- coding:UTF-8 -*-
"""
WeiTuo()中tongyidiaoyong()可以供北京、福州、厦门调用，调用时传入cityname=0/1/2 即可。可从文件中读取数据，也可以以传参数的
形式传入要输入的值xiaoqu_name='',jushi='',mianji='',qiwangshoujia='',lianxifangshi=''。
需要测试委托输入不同错误内容时，得出不同的提示语情况时，可单独调用send_text()方法编写测试用例（传入需要输入的不同内容）
例如：
WeiTuo(driver).send_text(xiaoqu_name='123',jushi=123,mianji=456,qiwangshoujia=789,lianxifangshi=15000000000)
"""
from time import sleep
from selenium.webdriver.common.by import By
from test.common_package.basic import Page
from test.common_package.selectcity import SelectCity
from lib.readtxt import readtxt
from test.common_package.sousuokuang import SouSuoKuang

class WeiTuo(Page):
    #读取文件内容
    def readtext(self,filename=''):
        neirong = readtxt(filename)
        cityname = SouSuoKuang(self.driver).get_cityname(cityClass='show')
        #print(cityname,neirong)
        for city in neirong:  # 从获取的文件内容中判断当前所在城市，并取出该城市下的所有内容
            if city == cityname:
                city_index = neirong.index(city)
        for city_son in neirong[city_index + 1:]:  # 截取城市中的内容
            if city_son == '北京' or city_son == '福州' or city_son == '厦门':
                city_index_son = neirong.index(city_son)  # 当读取另一个城市的名称时，记录该名称所在位置并结束循环
                break
            else:
                city_index_son = -1  # 如果没有读取到其他城市名称，则标志赋值为-1，说明该城市在文件中为最后一个城市
        if city_index_son == -1:  # 如果标志位-1，读取城市名称后面一个位置的内容，直到最后
            neirong = neirong[city_index + 1:]
        else:
            neirong = neirong[city_index + 1:city_index_son]  # 如果标志位不为-1，读取读取城市名称后面一个位置的内容，直到下一个城市位置的前一个内容
        #print(neirong)
        return neirong

    # 读取内容所对应的文本框
    def read_sendtext(self,filename='',xiaoqu_name='',jushi='',mianji='',qiwangshoujia='',lianxifangshi=''):
        if filename == '':
            xiaoqu_name = xiaoqu_name
            jushi = jushi
            mianji = mianji
            qiwangshoujia = qiwangshoujia
            lianxifangshi = lianxifangshi
        else:
            sendtext = self.readtext(filename=filename)
            for st in sendtext:
                if '小区名称:' in st:
                    xiaoqu_name = st[st.index(':')+1:]
                elif '居室:' in st:
                    jushi = st[st.index(':')+1:]
                elif '面积:' in st:
                    mianji = st[st.index(':')+1:]
                elif '期望售价:' in st:
                    qiwangshoujia = st[st.index(':')+1:]
                elif '联系方式:' in st:
                    lianxifangshi = st[st.index(':')+1:]
                else:
                    if '小区名称:' not in st:
                        xiaoqu_name = ''
                    elif '居室:' not in st:
                        jushi = ''
                    elif '面积:' not in st:
                        mianji = ''
                    elif '期望售价:' not in st:
                        qiwangshoujia = ''
                    elif '联系方式:' not in st:
                        lianxifangshi = ''
        return xiaoqu_name,jushi,mianji,qiwangshoujia,lianxifangshi

    #输入读取的内容
    def send_text(self,filename='',xiaoqu_name='',jushi='',mianji='',qiwangshoujia='',lianxifangshi='',nameID='garden',jushiID='house',mianjiID='area',shoujiaID='price',shoujiID='Phone'):
        sendtext = self.read_sendtext(filename=filename,xiaoqu_name=xiaoqu_name,jushi=jushi,mianji=mianji,qiwangshoujia=qiwangshoujia,lianxifangshi=lianxifangshi)
        #print(sendtext)
        self.find_element(*(By.ID,nameID)).clear()
        self.find_element(*(By.ID, nameID)).send_keys(sendtext[0])
        self.find_element(*(By.ID, jushiID)).clear()
        self.find_element(*(By.ID, jushiID)).send_keys(sendtext[1])
        self.find_element(*(By.ID, mianjiID)).clear()
        self.find_element(*(By.ID, mianjiID)).send_keys(sendtext[2])
        self.find_element(*(By.ID, shoujiaID)).clear()
        self.find_element(*(By.ID, shoujiaID)).send_keys(sendtext[3])
        self.find_element(*(By.ID, shoujiID)).clear()
        self.find_element(*(By.ID, shoujiID)).send_keys(sendtext[4])

    #点击提交按钮
    def tijiao_click(self,tijiaoID='btnSubmit'):
        self.find_element(*(By.ID,tijiaoID)).click()

    #接收警告
    def jieshou_warning(self):
        self.driver.switch_to_alert().accept()

    #获取警告提示内容
    def get_warning_text(self):
        return self.driver.switch_to_alert().text

    # 统一调用
    def tongyidiaoyong(self,filename='',xiaoqu_name='',jushi='',mianji='',qiwangshoujia='',lianxifangshi='',cityname=0):
        SelectCity(self.driver).dakaiwangzhan()  # 打开网站
        sleep(2)
        SelectCity(self.driver).maitian_online_city_select(cityname=cityname)  # 选择城市
        sleep(3)
        self.shouye_handle = self.driver.current_window_handle
        SelectCity(self.driver).weituo()  # 点击委托
        sleep(3)
        self.all_handle = self.driver.window_handles
        for self.handle in self.all_handle:
            if self.handle != self.shouye_handle:
                self.driver.switch_to.window(self.handle)
                self.send_text(filename=filename,xiaoqu_name=xiaoqu_name,jushi=jushi,mianji=mianji,qiwangshoujia=qiwangshoujia,lianxifangshi=lianxifangshi)

    #传入文件名称，读取文件中的内容（可读取多个内容）
    def duqutext(self,filename=''):
        neirong = readtxt(filename)
        print(neirong)
        for i in range(len(neirong)):
            #for name in neirong:
            wt_text = [na for na in neirong[i].split()]
            print(wt_text)
            xiaoqu_name = wt_text[0]
            jushi = wt_text[1]
            mianji = wt_text[2]
            qiwangshoujia = wt_text[3]
            lianxifangshi = wt_text[4]
            self.send_text(xiaoqu_name=xiaoqu_name, jushi=jushi, mianji=mianji, qiwangshoujia=qiwangshoujia, lianxifangshi=lianxifangshi)


if __name__ == "__main__":
    from selenium import webdriver
    import data.urldata as URL

    driver = webdriver.Chrome()

    url = URL.maitian_online_url
    #driver.get(url)
    driver.get('http://bj-test.imtfc.com/membersell')
    driver.implicitly_wait(2)
    driver.maximize_window()

    WeiTuo(driver).send_text(xiaoqu_name='龙腾苑', jushi=3, mianji=120, qiwangshoujia=300, lianxifangshi=15010561252)
    WeiTuo(driver).tijiao_click()
    sleep(3)
    warningText = WeiTuo(driver).get_warning_text()
    #WeiTuo(driver).jieshou_warning()
    print(warningText)
    sleep(3)

  #  WeiTuo(driver).duqutext('lianxi')
 #   driver.quit()