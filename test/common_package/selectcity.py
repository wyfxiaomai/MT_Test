#!/usr/bin/python
# -*- coding:UTF-8 -*-
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from test.common_package.basic import Page

class SelectCity(Page):
    url = '/'
    city_button = (By.XPATH, '/html/body/header/div/div[1]/div/div[1]/div/span')  # 城市选择
    city_name = ((By.LINK_TEXT, '北京'),(By.LINK_TEXT, '福州'),(By.LINK_TEXT, '厦门'))

    #打开网站
    def dakaiwangzhan(self):
        self.open()

    # 城市选择，cityname=0，表示选择北京，cityname=1，表示选择福州，cityname=2，表示选择厦门
    def maitian_online_city_select(self,cityname=0):    #调用该函数时，传入参数可分别为0,1,2
        self.city = self.find_element(*self.city_button)
        ActionChains(self.driver).move_to_element(self.city).perform()
        sleep(3)
        self.find_element(*self.city_name[cityname]).click()
        sleep(2)

    # 点击二手房
    second_hand_house_loc = (By.XPATH, '/html/body/header/div/div[1]/div/div[2]/nav/ul/li[2]/a')
    def second_hand_house(self):
        self.find_element(*self.second_hand_house_loc).click()

    #点击租房
    zufang_loc = (By.XPATH,'/html/body/header/div/div[1]/div/div[2]/nav/ul/li[3]/a')
    def zufang(self):
        self.find_element(*self.zufang_loc).click()

    #点击别墅
    bieshu_loc = (By.XPATH, '/html/body/header/div[1]/div[1]/div/div[2]/nav/ul/li[3]/a')
    def bieshu(self):
        self.find_element(*self.bieshu_loc).click()

    #点击小区
    xiaoqu_loc = (By.XPATH,'/html/body/header/div/div[1]/div/div[2]/nav/ul/li[4]/a')
    def xiaoqu(self):
        self.find_element(*self.xiaoqu_loc).click()

    #点击房产顾问
    fangchanguwen_loc = (By.XPATH,'/html/body/header/div/div[1]/div/div[2]/nav/ul/li[5]/a')
    def fangchanguwen(self):
        self.find_element(*self.fangchanguwen_loc).click()

    #点击委托
    weituo_loc = (By.XPATH,'/html/body/header/div/div[1]/div/div[2]/nav/ul/li[6]/a')
    def weituo(self):
        self.find_element(*self.weituo_loc).click()

if __name__=="__main__":
    from selenium import webdriver
    import data.urldata as URL

    driver = webdriver.Chrome()
    url = URL.maitian_online_url
    #driver.get(url)
    driver.get('http://bj-test.imtfc.com/index.html')
    driver.implicitly_wait(3)
    driver.maximize_window()
    sleep(1)
    SelectCity(driver).maitian_online_city_select(2)
    SelectCity(driver).weituo()
    sleep(2)
    driver.quit()