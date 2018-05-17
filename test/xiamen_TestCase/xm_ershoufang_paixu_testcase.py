#!/usr/bin/python
# -*- coding:UTF-8 -*-

from test.common_package import myunit
from time import sleep
from test.common_package.searchcommon import SearchCommon
from test.common_package.selectcity import SelectCity
from test.common_package.basic import Page

class Bj_ErShouFang_All_PaiXu(myunit.MyTest,Page):
    #单元测试使用
    #def __init__(self,driver):
    #    self.driver = driver

    def open_url(self):
        SelectCity(self.driver).dakaiwangzhan()  # 打开网站
        sleep(2)
        SelectCity(self.driver).maitian_online_city_select(cityname=2)  # 选择城市
        self.shouye_handle = self.driver.current_window_handle
        SelectCity(self.driver).second_hand_house()  # 二手房
        sleep(3)
        self.all_handle = self.driver.window_handles
        for self.handle in self.all_handle:
            if self.handle != self.shouye_handle:
                self.driver.switch_to.window(self.handle)
        sleep(1)

    def test_1(self):
        self.open_url()
        SearchCommon(self.driver).paixu_list(paixuname='总价')
        SearchCommon(self.driver).paixu_list(paixuname='单价')
        SearchCommon(self.driver).paixu_list(paixuname='面积')

if __name__=="__main__":
    from selenium import webdriver
    import data.urldata as URL

    driver = webdriver.Chrome()
    url = URL.maitian_online_url
    driver.get(url)
    # driver.get('http://bj-test.imtfc.com/esfway/B1D1/T3L1')
    driver.implicitly_wait(2)
    driver.maximize_window()
    Bj_ErShouFang_All_PaiXu(driver).test_1()
