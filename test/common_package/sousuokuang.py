#!/usr/bin/python
"""
说明：
用于除首页外其他页面的搜索框内容搜索，若果单测摸个页面，在各个页面调用该类中的“send_sousuoneirong()”方法，搜索内容在文件“sousuoneirong”中编辑，格式为城市(北京、福州、厦门)---搜索类型
(二手房、租房、小区、房产顾问、别墅)---搜索内容，每一个内容占一行，
例如：
北京
二手房
海淀
朝阳
租房
海淀
朝阳
房产顾问
李增辉
周
小区
海淀
朝阳
"""

from time import sleep
from selenium.webdriver.common.by import By
from test.common_package.basic import Page
from lib.readtxt import readtxt
from test.common_package.searchcommon import SearchCommon
from test.common_package.selectcity import SelectCity

class SouSuoKuang(Page):
    #点击搜索按钮
    def sousuo_click(self,buttomID='btSearch'):
        self.find_element(*(By.ID,buttomID)).click()

    #获取城市名称
    def get_cityname(self,cityClass='show'):
        return self.find_element(*(By.CLASS_NAME, cityClass)).text

    #获取页面类型
    def get_page_leixing(self):
        url_leixing = ['esfall','esfbslb','xqall','bkesf','zfall']
        leixing = ['二手房','别墅','小区','房产顾问','租房']
        for URL in url_leixing:
            if URL in self.driver.current_url:
                return leixing[url_leixing.index(URL)]  #返回所在的页面类型

    #读取文件中的搜索内容
    def readsousuoneirong(self):
        searchtext = readtxt('sousuoneirong')#调用readtxt读取文件中的内容
        searchtext_id = [index for index, name in enumerate(searchtext) if name == '北京' or name == '福州' or name == '厦门']#获取城市名称在列表中的index
        city_name = self.get_cityname()
        leixing_name = self.get_page_leixing()
        #print('searchtext_ALL', searchtext)
        #print('searchtext_id',searchtext_id)
        for city in searchtext:     #从获取的文件内容中判断当前所在城市，并取出该城市下的所有内容
            if  city == city_name:
                city_index = searchtext.index(city)
        for city_son in searchtext[city_index+1:]:  #截取城市中的内容
            if city_son == '北京' or city_son == '福州' or city_son == '厦门':
                city_index_son = searchtext.index(city_son) #当读取另一个城市的名称时，记录该名称所在位置并结束循环
                break
            else:
                city_index_son = -1 #如果没有读取到其他城市名称，则标志赋值为-1，说明该城市在文件中为最后一个城市
        if city_index_son == -1:    #如果标志位-1，读取城市名称后面一个位置的内容，直到最后
            searchtext = searchtext[city_index + 1:]
        else:
            searchtext = searchtext[city_index+1:city_index_son]#如果标志位不为-1，读取读取城市名称后面一个位置的内容，直到下一个城市位置的前一个内容

        #print('searchtext',searchtext)
        for leixingname in searchtext:#从获取的城市内容中获取类型所在位置（读取类型中的内容逻辑同读取城市中的内容逻辑一致）
            if leixingname == leixing_name:
                jiequ_index = searchtext.index(leixing_name)
        for jiequ in searchtext[jiequ_index+1:]:#截取类型中的内容
            if jiequ == '二手房' or jiequ == '租房' or jiequ == '小区'or jiequ == '房产顾问' or jiequ == '别墅':
                jiequ_index_son = searchtext.index(jiequ)
                break
            else:
                jiequ_index_son = -1
        if jiequ_index_son == -1:
            searchtext = searchtext[jiequ_index + 1:]
        else:
            searchtext = searchtext[jiequ_index+1:jiequ_index_son]
        #print('searchtext_END', searchtext)
        return searchtext

    #输入搜索内容并搜索
    def send_sousuoneirong(self,wenbenID='ico-search'):
        for txt in self.readsousuoneirong():
            self.find_element(*(By.ID,wenbenID)).clear()
            self.find_element(*(By.ID, wenbenID)).send_keys(txt)
            sleep(2)
            self.get_lianxiangci(txt=txt)
            self.find_element(*(By.ID, wenbenID)).clear()
            self.sousuo_click()
            self.find_element(*(By.ID, wenbenID)).send_keys(txt)
            self.sousuo_click()
            self.panduan_list()

    #获取联想词
    def get_lianxiangci(self,thinkwordid = 'SearchTips',txt=''):
        thinkword = self.find_element(*(By.ID, thinkwordid)).text
        thinkword_linkname = ['待售', '待租']
        if thinkword is None:
            print('%s 没有联想词！！！' % txt)
        thinkword_list = [think for think in thinkword.split('\n') ]    #以‘\n’为标志解析获取的内容，返回一个解析列表
        for thinkword in thinkword_list:    #过滤联想词解析列表中待售、待租的字段
            if thinkword_linkname[0] and thinkword_linkname[1] in thinkword:#如果待售待租同时包含在联想词中，删除该联想词（出现在小区页面）
                thinkword_list.remove(thinkword)
            else:
                for th_daizudaishou in thinkword_linkname:  #如果包含待售或待租，删除该联想词
                    if th_daizudaishou in thinkword:
                        thinkword_list.remove(thinkword)
        #print('处理后的联想词：',thinkword_list)
        for lianxiangci in thinkword_list:  #判断搜索的内容是否包含在过滤后的联想词中
            try:
                assert txt in lianxiangci
                #print('%s 包含在 %s' % (txt,lianxiangci))
            except BaseException as e:
                print('%s 不包含在 %s' % (txt,lianxiangci))
        self.lianxiangci_click(thinkwordid=thinkwordid,thinkword_list=thinkword_list,txt=txt)

    #判断搜索内容在列表的正确性
    shouye_link_loc = (By.XPATH, '//div[@id="paging"]/a')
    weiye_link_loc = (By.LINK_TEXT, '尾页')
    xiayiye_link_loc = (By.LINK_TEXT, '下一页')
    weiyeshu_loc = (By.CLASS_NAME, 'on')
    def panduan_list(self,link=''):
        if link == '':
            pass
        else:
            self.find_element(*(By.PARTIAL_LINK_TEXT, link)).click()
        jiansuoneirong = SearchCommon(self.driver).get_jiansuotiaojian_text(jiansuoneirong_ID='SearchHouseTerm')
        fangyuanliebiao = SearchCommon(self.driver).get_fangyuanliebiao_list(fangyuanliebiao_className='list_wrap')[0]
        fangyuanzongshu = SearchCommon(self.driver).get_fangyuan_zongshu(fangyaunzongshu_xpath="//p[@class='search_result']/span")

        if int(fangyuanzongshu) <= 10:
            for js in jiansuoneirong:
                for fy in fangyuanliebiao:
                    try:
                        assert js in fy
                        #print('%s 包含在 %s'%(js,fy))
                    except BaseException as e:
                        print('%s 不包含在 %s' % (js, fy))
        else:
            self.find_element(*self.weiye_link_loc).click()  # 点击尾页
            sleep(2)
            zongshu_ye = self.find_element(*self.weiyeshu_loc).text  # 获取总页数
            self.find_element(*self.shouye_link_loc).click()  # 点首页
            for zs in range(int(zongshu_ye)):
                fangyuanliebiao = SearchCommon(self.driver).get_fangyuanliebiao_list(fangyuanliebiao_className='list_wrap')[0]
                for js in jiansuoneirong:
                    for fy in fangyuanliebiao:
                        try:
                            assert js in fy
                            #print('%s 包含在 %s' % (js, fy))
                        except BaseException as e:
                            print('%s 不包含在 %s' % (js, fy))
                self.yeshu_link_loc = (By.LINK_TEXT, str(zs + 1))
                self.find_element(*self.xiayiye_link_loc).click()  # 点击下一页
                sleep(1)
            self.find_element(*self.shouye_link_loc).click()  # 点首页

    #点击联想词并判断
    def lianxiangci_click(self,thinkword_list='',thinkwordid = 'SearchTips',wenbenID='ico-search',txt='' ):
        self.script(self.find_element(*(By.ID, thinkwordid)))
        for link in thinkword_list:
            self.panduan_list(link=link)    #调用判断列表中的内容是否是联想词的搜索内容
            self.find_element(*(By.ID, wenbenID)).clear()
            sleep(2)
            self.find_element(*(By.ID, wenbenID)).send_keys(txt)
            sleep(2)

    #统一调用
    def tongyidiaoyong(self,cityname=0,leixing='二手房'):
        SelectCity(self.driver).dakaiwangzhan()  # 打开网站
        sleep(2)
        SelectCity(self.driver).maitian_online_city_select(cityname=cityname)  # 选择城市
        sleep(3)
        self.shouye_handle = self.driver.current_window_handle
        if leixing == '二手房':
            SelectCity(self.driver).second_hand_house()  # 点击二手房
        elif leixing == '租房':
            SelectCity(self.driver).zufang()  # 点击租房
        elif leixing == '小区':
            SelectCity(self.driver).xiaoqu()  # 点击小区
        elif leixing == '房产顾问':
            SelectCity(self.driver).fangchanguwen()  # 点击房产顾问
        else:
            SelectCity(self.driver).bieshu()  # 点击别墅
        sleep(3)
        self.all_handle = self.driver.window_handles
        for self.handle in self.all_handle:
            if self.handle != self.shouye_handle:
                self.driver.switch_to.window(self.handle)
                self.send_sousuoneirong()



if __name__ == "__main__":
    from selenium import webdriver
    import data.urldata as URL

    driver = webdriver.Chrome()
    url = URL.maitian_online_url
    # driver.get(url)
    driver.get('http://fz-test.imtfc.com/bkesf')
    driver.implicitly_wait(2)
    driver.maximize_window()
    SouSuoKuang(driver).send_sousuoneirong()