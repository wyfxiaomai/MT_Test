#!/usr/bin/python
# -*- coding:UTF-8 -*-
"""
For_BianLi()类中包含10层for循环，一个tongyidiaoyong()方法，该方法参数有：
cityname,leixing，pricemin,pricemax,mianjimin,mianjimax,fy_xpath_qian_li,fy_xpath_hou_li,for_1_range,subway_f='',subway_f_xpath='',louceng_xpath='',louling_xpath='',for_1_2_index='',for_1_list='',for_2_list='',for_3_list='',for_4_list='',for_5_list='',for_6_list='',for_7_list='',for_8_list='',for_9_list='',for_10_list='',for_1_indexmin=0,for_1_indexmax=100,for_2_indexmin=0,for_2_indexmax=100,for_3_indexmin=0,for_3_indexmax=100,for_4_indexmin=0,for_4_indexmax=100,for_5_indexmin=0,for_5_indexmax=100, for_6_indexmin=0, for_6_indexmax=100,for_7_indexmin=0,for_7_indexmax=100,for_8_indexmin=0,for_8_indexmax=100, for_9_indexmin=0, for_9_indexmax=100,for_10_indexmin=0,for_10_indexmax=100,for_1_flag=True,for_2_flag=True,for_3_flag=True,for_4_flag=True,for_5_flag=True,for_6_flag=True,for_7_flag=True,for_8_flag=True,for_9_flag=True,for_10_flag=True,for_3_buxian='',for_4_buxian='',for_5_buxian='',for_6_buxian='',for_7_buxian='',for_8_buxian=''

cityname：必传参数，要选择的城市，参数值分别为0,1,2。-----0:北京，1：福州，2:厦门
leixing：必传参数，在首页时要点击的菜单栏，参数有：二手房、租房、小区、房产顾问、别墅
pricemin,pricemax:必传参数,存放售价的最大最小值
mianjimin,mianjimax：必传参数,存放面积的最大最小值
fy_xpath_qian_li：必传参数，截取的房源或顾问列表的xpath路径<ul>/<li>标签前一部分，例如 '//div[@class="list_wrap"]/ul/li[1]/ a / img'或'/html/body/section[2]/div[2]/div[2]/ul/li[1]/div[1]/a'截取'//div[@class="list_wrap"]/ul/li[’ 或‘/html/body/section[2]/div[2]/div[2]/ul/li[’
fy_xpath_hou_li：必传参数，截取的房源或顾问列表的xpath路径<ul>/<li>标签后一部分，例如 '//div[@class="list_wrap"]/ul/li[1]/ a / img'或'/html/body/section[2]/div[2]/div[2]/ul/li[1]/div[1]/a'截取']/ a / img’ 或‘]/a’
for_1_range:可选参数，存放区域或地铁线路ID所在的位置，传参模式可为（供参考）：for i, line in enumerate(quYu):linkindex.append(i)，当for_1_flag=False时，可以不传该参数。
subway_f:可选参数，点击地铁房的标识，参数为“地铁房”，默认为空
subway_f_xpath:可选参数，点击地铁房的标识，参数为“地铁房的xpath路径”，默认为空，当subway_f传入参数时，该参数为必传参数
louceng_xpath：可选参数，存放楼层所在页面的xpath路径，当for_9_flag=False时，可不传该参数
louling_xpath：可选参数，存放楼龄所在页面的xpath路径，当for_10_flag=False时，可不传该参数
for_1_2_index:可选参数,存放每个区域的商圈数量或每个地铁线路站台的数量，当for_2_flag=False时，可不传该参数
for_1_list --- for_10_list：可选参数，存放每一个for循环的列表值，列表中存放的是所要遍历的标签ID,如：for_2_list=shangQuan
for_1_indexmin --- for_10_indexmin：可选参数，存放每一个for循环列表的范围的最小值，默认为零
for_1_indexmax ---  for_10_indexmax：可选参数，存放每一个for循环列表的范围的最大值，默认为100，传参时，可取所要传入的列表的长度，入len(shangQuan)
for_1_flag --- for_10_flag：可选参数，默认值为True，当传入的值为False时，不执行该层for循环，如：for_3_flag=False
for_3_buxian --- for_8_buxian：可选参数，当使用for_3 到for_8 中的某个for循环时，要传入该层的for_N_buxian 的值，参数值所要遍历内容的不限标签ID
"""

from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import data.shhdata as Data
from test.common_package.searchcommon import SearchCommon
from test.common_package.basic import Page
from test.common_package.selectcity import SelectCity

class For_BianLi(Page):
    def biaoqian(self):
        fangyuanzongshu_xpath = "//p[@class='search_result']/span"
        lingtishiyu_xpath = "//div[@class='no_home']"
        fangyuanliebiao_className = 'list_wrap'
        jiansuoneirong_ID = 'SearchHouseTerm'
        return fangyuanzongshu_xpath, lingtishiyu_xpath, fangyuanliebiao_className, jiansuoneirong_ID

    def for_1(self,pricemin,pricemax,mianjimin,mianjimax,louceng_xpath,louling_xpath,fy_xpath_qian_li,fy_xpath_hou_li,shouye_handle,page_url,for_1_flag,for_2_flag,for_3_flag,for_4_flag,for_5_flag,for_6_flag,for_7_flag,for_8_flag,for_9_flag,for_10_flag,for_1_range,for_1_list,for_2_list,for_3_list,for_4_list,for_5_list,for_6_list,for_7_list,for_8_list,for_9_list,for_10_list,for_1_indexmin,for_1_indexmax,for_2_indexmin,for_2_indexmax,for_3_indexmin,for_3_indexmax,for_4_indexmin,for_4_indexmax,for_5_indexmin,for_5_indexmax, for_6_indexmin, for_6_indexmax,for_7_indexmin,for_7_indexmax,for_8_indexmin,for_8_indexmax, for_9_indexmin, for_9_indexmax,for_10_indexmin,for_10_indexmax,for_1_2_index,for_3_buxian='',for_4_buxian='',for_5_buxian='',for_6_buxian='',for_7_buxian='',for_8_buxian=''):
        if for_1_flag == True:
            for_1_page_url = self.driver.current_url
            for f1_index in for_1_range:#for_1_range为一个列表，用来接收地铁线路ID所在的位置
                for f1 in for_1_list[f1_index:f1_index+1]:#获取某个ID
                    self.find_element(*(By.ID,f1)).click()
                    sleep(2)
                    if SearchCommon(self.driver).fangyuan_zongshu_ling(self.biaoqian()[0]) == False:   #如果房源总数为零，说明该线路下没有房源，结束本层循环，不再做后面的搜索查询
                        SearchCommon(self.driver).fangyuan_zongshu_ling_panduantishiyu(self.biaoqian()[1]) #判断房源为零时候的提示语
                        continue
                    if for_2_flag == True:    #如果for_2_flag标识为真，点击该地区域或铁线路下的所有商圈或站点，否则该线路下的站台不限
                        for f2 in for_2_list[sum(for_1_2_index[0:f1_index]):sum(for_1_2_index[0:f1_index])+for_1_2_index[f1_index]]:#切片用于获取相应商圈或地铁线路站台的ID
                            self.find_element(*(By.ID,f2)).click()
                            if SearchCommon(self.driver).fangyuan_zongshu_ling(self.biaoqian()[0]) == False:#如果房源总数为零，说明没有房源，结束本层循环，不再做后面的搜索查询
                                SearchCommon(self.driver).fangyuan_zongshu_ling_panduantishiyu(self.biaoqian()[1])#判断房源为零时候的提示语
                                continue
                            if 'way' in for_1_page_url:
                                subwaylinesontext = self.find_element(*(By.ID, f2)).text
                                self.for_3(pricemin=pricemin, pricemax=pricemax,mianjimin=mianjimin,mianjimax=mianjimax,louceng_xpath=louceng_xpath,louling_xpath=louling_xpath,for_3_buxian=for_3_buxian,for_4_buxian=for_4_buxian,for_5_buxian=for_5_buxian,for_6_buxian=for_6_buxian,for_7_buxian=for_7_buxian,for_8_buxian=for_8_buxian,fy_xpath_qian_li=fy_xpath_qian_li,fy_xpath_hou_li=fy_xpath_hou_li,subwaylinesontext=subwaylinesontext, page_url=page_url,shouye_handle=shouye_handle,for_3_list=for_3_list, for_4_list=for_4_list, for_5_list=for_5_list,for_6_list=for_6_list, for_7_list=for_7_list, for_8_list=for_8_list,for_9_list=for_9_list, for_10_list=for_10_list,for_3_indexmin=for_3_indexmin, for_3_indexmax=for_3_indexmax,for_4_indexmin=for_4_indexmin, for_4_indexmax=for_4_indexmax,for_5_indexmin=for_5_indexmin, for_5_indexmax=for_5_indexmax,for_6_indexmin=for_6_indexmin, for_6_indexmax=for_6_indexmax,for_7_indexmin=for_7_indexmin, for_7_indexmax=for_7_indexmax,for_8_indexmin=for_8_indexmin, for_8_indexmax=for_8_indexmax,for_9_indexmin=for_9_indexmin, for_9_indexmax=for_9_indexmax,for_10_indexmin=for_10_indexmin, for_10_indexmax=for_10_indexmax,for_3_flag=for_3_flag, for_4_flag=for_4_flag, for_5_flag=for_5_flag,for_6_flag=for_6_flag, for_7_flag=for_7_flag, for_8_flag=for_8_flag,for_9_flag=for_9_flag, for_10_flag=for_10_flag)
                                sleep(1)
                            else:
                                self.for_3(pricemin=pricemin, pricemax=pricemax,mianjimin=mianjimin,mianjimax=mianjimax,louceng_xpath=louceng_xpath,louling_xpath=louling_xpath,for_3_buxian=for_3_buxian,for_4_buxian=for_4_buxian,for_5_buxian=for_5_buxian,for_6_buxian=for_6_buxian,for_7_buxian=for_7_buxian,for_8_buxian=for_8_buxian,fy_xpath_qian_li=fy_xpath_qian_li,fy_xpath_hou_li=fy_xpath_hou_li,page_url=page_url,shouye_handle=shouye_handle,for_3_list=for_3_list,for_4_list=for_4_list,for_5_list=for_5_list,for_6_list=for_6_list,for_7_list=for_7_list,for_8_list=for_8_list,for_9_list=for_9_list,for_10_list=for_10_list,for_3_indexmin=for_3_indexmin,for_3_indexmax=for_3_indexmax,for_4_indexmin=for_4_indexmin,for_4_indexmax=for_4_indexmax,for_5_indexmin=for_5_indexmin,for_5_indexmax=for_5_indexmax, for_6_indexmin=for_6_indexmin, for_6_indexmax=for_6_indexmax,for_7_indexmin=for_7_indexmin,for_7_indexmax=for_7_indexmax,for_8_indexmin=for_8_indexmin,for_8_indexmax=for_8_indexmax, for_9_indexmin=for_9_indexmin, for_9_indexmax=for_9_indexmax,for_10_indexmin=for_10_indexmin,for_10_indexmax=for_10_indexmax,for_3_flag=for_3_flag,for_4_flag=for_4_flag,for_5_flag=for_5_flag,for_6_flag=for_6_flag,for_7_flag=for_7_flag,for_8_flag=for_8_flag,for_9_flag=for_9_flag,for_10_flag=for_10_flag)
                    else:
                       self.for_3(pricemin=pricemin, pricemax=pricemax,mianjimin=mianjimin,mianjimax=mianjimax,louceng_xpath=louceng_xpath,louling_xpath=louling_xpath,for_3_buxian=for_3_buxian,for_4_buxian=for_4_buxian,for_5_buxian=for_5_buxian,for_6_buxian=for_6_buxian,for_7_buxian=for_7_buxian,for_8_buxian=for_8_buxian,fy_xpath_qian_li=fy_xpath_qian_li,fy_xpath_hou_li=fy_xpath_hou_li,page_url=page_url,shouye_handle=shouye_handle,for_3_list=for_3_list, for_4_list=for_4_list, for_5_list=for_5_list,for_6_list=for_6_list, for_7_list=for_7_list, for_8_list=for_8_list,for_9_list=for_9_list, for_10_list=for_10_list, for_3_indexmin=for_3_indexmin,for_3_indexmax=for_3_indexmax, for_4_indexmin=for_4_indexmin,for_4_indexmax=for_4_indexmax, for_5_indexmin=for_5_indexmin,for_5_indexmax=for_5_indexmax, for_6_indexmin=for_6_indexmin,for_6_indexmax=for_6_indexmax, for_7_indexmin=for_7_indexmin,for_7_indexmax=for_7_indexmax, for_8_indexmin=for_8_indexmin,for_8_indexmax=for_8_indexmax, for_9_indexmin=for_9_indexmin,for_9_indexmax=for_9_indexmax, for_10_indexmin=for_10_indexmin,for_10_indexmax=for_10_indexmax, for_3_flag=for_3_flag, for_4_flag=for_4_flag,for_5_flag=for_5_flag, for_6_flag=for_6_flag, for_7_flag=for_7_flag,for_8_flag=for_8_flag, for_9_flag=for_9_flag, for_10_flag=for_10_flag)
        else:
            self.for_3(pricemin=pricemin, pricemax=pricemax,mianjimin=mianjimin,mianjimax=mianjimax,louceng_xpath=louceng_xpath,louling_xpath=louling_xpath,for_3_buxian=for_3_buxian,for_4_buxian=for_4_buxian,for_5_buxian=for_5_buxian,for_6_buxian=for_6_buxian,for_7_buxian=for_7_buxian,for_8_buxian=for_8_buxian,fy_xpath_qian_li=fy_xpath_qian_li,fy_xpath_hou_li=fy_xpath_hou_li,page_url=page_url,shouye_handle=shouye_handle,for_3_list=for_3_list, for_4_list=for_4_list, for_5_list=for_5_list, for_6_list=for_6_list,for_7_list=for_7_list, for_8_list=for_8_list, for_9_list=for_9_list, for_10_list=for_10_list,for_3_indexmin=for_3_indexmin, for_3_indexmax=for_3_indexmax, for_4_indexmin=for_4_indexmin,for_4_indexmax=for_4_indexmax, for_5_indexmin=for_5_indexmin, for_5_indexmax=for_5_indexmax,for_6_indexmin=for_6_indexmin, for_6_indexmax=for_6_indexmax, for_7_indexmin=for_7_indexmin,for_7_indexmax=for_7_indexmax, for_8_indexmin=for_8_indexmin, for_8_indexmax=for_8_indexmax,for_9_indexmin=for_9_indexmin, for_9_indexmax=for_9_indexmax, for_10_indexmin=for_10_indexmin,for_10_indexmax=for_10_indexmax, for_3_flag=for_3_flag, for_4_flag=for_4_flag,for_5_flag=for_5_flag, for_6_flag=for_6_flag, for_7_flag=for_7_flag, for_8_flag=for_8_flag,for_9_flag=for_9_flag, for_10_flag=for_10_flag)

    shoujia_queding_loc = (By.ID, 'Sbtn')  # 售价自定义输入内容确定按钮
    def for_3(self,louceng_xpath,louling_xpath,fy_xpath_qian_li,fy_xpath_hou_li,shouye_handle,page_url,for_3_flag,for_4_flag,for_5_flag,for_6_flag,for_7_flag,for_8_flag,for_9_flag,for_10_flag,for_3_list,for_4_list,for_5_list,for_6_list,for_7_list,for_8_list,for_9_list,for_10_list,for_3_indexmin,for_3_indexmax,for_4_indexmin,for_4_indexmax,for_5_indexmin,for_5_indexmax, for_6_indexmin, for_6_indexmax,for_7_indexmin,for_7_indexmax,for_8_indexmin,for_8_indexmax, for_9_indexmin, for_9_indexmax,for_10_indexmin,for_10_indexmax,pricemin,pricemax,mianjimin,mianjimax,subwaylinesontext='',for_3_buxian='',for_4_buxian='',for_5_buxian='',for_6_buxian='',for_7_buxian='',for_8_buxian=''):
        if for_3_flag == True:  # for_3_flag，点击传入的售价标签，否则售价状态为不限
            for f3 in for_3_list[for_3_indexmin:for_3_indexmax]:  # [for_3_indexmin:for_3_indexmax]为售价要被点击的范围
                if (f3 == 'SB' and  pricemin != '') or (f3 == 'SE' and  pricemax != '') or (f3 == 'JGB' and  pricemax != '') or (f3 == 'JGE' and  pricemax != ''):  # 判断点击的售价是否是文本框，如果是分别输入最小最大值，如果不是，则点击已有的售价标签
                    if f3 == 'SB':  # 如果定位到最小值文本框，输入最小之后，结束本层循环
                        self.find_element(*(By.ID, f3)).send_keys(pricemin)
                        continue
                    else:
                        self.find_element(*(By.ID, f3)).send_keys(pricemax)
                    sleep(1)
                    self.find_element(*self.shoujia_queding_loc).click()  # 自定义文本框输入内容后点击确定按钮
                    if SearchCommon(self.driver).fangyuan_zongshu_ling(self.biaoqian()[0]) == False:  # 如果房源总数为零，判断房源为零时候的提示语，然后结束本层循环，不再执行后面的搜索
                        SearchCommon(self.driver).fangyuan_zongshu_ling_panduantishiyu(self.biaoqian()[1])
                        continue
                else:
                    self.find_element(*(By.ID, f3)).click()
                    sleep(1)
                    if SearchCommon(self.driver).fangyuan_zongshu_ling(self.biaoqian()[0]) == False:
                        SearchCommon(self.driver).fangyuan_zongshu_ling_panduantishiyu(self.biaoqian()[1])
                        continue
                self.for_4(mianjimin=mianjimin,mianjimax=mianjimax,louceng_xpath=louceng_xpath,louling_xpath=louling_xpath,for_4_buxian=for_4_buxian,for_5_buxian=for_5_buxian,for_6_buxian=for_6_buxian,for_7_buxian=for_7_buxian,for_8_buxian=for_8_buxian,fy_xpath_qian_li=fy_xpath_qian_li,fy_xpath_hou_li=fy_xpath_hou_li,subwaylinesontext=subwaylinesontext,shouye_handle=shouye_handle,page_url=page_url,for_4_list=for_4_list, for_5_list=for_5_list, for_6_list=for_6_list,for_7_list=for_7_list, for_8_list=for_8_list, for_9_list=for_9_list, for_10_list=for_10_list, for_4_indexmin=for_4_indexmin,for_4_indexmax=for_4_indexmax, for_5_indexmin=for_5_indexmin, for_5_indexmax=for_5_indexmax,for_6_indexmin=for_6_indexmin, for_6_indexmax=for_6_indexmax, for_7_indexmin=for_7_indexmin,for_7_indexmax=for_7_indexmax, for_8_indexmin=for_8_indexmin, for_8_indexmax=for_8_indexmax,for_9_indexmin=for_9_indexmin, for_9_indexmax=for_9_indexmax, for_10_indexmin=for_10_indexmin,for_10_indexmax=for_10_indexmax, for_4_flag=for_4_flag,for_5_flag=for_5_flag, for_6_flag=for_6_flag, for_7_flag=for_7_flag, for_8_flag=for_8_flag,for_9_flag=for_9_flag, for_10_flag=for_10_flag)
            if pricemin != '' or  pricemax != '':
                self.find_element(*(By.ID, for_3_list[0])).click()
            self.find_element(*(By.ID, for_3_buxian)).click()
        else:
            self.for_4(mianjimin=mianjimin,mianjimax=mianjimax,louceng_xpath=louceng_xpath,louling_xpath=louling_xpath,for_4_buxian=for_4_buxian,for_5_buxian=for_5_buxian,for_6_buxian=for_6_buxian,for_7_buxian=for_7_buxian,for_8_buxian=for_8_buxian,fy_xpath_qian_li=fy_xpath_qian_li,fy_xpath_hou_li=fy_xpath_hou_li,subwaylinesontext=subwaylinesontext,shouye_handle=shouye_handle,page_url=page_url,for_4_list=for_4_list, for_5_list=for_5_list, for_6_list=for_6_list, for_7_list=for_7_list,for_8_list=for_8_list, for_9_list=for_9_list, for_10_list=for_10_list,for_4_indexmin=for_4_indexmin, for_4_indexmax=for_4_indexmax, for_5_indexmin=for_5_indexmin,for_5_indexmax=for_5_indexmax, for_6_indexmin=for_6_indexmin, for_6_indexmax=for_6_indexmax,for_7_indexmin=for_7_indexmin, for_7_indexmax=for_7_indexmax, for_8_indexmin=for_8_indexmin,for_8_indexmax=for_8_indexmax, for_9_indexmin=for_9_indexmin, for_9_indexmax=for_9_indexmax,for_10_indexmin=for_10_indexmin, for_10_indexmax=for_10_indexmax, for_4_flag=for_4_flag,for_5_flag=for_5_flag, for_6_flag=for_6_flag, for_7_flag=for_7_flag, for_8_flag=for_8_flag,for_9_flag=for_9_flag, for_10_flag=for_10_flag)

    mianji_queding_loc = (By.ID, 'Abtn')  # 面积自定义输入内容确定按钮
    def for_4(self,louceng_xpath,louling_xpath,fy_xpath_qian_li,fy_xpath_hou_li,shouye_handle,page_url,for_4_flag,for_5_flag,for_6_flag,for_7_flag,for_8_flag,for_9_flag,for_10_flag,for_4_list,for_5_list,for_6_list,for_7_list,for_8_list,for_9_list,for_10_list,for_4_indexmin,for_4_indexmax,for_5_indexmin,for_5_indexmax, for_6_indexmin, for_6_indexmax,for_7_indexmin,for_7_indexmax,for_8_indexmin,for_8_indexmax, for_9_indexmin, for_9_indexmax,for_10_indexmin,for_10_indexmax,mianjimin,mianjimax,subwaylinesontext='',for_4_buxian='',for_5_buxian='',for_6_buxian='',for_7_buxian='',for_8_buxian=''):
        if for_4_flag == True:#如果for_4_flag为真，点击面积的所有标签，否则面积状态为不限
            for f4 in for_4_list[for_4_indexmin:for_4_indexmax]:#[for_4_indexmin:for_4_indexmax]要点击的面积标签范围
                if (f4 == 'AB' and  mianjimin != '') or (f4 == 'AE' and  mianjimax != '') or (f4 == 'JGB' and  mianjimax != '') or (f4 == 'JGE' and  mianjimax != ''):#判断定位的是否是自定义面积输入框，如果是则分别输入最小最大值
                    if f4 == 'AB':#如果是最小值文本框，输入面积最小值后，结束本层循环
                        self.find_element(*(By.ID, f4)).send_keys(mianjimin)
                        continue
                    else:
                        self.find_element(*(By.ID, f4)).send_keys(mianjimax)
                    sleep(1)
                    self.find_element(*self.mianji_queding_loc).click()#自定义文本框输入内容后点击确定按钮
                    if SearchCommon(self.driver).fangyuan_zongshu_ling(self.biaoqian()[0]) == False:
                        SearchCommon(self.driver).fangyuan_zongshu_ling_panduantishiyu(self.biaoqian()[1])
                        continue
                else:
                    self.find_element(*(By.ID, f4)).click()
                    sleep(1)
                    if SearchCommon(self.driver).fangyuan_zongshu_ling(self.biaoqian()[0]) == False:
                        SearchCommon(self.driver).fangyuan_zongshu_ling_panduantishiyu(self.biaoqian()[1])
                        continue
                self.for_5(louceng_xpath=louceng_xpath,louling_xpath=louling_xpath,for_5_buxian=for_5_buxian,for_6_buxian=for_6_buxian,for_7_buxian=for_7_buxian,for_8_buxian=for_8_buxian,fy_xpath_qian_li=fy_xpath_qian_li,fy_xpath_hou_li=fy_xpath_hou_li,subwaylinesontext=subwaylinesontext,shouye_handle=shouye_handle,page_url=page_url,for_5_list=for_5_list, for_6_list=for_6_list, for_7_list=for_7_list,for_8_list=for_8_list, for_9_list=for_9_list, for_10_list=for_10_list, for_5_indexmin=for_5_indexmin,for_5_indexmax=for_5_indexmax, for_6_indexmin=for_6_indexmin, for_6_indexmax=for_6_indexmax,for_7_indexmin=for_7_indexmin, for_7_indexmax=for_7_indexmax, for_8_indexmin=for_8_indexmin,for_8_indexmax=for_8_indexmax, for_9_indexmin=for_9_indexmin, for_9_indexmax=for_9_indexmax,for_10_indexmin=for_10_indexmin, for_10_indexmax=for_10_indexmax,for_5_flag=for_5_flag, for_6_flag=for_6_flag, for_7_flag=for_7_flag, for_8_flag=for_8_flag,for_9_flag=for_9_flag, for_10_flag=for_10_flag)
            if mianjimin != '' or  mianjimax != '':
                self.find_element(*(By.ID, for_4_list[0])).click()
            self.find_element(*(By.ID, for_4_buxian)).click()
        else:
            self.for_5(louceng_xpath=louceng_xpath,louling_xpath=louling_xpath,for_5_buxian=for_5_buxian,for_6_buxian=for_6_buxian,for_7_buxian=for_7_buxian,for_8_buxian=for_8_buxian,fy_xpath_qian_li=fy_xpath_qian_li,fy_xpath_hou_li=fy_xpath_hou_li,subwaylinesontext=subwaylinesontext,shouye_handle=shouye_handle,page_url=page_url,for_5_list=for_5_list, for_6_list=for_6_list, for_7_list=for_7_list, for_8_list=for_8_list,for_9_list=for_9_list, for_10_list=for_10_list, for_5_indexmin=for_5_indexmin,for_5_indexmax=for_5_indexmax, for_6_indexmin=for_6_indexmin, for_6_indexmax=for_6_indexmax,for_7_indexmin=for_7_indexmin, for_7_indexmax=for_7_indexmax, for_8_indexmin=for_8_indexmin,for_8_indexmax=for_8_indexmax, for_9_indexmin=for_9_indexmin, for_9_indexmax=for_9_indexmax,for_10_indexmin=for_10_indexmin, for_10_indexmax=for_10_indexmax, for_5_flag=for_5_flag,for_6_flag=for_6_flag, for_7_flag=for_7_flag, for_8_flag=for_8_flag, for_9_flag=for_9_flag,for_10_flag=for_10_flag)


    def for_5(self,louceng_xpath,louling_xpath,fy_xpath_qian_li,fy_xpath_hou_li,shouye_handle,page_url,for_5_flag,for_6_flag,for_7_flag,for_8_flag,for_9_flag,for_10_flag,for_5_list,for_6_list,for_7_list,for_8_list,for_9_list,for_10_list,for_5_indexmin,for_5_indexmax, for_6_indexmin, for_6_indexmax,for_7_indexmin,for_7_indexmax,for_8_indexmin,for_8_indexmax, for_9_indexmin, for_9_indexmax,for_10_indexmin,for_10_indexmax,subwaylinesontext='',for_5_buxian='',for_6_buxian='',for_7_buxian='',for_8_buxian=''):
        if for_5_flag == True:  # 如果for_5_flag标识为真，点击所有标签，否则状态为不限
            for f5 in for_5_list[for_5_indexmin:for_5_indexmax]:  # 要点击的范围
                self.find_element(*(By.ID, f5)).click()
                sleep(1)
                if SearchCommon(self.driver).fangyuan_zongshu_ling(self.biaoqian()[0]) == False:
                    SearchCommon(self.driver).fangyuan_zongshu_ling_panduantishiyu(self.biaoqian()[1])
                    continue
                self.for_6(louceng_xpath=louceng_xpath,louling_xpath=louling_xpath,for_6_buxian=for_6_buxian,for_7_buxian=for_7_buxian,for_8_buxian=for_8_buxian,fy_xpath_qian_li=fy_xpath_qian_li,fy_xpath_hou_li=fy_xpath_hou_li,subwaylinesontext=subwaylinesontext,shouye_handle=shouye_handle,page_url=page_url,for_6_list=for_6_list, for_7_list=for_7_list, for_8_list=for_8_list,for_9_list=for_9_list, for_10_list=for_10_list, for_6_indexmin=for_6_indexmin, for_6_indexmax=for_6_indexmax,for_7_indexmin=for_7_indexmin, for_7_indexmax=for_7_indexmax, for_8_indexmin=for_8_indexmin,for_8_indexmax=for_8_indexmax, for_9_indexmin=for_9_indexmin, for_9_indexmax=for_9_indexmax,for_10_indexmin=for_10_indexmin, for_10_indexmax=for_10_indexmax,for_6_flag=for_6_flag, for_7_flag=for_7_flag, for_8_flag=for_8_flag, for_9_flag=for_9_flag,for_10_flag=for_10_flag)
            self.find_element(*(By.ID, for_5_buxian)).click()
        else:
            self.for_6(louceng_xpath=louceng_xpath,louling_xpath=louling_xpath,for_6_buxian=for_6_buxian,for_7_buxian=for_7_buxian,for_8_buxian=for_8_buxian,fy_xpath_qian_li=fy_xpath_qian_li,fy_xpath_hou_li=fy_xpath_hou_li,subwaylinesontext=subwaylinesontext,shouye_handle=shouye_handle,page_url=page_url,for_6_list=for_6_list, for_7_list=for_7_list, for_8_list=for_8_list, for_9_list=for_9_list,for_10_list=for_10_list, for_6_indexmin=for_6_indexmin, for_6_indexmax=for_6_indexmax,for_7_indexmin=for_7_indexmin, for_7_indexmax=for_7_indexmax, for_8_indexmin=for_8_indexmin,for_8_indexmax=for_8_indexmax, for_9_indexmin=for_9_indexmin, for_9_indexmax=for_9_indexmax,for_10_indexmin=for_10_indexmin, for_10_indexmax=for_10_indexmax, for_6_flag=for_6_flag,for_7_flag=for_7_flag, for_8_flag=for_8_flag, for_9_flag=for_9_flag, for_10_flag=for_10_flag)

    def for_6(self,louceng_xpath,louling_xpath,fy_xpath_qian_li,fy_xpath_hou_li,shouye_handle,page_url,for_6_flag,for_7_flag,for_8_flag,for_9_flag,for_10_flag,for_6_list,for_7_list,for_8_list,for_9_list,for_10_list, for_6_indexmin, for_6_indexmax,for_7_indexmin,for_7_indexmax,for_8_indexmin,for_8_indexmax, for_9_indexmin, for_9_indexmax,for_10_indexmin,for_10_indexmax,subwaylinesontext='',for_6_buxian='',for_7_buxian='',for_8_buxian=''):
        if for_6_flag == True:
            for f6 in for_6_list[for_6_indexmin:for_6_indexmax]:
                self.find_element(*(By.ID, f6)).click()
                sleep(1)
                if SearchCommon(self.driver).fangyuan_zongshu_ling(self.biaoqian()[0]) == False:
                    SearchCommon(self.driver).fangyuan_zongshu_ling_panduantishiyu(self.biaoqian()[1])
                    continue
                self.for_7(louceng_xpath=louceng_xpath,louling_xpath=louling_xpath,for_7_buxian=for_7_buxian,for_8_buxian=for_8_buxian,fy_xpath_qian_li=fy_xpath_qian_li,fy_xpath_hou_li=fy_xpath_hou_li,subwaylinesontext=subwaylinesontext,shouye_handle=shouye_handle,page_url=page_url,for_7_list=for_7_list, for_8_list=for_8_list, for_9_list=for_9_list,for_10_list=for_10_list,for_7_indexmin=for_7_indexmin, for_7_indexmax=for_7_indexmax, for_8_indexmin=for_8_indexmin,for_8_indexmax=for_8_indexmax, for_9_indexmin=for_9_indexmin, for_9_indexmax=for_9_indexmax,for_10_indexmin=for_10_indexmin, for_10_indexmax=for_10_indexmax,for_7_flag=for_7_flag, for_8_flag=for_8_flag, for_9_flag=for_9_flag, for_10_flag=for_10_flag)
            self.find_element(*(By.ID, for_6_buxian)).click()
        else:
            self.for_7(louceng_xpath=louceng_xpath,louling_xpath=louling_xpath,for_7_buxian=for_7_buxian,for_8_buxian=for_8_buxian,fy_xpath_qian_li=fy_xpath_qian_li,fy_xpath_hou_li=fy_xpath_hou_li,subwaylinesontext=subwaylinesontext,shouye_handle=shouye_handle,page_url=page_url,for_7_list=for_7_list, for_8_list=for_8_list, for_9_list=for_9_list,for_10_list=for_10_list,for_7_indexmin=for_7_indexmin, for_7_indexmax=for_7_indexmax, for_8_indexmin=for_8_indexmin,for_8_indexmax=for_8_indexmax, for_9_indexmin=for_9_indexmin, for_9_indexmax=for_9_indexmax,for_10_indexmin=for_10_indexmin, for_10_indexmax=for_10_indexmax,for_7_flag=for_7_flag, for_8_flag=for_8_flag, for_9_flag=for_9_flag, for_10_flag=for_10_flag)

    def for_7(self,louceng_xpath,louling_xpath,fy_xpath_qian_li,fy_xpath_hou_li,page_url,shouye_handle,for_7_flag,for_8_flag,for_9_flag,for_10_flag,for_7_list,for_8_list,for_9_list,for_10_list,for_7_indexmin,for_7_indexmax,for_8_indexmin,for_8_indexmax, for_9_indexmin, for_9_indexmax,for_10_indexmin,for_10_indexmax,subwaylinesontext='',for_7_buxian='',for_8_buxian=''):
        if for_7_flag == True:
            for f7 in for_7_list[for_7_indexmin:for_7_indexmax]:
                self.find_element(*(By.ID, f7)).click()
                sleep(1)
                if SearchCommon(self.driver).fangyuan_zongshu_ling(self.biaoqian()[0]) == False:
                    SearchCommon(self.driver).fangyuan_zongshu_ling_panduantishiyu(self.biaoqian()[1])
                    continue
                self.for_8(louceng_xpath=louceng_xpath,louling_xpath=louling_xpath,for_8_buxian=for_8_buxian,fy_xpath_qian_li=fy_xpath_qian_li,fy_xpath_hou_li=fy_xpath_hou_li,subwaylinesontext=subwaylinesontext,shouye_handle=shouye_handle,page_url=page_url,for_8_list=for_8_list, for_9_list=for_9_list,for_10_list=for_10_list, for_8_indexmin=for_8_indexmin,for_8_indexmax=for_8_indexmax, for_9_indexmin=for_9_indexmin, for_9_indexmax=for_9_indexmax,for_10_indexmin=for_10_indexmin, for_10_indexmax=for_10_indexmax,for_8_flag=for_8_flag, for_9_flag=for_9_flag, for_10_flag=for_10_flag)
            self.find_element(*(By.ID, for_7_buxian)).click()
        else:
            self.for_8(louceng_xpath=louceng_xpath,louling_xpath=louling_xpath,for_8_buxian=for_8_buxian,fy_xpath_qian_li=fy_xpath_qian_li,fy_xpath_hou_li=fy_xpath_hou_li,subwaylinesontext=subwaylinesontext,shouye_handle=shouye_handle,page_url=page_url,for_8_list=for_8_list, for_9_list=for_9_list,for_10_list=for_10_list,for_8_indexmin=for_8_indexmin,for_8_indexmax=for_8_indexmax, for_9_indexmin=for_9_indexmin, for_9_indexmax=for_9_indexmax,for_10_indexmin=for_10_indexmin, for_10_indexmax=for_10_indexmax,for_8_flag=for_8_flag, for_9_flag=for_9_flag, for_10_flag=for_10_flag)

    def for_8(self,louceng_xpath,louling_xpath,fy_xpath_qian_li,fy_xpath_hou_li,shouye_handle,page_url,for_8_flag,for_9_flag,for_10_flag,for_8_list,for_9_list,for_10_list,for_8_indexmin,for_8_indexmax, for_9_indexmin, for_9_indexmax,for_10_indexmin,for_10_indexmax,subwaylinesontext='',for_8_buxian=''):
        if for_8_flag == True:
            for f8 in for_8_list[for_8_indexmin:for_8_indexmax]:
                self.find_element(*(By.ID, f8)).click()
                sleep(1)
                if SearchCommon(self.driver).fangyuan_zongshu_ling(self.biaoqian()[0]) == False:
                    SearchCommon(self.driver).fangyuan_zongshu_ling_panduantishiyu(self.biaoqian()[1])
                    self.find_element(*(By.ID, for_8_buxian)).click()
                    continue
                self.for_9(louceng_xpath=louceng_xpath,louling_xpath=louling_xpath,fy_xpath_qian_li=fy_xpath_qian_li,fy_xpath_hou_li=fy_xpath_hou_li,subwaylinesontext=subwaylinesontext,shouye_handle=shouye_handle,page_url=page_url,for_9_list=for_9_list,for_10_list=for_10_list, for_9_indexmin=for_9_indexmin, for_9_indexmax=for_9_indexmax,for_10_indexmin=for_10_indexmin, for_10_indexmax=for_10_indexmax, for_9_flag=for_9_flag, for_10_flag=for_10_flag)
                self.find_element(*(By.ID, for_8_buxian)).click()
            self.find_element(*(By.ID, for_8_buxian)).click()
        else:
            self.for_9(louceng_xpath=louceng_xpath,louling_xpath=louling_xpath,fy_xpath_qian_li=fy_xpath_qian_li,fy_xpath_hou_li=fy_xpath_hou_li,subwaylinesontext=subwaylinesontext,shouye_handle=shouye_handle,page_url=page_url,for_9_list=for_9_list,for_10_list=for_10_list, for_9_indexmin=for_9_indexmin, for_9_indexmax=for_9_indexmax,for_10_indexmin=for_10_indexmin, for_10_indexmax=for_10_indexmax,for_9_flag=for_9_flag, for_10_flag=for_10_flag)

    def for_9(self,louceng_xpath,louling_xpath,fy_xpath_qian_li,fy_xpath_hou_li,shouye_handle,page_url, for_9_flag, for_10_flag, for_9_list, for_10_list, for_9_indexmin, for_9_indexmax, for_10_indexmin, for_10_indexmax,subwaylinesontext=''):
        if for_9_flag == True and louceng_xpath != '' :
            for f9 in for_9_list[for_9_indexmin:for_9_indexmax]:
                loucengindex = for_9_list.index(f9)
                self.louceng_loc = (By.XPATH,louceng_xpath)
                self.script(self.find_element(*self.louceng_loc))
                ActionChains(self.driver).double_click(self.find_element(*self.louceng_loc)).perform()
                self.find_element(*(By.XPATH, f9)).click()
                sleep(1)
                if SearchCommon(self.driver).fangyuan_zongshu_ling(self.biaoqian()[0]) == False:
                    SearchCommon(self.driver).fangyuan_zongshu_ling_panduantishiyu(self.biaoqian()[1])
                    continue
                self.for_10(louling_xpath=louling_xpath,fy_xpath_qian_li=fy_xpath_qian_li,fy_xpath_hou_li=fy_xpath_hou_li,subwaylinesontext=subwaylinesontext,shouye_handle=shouye_handle,page_url=page_url,for_10_list=for_10_list,for_10_indexmin=for_10_indexmin, for_10_indexmax=for_10_indexmax, for_10_flag=for_10_flag)
                if loucengindex == len(for_9_list) - 1:
                    self.louceng_loc = (By.XPATH, louceng_xpath)
                    self.script(self.find_element(*self.louceng_loc))
                    ActionChains(self.driver).double_click(self.find_element(*self.louceng_loc)).perform()
                    self.find_element(*(By.XPATH, for_9_list[0])).click()
        elif for_9_flag == True and louceng_xpath == '':
            for f9 in for_9_list[for_9_indexmin:for_9_indexmax]:  # 要点击的范围
                self.find_element(*(By.ID, f9)).click()
                sleep(1)
                if SearchCommon(self.driver).fangyuan_zongshu_ling(self.biaoqian()[0]) == False:
                    SearchCommon(self.driver).fangyuan_zongshu_ling_panduantishiyu(self.biaoqian()[1])
                    continue
                self.for_10(louling_xpath=louling_xpath, fy_xpath_qian_li=fy_xpath_qian_li,fy_xpath_hou_li=fy_xpath_hou_li, subwaylinesontext=subwaylinesontext,shouye_handle=shouye_handle, page_url=page_url, for_10_list=for_10_list,for_10_indexmin=for_10_indexmin, for_10_indexmax=for_10_indexmax, for_10_flag=for_10_flag)
            self.find_element(*(By.ID,'Z0')).click()
        else:
            self.for_10(louling_xpath=louling_xpath,fy_xpath_qian_li=fy_xpath_qian_li,fy_xpath_hou_li=fy_xpath_hou_li,subwaylinesontext=subwaylinesontext,shouye_handle=shouye_handle,page_url=page_url,for_10_list=for_10_list,for_10_indexmin=for_10_indexmin, for_10_indexmax=for_10_indexmax,for_10_flag=for_10_flag)

    def for_10(self,louling_xpath,fy_xpath_qian_li,fy_xpath_hou_li,shouye_handle,page_url,for_10_flag, for_10_list,for_10_indexmin, for_10_indexmax,subwaylinesontext=''):
        if for_10_flag == True and louling_xpath != '':
            for f10 in for_10_list[for_10_indexmin:for_10_indexmax]:
                loulingindex = for_10_list.index(f10)
                self.louling_loc = (By.XPATH, louling_xpath)
                self.script(self.find_element(*self.louling_loc))
                ActionChains(self.driver).double_click(self.find_element(*self.louling_loc)).perform()
                self.find_element(*(By.XPATH, f10)).click()
                sleep(1)
                if SearchCommon(self.driver).fangyuan_zongshu_ling(self.biaoqian()[0]) == False:
                    SearchCommon(self.driver).fangyuan_zongshu_ling_panduantishiyu(self.biaoqian()[1])
                    continue
                SearchCommon(self.driver).panduan_sousuo(fangyuan_url=page_url,shouye_handle=shouye_handle, subwaylinesontext=subwaylinesontext,fangyaunzongshu_xpath=self.biaoqian()[0],fangyuanliebiao_className=self.biaoqian()[2],jiansuoneirong_ID=self.biaoqian()[3],fy_xpath_qian_li=fy_xpath_qian_li,fy_xpath_hou_li=fy_xpath_hou_li)
                if loulingindex == len(for_10_list) - 1:
                    self.louling_loc = (By.XPATH, louling_xpath)
                    self.script(self.find_element(*self.louling_loc))
                    ActionChains(self.driver).double_click(self.find_element(*self.louling_loc)).perform()
                    self.find_element(*(By.XPATH, for_10_list[0])).click()
        elif for_10_flag == True and louling_xpath == '':
            for f10 in for_10_list[for_10_indexmin:for_10_indexmax]:  # 要点击的范围
                self.find_element(*(By.ID, f10)).click()
                sleep(1)
                if SearchCommon(self.driver).fangyuan_zongshu_ling(self.biaoqian()[0]) == False:
                    SearchCommon(self.driver).fangyuan_zongshu_ling_panduantishiyu(self.biaoqian()[1])
                    continue
                SearchCommon(self.driver).panduan_sousuo(fangyuan_url=page_url, shouye_handle=shouye_handle,subwaylinesontext=subwaylinesontext,fangyaunzongshu_xpath=self.biaoqian()[0],fangyuanliebiao_className=self.biaoqian()[2],jiansuoneirong_ID=self.biaoqian()[3],fy_xpath_qian_li=fy_xpath_qian_li,fy_xpath_hou_li=fy_xpath_hou_li)
            self.find_element(*(By.ID,'F0')).click()
        else:
            SearchCommon(self.driver).panduan_sousuo(fangyuan_url=page_url, shouye_handle=shouye_handle,subwaylinesontext=subwaylinesontext,fangyaunzongshu_xpath=self.biaoqian()[0],fangyuanliebiao_className=self.biaoqian()[2],jiansuoneirong_ID=self.biaoqian()[3],fy_xpath_qian_li=fy_xpath_qian_li,fy_xpath_hou_li=fy_xpath_hou_li)

    #统一调用
    def tongyidiaoyong(self,cityname,leixing,fy_xpath_qian_li,fy_xpath_hou_li,subway_f='',subway_f_xpath='',pricemin='', pricemax='',mianjimin='',mianjimax='',for_1_range='',louceng_xpath='',louling_xpath='',for_1_2_index='',for_1_list='',for_2_list='',for_3_list='',for_4_list='',for_5_list='',for_6_list='',for_7_list='',for_8_list='',for_9_list='',for_10_list='',for_1_indexmin=0,for_1_indexmax=100,for_2_indexmin=0,for_2_indexmax=100,for_3_indexmin=0,for_3_indexmax=100,for_4_indexmin=0,for_4_indexmax=100,for_5_indexmin=0,for_5_indexmax=100, for_6_indexmin=0, for_6_indexmax=100,for_7_indexmin=0,for_7_indexmax=100,for_8_indexmin=0,for_8_indexmax=100, for_9_indexmin=0, for_9_indexmax=100,for_10_indexmin=0,for_10_indexmax=100,for_1_flag=True,for_2_flag=True,for_3_flag=True,for_4_flag=True,for_5_flag=True,for_6_flag=True,for_7_flag=True,for_8_flag=True,for_9_flag=True,for_10_flag=True,for_3_buxian='',for_4_buxian='',for_5_buxian='',for_6_buxian='',for_7_buxian='',for_8_buxian=''):
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
        elif leixing == '别墅':
            SelectCity(self.driver).bieshu()  # 点击别墅
        sleep(2)
        self.all_handle = self.driver.window_handles
        for self.handle in self.all_handle:
            if len(self.all_handle) == 1:
                page_url = self.driver.current_url
                if subway_f == '地铁房':
                    self.find_element(*(By.XPATH,subway_f_xpath)).click()
                    sleep(1)
                self.for_1(pricemin=pricemin, pricemax=pricemax, mianjimin=mianjimin, mianjimax=mianjimax,louceng_xpath=louceng_xpath, louling_xpath=louling_xpath, for_3_buxian=for_3_buxian,for_4_buxian=for_4_buxian, for_5_buxian=for_5_buxian, for_6_buxian=for_6_buxian,for_7_buxian=for_7_buxian, for_8_buxian=for_8_buxian, fy_xpath_qian_li=fy_xpath_qian_li,fy_xpath_hou_li=fy_xpath_hou_li, page_url=page_url, shouye_handle=self.shouye_handle,for_1_range=for_1_range, for_1_list=for_1_list, for_2_list=for_2_list, for_3_list=for_3_list,for_4_list=for_4_list, for_5_list=for_5_list, for_6_list=for_6_list, for_7_list=for_7_list,for_8_list=for_8_list, for_9_list=for_9_list, for_10_list=for_10_list,for_1_indexmin=for_1_indexmin, for_1_indexmax=for_1_indexmax, for_2_indexmin=for_2_indexmin,for_2_indexmax=for_2_indexmax, for_3_indexmin=for_3_indexmin, for_3_indexmax=for_3_indexmax,for_4_indexmin=for_4_indexmin, for_4_indexmax=for_4_indexmax, for_5_indexmin=for_5_indexmin,for_5_indexmax=for_5_indexmax, for_6_indexmin=for_6_indexmin, for_6_indexmax=for_6_indexmax,for_7_indexmin=for_7_indexmin, for_7_indexmax=for_7_indexmax, for_8_indexmin=for_8_indexmin,for_8_indexmax=for_8_indexmax, for_9_indexmin=for_9_indexmin, for_9_indexmax=for_9_indexmax,for_10_indexmin=for_10_indexmin, for_10_indexmax=for_10_indexmax,for_1_2_index=for_1_2_index, for_1_flag=for_1_flag, for_2_flag=for_2_flag,for_3_flag=for_3_flag, for_4_flag=for_4_flag, for_5_flag=for_5_flag, for_6_flag=for_6_flag,for_7_flag=for_7_flag, for_8_flag=for_8_flag, for_9_flag=for_9_flag, for_10_flag=for_10_flag)
            else:
                if self.handle != self.shouye_handle:
                    self.driver.switch_to.window(self.handle)
                    page_url = self.driver.current_url
                    if subway_f == '地铁房':
                        self.find_element(*(By.XPATH, subway_f_xpath)).click()
                        sleep(1)
                    self.for_1(pricemin=pricemin, pricemax=pricemax,mianjimin=mianjimin,mianjimax=mianjimax,louceng_xpath=louceng_xpath,louling_xpath=louling_xpath,for_3_buxian=for_3_buxian,for_4_buxian=for_4_buxian,for_5_buxian=for_5_buxian,for_6_buxian=for_6_buxian,for_7_buxian=for_7_buxian,for_8_buxian=for_8_buxian,fy_xpath_qian_li=fy_xpath_qian_li,fy_xpath_hou_li=fy_xpath_hou_li,page_url=page_url,shouye_handle=self.shouye_handle,for_1_range=for_1_range,for_1_list=for_1_list,for_2_list=for_2_list,for_3_list=for_3_list,for_4_list=for_4_list,for_5_list=for_5_list,for_6_list=for_6_list,for_7_list=for_7_list,for_8_list=for_8_list,for_9_list=for_9_list,for_10_list=for_10_list,for_1_indexmin=for_1_indexmin,for_1_indexmax=for_1_indexmax,for_2_indexmin=for_2_indexmin,for_2_indexmax=for_2_indexmax,for_3_indexmin=for_3_indexmin,for_3_indexmax=for_3_indexmax,for_4_indexmin=for_4_indexmin,for_4_indexmax=for_4_indexmax,for_5_indexmin=for_5_indexmin,for_5_indexmax=for_5_indexmax, for_6_indexmin=for_6_indexmin, for_6_indexmax=for_6_indexmax,for_7_indexmin=for_7_indexmin,for_7_indexmax=for_7_indexmax,for_8_indexmin=for_8_indexmin,for_8_indexmax=for_8_indexmax, for_9_indexmin=for_9_indexmin, for_9_indexmax=for_9_indexmax,for_10_indexmin=for_10_indexmin,for_10_indexmax=for_10_indexmax,for_1_2_index=for_1_2_index,for_1_flag=for_1_flag,for_2_flag=for_2_flag,for_3_flag=for_3_flag,for_4_flag=for_4_flag,for_5_flag=for_5_flag,for_6_flag=for_6_flag,for_7_flag=for_7_flag,for_8_flag=for_8_flag,for_9_flag=for_9_flag,for_10_flag=for_10_flag)


#厦门---二手房---区域、商圈
XM_ErShouFang_QuYu = Data.XM_ErShouFang_QuYu
XM_ErShouFang_ShangQuan = Data.XM_ErShouFang_ShangQuan
XM_ErShouFang_ShangQuan_index = Data.XM_ErShouFang_ShangQuan_index
#厦门---二手房---售价
XM_ErShouFang_ShouJia = Data.XM_ErShouFang_ShouJia
#厦门---二手房---面积
XM_ErShouFang_MianJi = Data.XM_ErShouFang_MianJi
#厦门---二手房---户型
XM_ErShouFang_HuXing = Data.XM_ErShouFang_HuXing
#厦门---二手房---电梯
XM_ErShouFang_DianTi = Data.XM_ErShouFang_DianTi
#厦门---二手房---装修
XM_ErShouFang_ZhuangXiu = Data.XM_ErShouFang_ZhuangXiu
#厦门---二手房---卖点
XM_ErShouFang_MaiDian = Data.XM_ErShouFang_MaiDian
#厦门---二手房---楼层
XM_ErShouFang_LouCeng = Data.XM_ErShouFang_LouCeng
#厦门---二手房---楼龄
XM_ErShouFang_LouLing = Data.XM_ErShouFang_LouLing

if __name__=="__main__":
    from selenium import webdriver
    import data.urldata as URL

    driver = webdriver.Chrome()
    url = URL.maitian_online_url
    driver.get(url)
    # driver.get('http://bj-test.imtfc.com/esfway/B1D1/T3L1')
    driver.implicitly_wait(2)
    driver.maximize_window()

    linkindex = []
    for i, line in enumerate(XM_ErShouFang_QuYu):
        linkindex.append(i)
    For_BianLi(driver).tongyidiaoyong(
        cityname=2, leixing='二手房',
        fy_xpath_qian_li='//div[@class="list_wrap"]/ul/li[', fy_xpath_hou_li=']/div[2]/h1/a',
        for_1_range=linkindex,
        louceng_xpath='/html/body/section[2]/div[1]/div[2]/div[8]/div[1]/a',
        louling_xpath='/html/body/section[2]/div[1]/div[2]/div[8]/div[2]/a',
        pricemin=0, pricemax=100, mianjimin=20, mianjimax=90,
        for_1_2_index=XM_ErShouFang_ShangQuan_index,
        for_1_list=XM_ErShouFang_QuYu, for_2_list=XM_ErShouFang_ShangQuan,
        for_3_list=XM_ErShouFang_ShouJia, for_4_list=XM_ErShouFang_MianJi,
        for_5_list=XM_ErShouFang_HuXing, for_6_list=XM_ErShouFang_DianTi,
        for_7_list=XM_ErShouFang_ZhuangXiu, for_8_list=XM_ErShouFang_MaiDian,
        for_9_list=XM_ErShouFang_LouCeng, for_10_list=XM_ErShouFang_LouLing,
        for_1_indexmin=0, for_1_indexmax=len(XM_ErShouFang_QuYu),
        for_2_indexmin=0, for_2_indexmax=len(XM_ErShouFang_ShangQuan),
        for_3_indexmin=0, for_3_indexmax=len(XM_ErShouFang_ShouJia),
        for_4_indexmin=0, for_4_indexmax=len(XM_ErShouFang_MianJi),
        for_5_indexmin=0, for_5_indexmax=len(XM_ErShouFang_HuXing),
        for_6_indexmin=0, for_6_indexmax=len(XM_ErShouFang_DianTi),
        for_7_indexmin=0, for_7_indexmax=len(XM_ErShouFang_ZhuangXiu),
        for_8_indexmin=0, for_8_indexmax=len(XM_ErShouFang_MaiDian),
        for_9_indexmin=0, for_9_indexmax=len(XM_ErShouFang_LouCeng),
        for_10_indexmin=0, for_10_indexmax=len(XM_ErShouFang_LouLing),
        for_1_flag=True, for_2_flag=True, for_3_flag=True, for_4_flag=True, for_5_flag=True,
        for_6_flag=True, for_7_flag=True, for_8_flag=True, for_9_flag=True, for_10_flag=True,
        for_3_buxian='S0', for_4_buxian='A0', for_5_buxian='H0',
        for_6_buxian='DT2', for_7_buxian='ZX0', for_8_buxian='T0')