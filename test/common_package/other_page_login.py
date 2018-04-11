#!/usr/bin/python
from selenium import webdriver
from test.common_package.basic import Page
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OtherPageLogin(Page):
    def login_fangshi_click(self,loginfangshi):
        self.find_element(*(By.XPATH,loginfangshi)).click()

    def send_tel(self,tel,telD='txtLoginName'):
        self.find_element(*(By.ID, telD)).clear()
        self.find_element(*(By.ID, telD)).send_keys(tel)

    def send_password(self,password,passID='txtPassword'):
        self.find_element(*(By.ID, passID)).clear()
        self.find_element(*(By.ID, passID)).send_keys(password)

    def login_click(self,loginID='btnLogin'):
        self.find_element(*(By.ID, loginID)).click()

    def get_login_username(self,userxpath):
        return self.find_element(*(By.XPATH,userxpath)).text

    def user_error_hint(self):
        return self.driver.switch_to_alert().text

if __name__=='__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://bj-test.imtfc.com/bkesf')
    driver.find_element(*(By.XPATH,'/html/body/div[3]/section[2]/div[2]/div[2]/ul/li[1]/div/div[1]/h6/span[1]')).click()
    OtherPageLogin(driver).login_fangshi_click('/html/body/div[2]/div/p/span[2]')
    OtherPageLogin(driver).send_tel(telD='txtLoginName',tel='15010561252')
    OtherPageLogin(driver).send_password(passID='txtPassword', password='a123456')
    OtherPageLogin(driver).login_click(loginID='btnLogin')
    sleep(2)
    a = OtherPageLogin(driver).get_login_username('/html/body/header/div/div/p/a[3]')
    print(a)
    sleep(5)
    driver.quit()

