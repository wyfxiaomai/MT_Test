#!/usr/bin/python
from selenium import webdriver
import time

def insert_img(driver,filename):
    now = time.strftime('%Y-%m-%d  %H-%M-%S')
    filepath = "G:\\test_result\\get_screenshot\\" + now + ' ' + filename
    driver.get_screenshot_as_file(filepath)

if __name__=="__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://www.baidu.com')
    insert_img(driver,'1.png')
    driver.quit()