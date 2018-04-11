#!/usr/bin/python
import data.urldata as URL
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Page(object):
    maitian_online_url = URL.maitian_online_url

    def __init__(self, selenium_driver, base_url=maitian_online_url, parent=None):
        self.driver = selenium_driver
        self.base_url = base_url
        self.timeout = 30
        self.parent = parent

    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), 'Did not land on %s' % url

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def open(self):
        self._open(self.url)

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def script(self, src):
        return self.driver.execute_script("arguments[0].scrollIntoView();", src)

    def zhengzebioadashi(self,pipei_re,pipei_str,group=''):
        re_compile = re.compile(pipei_re)
        if group == True:
            #re_groups = re.findall(re_compile, pipei_str)
            re_groups = re_compile.findall(pipei_str)
            for regs in re_groups:
                re_groups[re_groups.index(regs)] = regs[0]
            return re_groups
        else:
            return re.findall(re_compile, pipei_str)