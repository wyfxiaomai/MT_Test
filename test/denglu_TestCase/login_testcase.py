#!/usr/bin/python
# -*-coding:UTF-8 -*-
import random
import unittest,os
from time import sleep

from test.common_package import myunit
from test.denglu_TestCase.loginPage import login


class loginTest(myunit.MyTest):
    def user_login_verify(self,username='',password=''):
        login(self.driver).user_login(username,password)

    def test_login(self):
        ''' 用户名和密码正确'''
        self.user_login_verify(username='15010561252',password='a123456')
        sleep(3)
        po = login(self.driver)

    #username and password is NULL
    def test_login_1(self):
        '''用户名和密码为空'''
        self.user_login_verify()
        po = login(self.driver)
        self.assertEqual(po.user_error_hint(),'温馨提示：请输入手机号！')
        self.assertEqual(po.pawd_error_hint(),'温馨提示：请输入手机号！')

    def test_login_2(self):
        '''用户名正确，密码为空'''
        self.user_login_verify('15010561252')
        po = login(self.driver)
        self.assertEqual(po.pawd_error_hint(),'温馨提示：请输入密码！')

    def test_login_3(self):
        '''用户名为空，密码正确'''
        self.user_login_verify(password='a123456')
        po = login(self.driver)
        self.assertEqual(po.user_error_hint(),'温馨提示：请输入手机号！')

    def test_login_4(self):
        '''用户名正确，密码为空'''
        character = random.choice('1234567890')
        password = 'a123456' + character
        self.user_login_verify(username='15010561252',password=password)
        po = login(self.driver)
        self.assertEqual(po.pawd_error_hint(),'温馨提示：用户名或密码错误！')
        
if __name__=="__main__":
    unittest.main()
