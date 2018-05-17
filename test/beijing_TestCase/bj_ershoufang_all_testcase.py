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

import data.shhdata as Data
from test.common_package import myunit
from test.common_package.bj_fz_xm_for_bianli import For_BianLi

#北京---二手房---区域、商圈
BJ_ErShouFang_QuYu = Data.BJ_ErShouFang_QuYu
BJ_ErShouFang_ShangQuan = Data.BJ_ErShouFang_ShangQuan
BJ_ErShouFang_ShangQuan_index = Data.BJ_ErShouFang_ShangQuan_index
#北京---二手房---售价
BJ_ErShouFang_ShouJia = Data.BJ_ErShouFang_ShouJia
#北京---二手房---面积
BJ_ErShouFang_MianJi = Data.BJ_ErShouFang_MianJi
#北京---二手房---户型
BJ_ErShouFang_HuXing = Data.BJ_ErShouFang_HuXing
#北京---二手房---朝向
BJ_ErShouFang_ChaoXiang = Data.BJ_ErShouFang_ChaoXiang
#北京---二手房---卖点
BJ_ErShouFang_MaiDian = Data.BJ_ErShouFang_MaiDian
#北京---二手房---楼层
BJ_ErShouFang_LouCeng = Data.BJ_ErShouFang_LouCeng

class Bj_ErShouFang(myunit.MyTest):
    # 单元测试时使用
    #def __init__(self, driver):
     #   self.driver = driver

    def __test(self,for_1_flag, for_2_flag, for_3_flag, for_4_flag, for_5_flag,for_6_flag, for_7_flag, for_8_flag, for_9_flag, for_10_flag):
        linkindex = []
        for i, line in enumerate(BJ_ErShouFang_QuYu):
            linkindex.append(i)
        For_BianLi(self.driver).tongyidiaoyong(
            cityname=0, leixing='二手房',
            fy_xpath_qian_li='//div[@class="list_wrap"]/ul/li[', fy_xpath_hou_li=']/div[2]/h1/a',
            for_1_range=linkindex,
            louceng_xpath='/html/body/section[2]/div[1]/div[2]/div[7]/div[1]/a',
            pricemin=0, pricemax=100, mianjimin=20, mianjimax=90,
            for_1_2_index=BJ_ErShouFang_ShangQuan_index,
            for_1_list=BJ_ErShouFang_QuYu, for_2_list=BJ_ErShouFang_ShangQuan,
            for_3_list=BJ_ErShouFang_ShouJia, for_4_list=BJ_ErShouFang_MianJi,
            for_5_list=BJ_ErShouFang_HuXing, for_6_list=BJ_ErShouFang_ChaoXiang,
            for_8_list=BJ_ErShouFang_MaiDian, for_9_list=BJ_ErShouFang_LouCeng,
            for_1_indexmin=0, for_1_indexmax=len(BJ_ErShouFang_QuYu),
            for_2_indexmin=0, for_2_indexmax=len(BJ_ErShouFang_ShangQuan),
            for_3_indexmin=0, for_3_indexmax=len(BJ_ErShouFang_ShouJia),
            for_4_indexmin=0, for_4_indexmax=len(BJ_ErShouFang_MianJi),
            for_5_indexmin=0, for_5_indexmax=len(BJ_ErShouFang_HuXing),
            for_6_indexmin=0, for_6_indexmax=len(BJ_ErShouFang_ChaoXiang),
            for_8_indexmin=0, for_8_indexmax=len(BJ_ErShouFang_MaiDian),
            for_9_indexmin=0, for_9_indexmax=len(BJ_ErShouFang_LouCeng),
            for_1_flag=for_1_flag, for_2_flag=for_2_flag, for_3_flag=for_3_flag,
            for_4_flag=for_4_flag, for_5_flag=for_5_flag,for_6_flag=for_6_flag,
            for_7_flag=for_7_flag, for_8_flag=for_8_flag, for_9_flag=for_9_flag,
            for_10_flag=for_10_flag,
            for_3_buxian='S0', for_4_buxian='A0', for_5_buxian='H0',
            for_6_buxian='O0', for_8_buxian='T0')

    def test_1(self):
        '''遍历每一个查询条件，校验房源详情'''
        self.__test(
            for_1_flag=True, for_2_flag=True, for_3_flag=True, for_4_flag=True, for_5_flag=True,
            for_6_flag=True, for_7_flag=False, for_8_flag=True, for_9_flag=True, for_10_flag=False
        )

    def test_2(self):
        '''只遍历区域'''
        self.__test(
            for_1_flag=True,for_2_flag=False,for_3_flag=False,for_4_flag=False,for_5_flag=False,
            for_6_flag=False,for_7_flag=False,for_8_flag=False,for_9_flag=False,for_10_flag=False
        )

    def test_3(self):
        '''只遍历面积'''
        self.__test(
            for_1_flag=False,for_2_flag=False,for_3_flag=True,for_4_flag=True,for_5_flag=False,
            for_6_flag=False,for_7_flag=False,for_8_flag=False,for_9_flag=False,for_10_flag=False
        )

    def test_4(self):
        '''只遍历户型'''
        self.__test(
            for_1_flag=False,for_2_flag=False,for_3_flag=False,for_4_flag=False,for_5_flag=True,
            for_6_flag=False,for_7_flag=False,for_8_flag=False,for_9_flag=False,for_10_flag=False
        )

if __name__=="__main__":
    from selenium import webdriver
    import data.urldata as URL

    driver = webdriver.Chrome()
    url = URL.maitian_online_url
    driver.get(url)
    # driver.get('http://bj-test.imtfc.com/esfway/B1D1/T3L1')
    driver.implicitly_wait(2)
    driver.maximize_window()
    Bj_ErShouFang(driver).test_4()
