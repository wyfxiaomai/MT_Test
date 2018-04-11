#!/usr/bin/python
# -*-coding:UTF-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from test.common_package.basic import Page
from time import sleep 
class login(Page):
    url = '/'
    maitian_online_login_user_loc = (By.LINK_TEXT,"登录")
    maitian_online_login_button_loc = (By.XPATH,'/html/body/div[3]/div[2]/p/span[2]')
    
    def maitian_online_login(self):
        self.find_element(*self.maitian_online_login_user_loc).click()
        sleep(3)
        self.find_element(*self.maitian_online_login_button_loc).click()
        sleep(3)
    
    login_user_loc = (By.ID,'txtLoginName')
    login_password_loc = (By.ID,'txtPassword')
    login_button_loc = (By.ID,'btnLogin')
    
    #login_user
    def login_username(self,username):
        self.find_element(*self.login_user_loc).send_keys(username)
    
    #login_password
    def login_password(self,password):
        self.find_element(*self.login_password_loc).send_keys(password)
    
    #login_button
    def login_button(self):
        self.find_element(*self.login_button_loc).click()
        
    #Uniform login entry
    def user_login(self,username="13522092612",password="a123456"):
        self.open()
        self.maitian_online_login()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(2)
        
    #username error
    def user_error_hint(self):
        return self.driver.switch_to_alert().text
    
    #password error
    def pawd_error_hint(self):
        return self.driver.switch_to_alert().text
    
    
    
    