#!/usr/bin/python
# -*- coding:UTF-8 -*-
import data.shhdata as Data
from test.common_package import myunit
from test.common_package.bj_fz_xm_for_bianli import For_BianLi

#北京---二手房---地铁房线路、站台
BJ_ErShouFang_SubWayLine = Data.BJ_ErShouFang_SubWayLine
BJ_ErShouFang_SubWayLine_ZhanTai = Data.BJ_ErShouFang_SubWayLine_ZhanTai
BJ_ErShouFang_SubWayLine_ZhanTai_index = Data.BJ_ErShouFang_SubWayLine_ZhanTai_index
#北京---二手房---地铁房---售价标签ID
BJ_ErShouFang_SubWay_ShouJia = Data.BJ_ErShouFang_SubWay_ShouJia
#北京---二手房---地铁房---面积标签ID
BJ_ErShouFang_SubWay_MianJi = Data.BJ_ErShouFang_SubWay_MianJi
#北京---二手房---地铁房---户型标签ID
BJ_ErShouFang_SubWay_HuXing = Data.BJ_ErShouFang_SubWay_HuXing
#北京---二手房---地铁房---朝向标签ID
BJ_ErShouFang_SubWay_ChaoXiang = Data.BJ_ErShouFang_SubWay_ChaoXiang
#北京---二手房---地铁房---卖点标签ID
BJ_ErShouFang_SubWay_MaiDian = Data.BJ_ErShouFang_SubWay_MaiDian
#北京---二手房---地铁房---楼层Xpath
BJ_ErShouFang_SubWay_LouCeng = Data.BJ_ErShouFang_SubWay_LouCeng


class Bj_ErShouFang_SubWay(myunit.MyTest):
    def test_1(self):
        linkindex = []
        for i, line in enumerate(BJ_ErShouFang_SubWayLine):
            linkindex.append(i)
        For_BianLi(self.driver).tongyidiaoyong(
            cityname=0, leixing='二手房',
            fy_xpath_qian_li='//div[@class="list_wrap"]/ul/li[', fy_xpath_hou_li=']/div[2]/h1/a',
            for_1_range=linkindex,
            subway_f='地铁房', subway_f_xpath='/html/body/section[2]/div[1]/div[1]/div/ul/li[2]/a',
            louceng_xpath='/html/body/div[3]/section[2]/div/div[2]/div[7]/div[1]/a',
            pricemin=0, pricemax=100, mianjimin=20, mianjimax=90,
            for_1_2_index=BJ_ErShouFang_SubWayLine_ZhanTai_index,
            for_1_list=BJ_ErShouFang_SubWayLine, for_2_list=BJ_ErShouFang_SubWayLine_ZhanTai,
            for_3_list=BJ_ErShouFang_SubWay_ShouJia, for_4_list=BJ_ErShouFang_SubWay_MianJi,
            for_5_list=BJ_ErShouFang_SubWay_HuXing, for_6_list=BJ_ErShouFang_SubWay_ChaoXiang,
            for_8_list=BJ_ErShouFang_SubWay_MaiDian, for_9_list=BJ_ErShouFang_SubWay_LouCeng,
            for_1_indexmin=0, for_1_indexmax=len(BJ_ErShouFang_SubWayLine),
            for_2_indexmin=0, for_2_indexmax=len(BJ_ErShouFang_SubWayLine_ZhanTai),
            for_3_indexmin=0, for_3_indexmax=len(BJ_ErShouFang_SubWay_ShouJia),
            for_4_indexmin=0, for_4_indexmax=len(BJ_ErShouFang_SubWay_MianJi),
            for_5_indexmin=0, for_5_indexmax=len(BJ_ErShouFang_SubWay_HuXing),
            for_6_indexmin=0, for_6_indexmax=len(BJ_ErShouFang_SubWay_ChaoXiang),
            for_8_indexmin=0, for_8_indexmax=len(BJ_ErShouFang_SubWay_MaiDian),
            for_9_indexmin=0, for_9_indexmax=len(BJ_ErShouFang_SubWay_LouCeng),
            for_1_flag=True, for_2_flag=True, for_3_flag=True, for_4_flag=True, for_5_flag=True,
            for_6_flag=True, for_7_flag=False, for_8_flag=True, for_9_flag=True, for_10_flag=False,
            for_3_buxian='S0', for_4_buxian='A0', for_5_buxian='H0',
            for_6_buxian='O0', for_8_buxian='T0')