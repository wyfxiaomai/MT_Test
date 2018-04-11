#!/usr/bin/python
from test.common_package.driver import browser
import unittest
class MyTest(unittest.TestCase):
     def setUp(self):
         self.driver = browser()
         self.driver.implicitly_wait(3)
         self.driver.maximize_window()

     def setDown(self):
         self.driver.quit()

"""
    #def setUp(self):
    @classmethod        #使用@classmethod 只打开一次浏览器，最后统一关闭浏览器，用例较多时，节省多次打开、关闭浏览器的时间
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    #def setDown(self):
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
"""
if __name__=="__main__":
    unittest.main()