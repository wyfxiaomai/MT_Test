#!/usr/bin/python
# -*- coding:UTF-8 -*-

from test.common_package import myunit
from time import sleep
from test.common_package.weituo import WeiTuo
from test.common_package.selectcity import SelectCity
from test.common_package.basic import Page
from selenium.webdriver.common.by import By
import unittest

class Bj_WeiTuo_TestCase(myunit.MyTest,Page):
    def open_url(self):
        SelectCity(self.driver).dakaiwangzhan()  # 打开网站
        sleep(2)
        #SelectCity(self.driver).maitian_online_city_select(cityname=0)  # 选择城市
        self.shouye_handle = self.driver.current_window_handle
        SelectCity(self.driver).weituo()  # 点击委托
        sleep(3)
        self.all_handle = self.driver.window_handles
        for self.handle in self.all_handle:
            if self.handle != self.shouye_handle:
                self.driver.switch_to.window(self.handle)
        sleep(1)

    def test_1(self):
        """正确的输入内容"""
        self.open_url()
        WeiTuo(self.driver).send_text(xiaoqu_name='龙腾苑',jushi=3,mianji=120,qiwangshoujia=300,lianxifangshi=15010561252)
        WeiTuo(self.driver).tijiao_click()
        sleep(1)
        warningText = WeiTuo(self.driver).get_warning_text()
        WeiTuo(self.driver).jieshou_warning()
        try:
            self.assertEqual(warningText,'温馨提示：卖房委托已成功提交！')
        except Exception as e:
            print(e)

    def test_2(self):
        """小区名称为空"""
        self.open_url()
        WeiTuo(self.driver).send_text(xiaoqu_name='',jushi=3,mianji=120,qiwangshoujia=300,lianxifangshi=15010561252)
        WeiTuo(self.driver).tijiao_click()
        sleep(1)
        warningText = WeiTuo(self.driver).get_warning_text()
        WeiTuo(self.driver).jieshou_warning()
        try:
            self.assertEqual(warningText,'请输入小区名称')
        except Exception as e:
            print(e)

    def test_3(self):
        """居室为空"""
        self.open_url()
        WeiTuo(self.driver).send_text(xiaoqu_name='龙腾苑',jushi='',mianji=120,qiwangshoujia=300,lianxifangshi=15010561252)
        WeiTuo(self.driver).tijiao_click()
        sleep(1)
        warningText = WeiTuo(self.driver).get_warning_text()
        WeiTuo(self.driver).jieshou_warning()
        try:
            self.assertEqual(warningText,'温馨提示：请输入正确的居室！')
        except Exception as e:
            print(e)

    def test_4(self):
        """面积为空"""
        self.open_url()
        WeiTuo(self.driver).send_text(xiaoqu_name='龙腾苑',jushi=3,mianji='',qiwangshoujia=300,lianxifangshi=15010561252)
        WeiTuo(self.driver).tijiao_click()
        sleep(1)
        warningText = WeiTuo(self.driver).get_warning_text()
        WeiTuo(self.driver).jieshou_warning()
        try:
            self.assertEqual(warningText,'温馨提示：请输入面积！')
        except Exception as e:
            print(e)

    def test_5(self):
        """售价为空"""
        self.open_url()
        WeiTuo(self.driver).send_text(xiaoqu_name='龙腾苑',jushi=3,mianji=120,qiwangshoujia='',lianxifangshi=15010561252)
        WeiTuo(self.driver).tijiao_click()
        sleep(1)
        warningText = WeiTuo(self.driver).get_warning_text()
        WeiTuo(self.driver).jieshou_warning()
        try:
            self.assertEqual(warningText,'温馨提示：请输入售价！')
        except Exception as e:
            print(e)

    def test_6(self):
        """售价为空"""
        self.open_url()
        WeiTuo(self.driver).send_text(xiaoqu_name='龙腾苑',jushi=3,mianji=120,qiwangshoujia=666,lianxifangshi='')
        WeiTuo(self.driver).tijiao_click()
        sleep(1)
        warningText = WeiTuo(self.driver).get_warning_text()
        WeiTuo(self.driver).jieshou_warning()
        try:
            self.assertEqual(warningText,'温馨提示：请输入正确手机号！')
        except Exception as e:
            print(e)

    def test_7(self):
        """输入不符合要求的手机号"""
        self.open_url()
        WeiTuo(self.driver).send_text(xiaoqu_name='龙腾苑',jushi=3,mianji=120,qiwangshoujia=666,lianxifangshi='12345678901')
        #WeiTuo(self.driver).tijiao_click()
        sleep(1)
        warningText = WeiTuo(self.driver).get_warning_text()
        WeiTuo(self.driver).jieshou_warning()
        try:
            self.assertEqual(warningText,'温馨提示：请输入正确手机号！')
        except Exception as e:
            print(e)

    def test_8(self):
        """输入没有注册的手机号"""
        self.open_url()
        WeiTuo(self.driver).send_text(xiaoqu_name='龙腾苑',jushi=3,mianji=120,qiwangshoujia=666,lianxifangshi='18351886391')
        #WeiTuo(self.driver).tijiao_click()
        sleep(1)
        warningText = WeiTuo(self.driver).get_warning_text()
        WeiTuo(self.driver).jieshou_warning()
        try:
            self.assertEqual(warningText,'您目前不是注册用户，请输入手机短信验证码，完成委托！')
        except Exception as e:
            print(e)
        yanzhengma = self.find_element(*(By.ID,'liYZM')).text
        try:
            self.assertIn('验证码',yanzhengma)
        except Exception as e:
            print(e)

if __name__=="__main__":
    unittest.main()