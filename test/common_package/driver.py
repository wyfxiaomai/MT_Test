#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver import Remote
import os,time

"""
def browser():

    lists = {'http://127.0.0.1:4444/wd/hub': 'chrome',
            'http://172.16.13.105:5555/wd/hub':'chrome',
                }
    for host, browser in lists.items():
        print(host, browser)
        driver = Remote(command_executor=host,  # 地址
                        desired_capabilities={'platform': 'ANY',  # 测试平台（默认ANY）
                                                'browserName': browser,  # 浏览器
                                                'version': '',  # 浏览器版本
                                                'javascriptEnabled': True  # javascript启动状态״̬
                                                }
                        )
       # driver.get('http://www.baidu.com')
        #host = '127.0.0.1:4444'
       # dc = {'browserName': 'chrome'}
        #driver = Remote(command_executor='http://' + host + '/wd/hub',
        #                desired_capabilities=dc
        #                )

    #chromedriver = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))+'/config/chromedriver.exe'
    #os.environ["webdriver.chrome.driver"] = chromedriver
    #driver = webdriver.Chrome(chromedriver)
    #driver = webdriver.Chrome()
    time.sleep(2)
    global driver
    return driver


"""
def browser():
    #driver = webdriver.Chrome()
    driver = webdriver.PhantomJS()
    return driver


if __name__=="__main__":
    br = browser()
    br.get('http://www.baidu.com')
    time.sleep(2)
    br.quit()

