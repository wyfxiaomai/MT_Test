#!/usr/bin/python
# -*- coding:UTF-8 -*-
import data.shhdata as Data
from test.common_package import myunit
from test.common_package.shouye_search import ShouYeSearch
from test.common_package.pgbo_check import PageBottomCheck
from test.common_package.selectcity import SelectCity
from time import sleep

class Bj_ShouYe(myunit.MyTest):
    def open_url(self):
        SelectCity(self.driver).dakaiwangzhan()  # 打开网站
        sleep(2)
        SelectCity(self.driver).maitian_online_city_select(cityname=2)  # 选择城市
        sleep(3)

    def test_1(self):
        self.open_url()
        ShouYeSearch(self.driver).tongyidiaoyong()
        PageBottomCheck(self.driver).tongyidiaoyong()