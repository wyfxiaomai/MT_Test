#!/usr/bin/python
#-*- coding:UTF-8 -*-

from selenium.webdriver.common.by import By
from test.common_package.basic import Page
from lib.readtxt import readtxt
from time import sleep

class SearchThinkWordPanDuan(Page):
    def twpanduan(self):
        search_kuangid = 'ico-search'
        thinkwordid = 'SearchTips'
        self.find_element(*(By.ID,search_kuangid)).clear()
        self.find_element(*(By.ID, search_kuangid)).send_keys('海淀')
        sleep(2)
        thinkword = self.find_element(*(By.ID,thinkwordid)).text
        #print(self.find_element(*(By.ID,thinkwordid)).text)
        print(thinkword)
        thinkword_list = [think for think in thinkword.split('\n') if '待售' not in think]
        print(thinkword_list)
        for word in thinkword_list:
            try:
                assert '朝阳' in word
            except Exception as e:
                print("%s 联想词有误！！！" % word)

if __name__ == "__main__":
    from selenium import webdriver
    import data.urldata as URL
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get(URL.maitian_online_url)
    # driver.get('http://fz-test.imtfc.com/VIEW/Index/Index2.html')
    # driver.get('http://xm-test.imtfc.com/VIEW/Index/Index2.html')
    SearchThinkWordPanDuan(selenium_driver=driver).twpanduan()
    driver.close()