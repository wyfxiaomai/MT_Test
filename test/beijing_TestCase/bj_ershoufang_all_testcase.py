#!/usr/bin/python
# -*- coding:UTF-8 -*-
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
    def test_1(self):
        linkindex = []
        for i, line in enumerate(BJ_ErShouFang_QuYu):
            linkindex.append(i)
        For_BianLi(self.driver).tongyidiaoyong(
            cityname=0,leixing='二手房',
            fy_xpath_qian_li='//div[@class="list_wrap"]/ul/li[',fy_xpath_hou_li=']/div[2]/h1/a',
            for_1_range=linkindex,
            louceng_xpath='/html/body/section[2]/div[1]/div[2]/div[7]/div[1]/a',
            pricemin=0, pricemax=100, mianjimin=20, mianjimax=90,
            for_1_2_index=BJ_ErShouFang_ShangQuan_index,
            for_1_list=BJ_ErShouFang_QuYu,for_2_list=BJ_ErShouFang_ShangQuan,
            for_3_list=BJ_ErShouFang_ShouJia,for_4_list=BJ_ErShouFang_MianJi,
            for_5_list=BJ_ErShouFang_HuXing,for_6_list=BJ_ErShouFang_ChaoXiang,
            for_8_list=BJ_ErShouFang_MaiDian,for_9_list=BJ_ErShouFang_LouCeng,
            for_1_indexmin=0,for_1_indexmax=len(BJ_ErShouFang_QuYu),
            for_2_indexmin=0,for_2_indexmax=len(BJ_ErShouFang_ShangQuan),
            for_3_indexmin=0,for_3_indexmax=len(BJ_ErShouFang_ShouJia),
            for_4_indexmin=0,for_4_indexmax=len(BJ_ErShouFang_MianJi),
            for_5_indexmin=0,for_5_indexmax=len(BJ_ErShouFang_HuXing),
            for_6_indexmin=0, for_6_indexmax=len(BJ_ErShouFang_ChaoXiang),
            for_8_indexmin=0,for_8_indexmax=len(BJ_ErShouFang_MaiDian),
            for_9_indexmin=0, for_9_indexmax=len(BJ_ErShouFang_LouCeng),
            for_1_flag=True,for_2_flag=True,for_3_flag=True,for_4_flag=True,for_5_flag=True,
            for_6_flag=True,for_7_flag=False,for_8_flag=True,for_9_flag=True,for_10_flag=False,
            for_3_buxian='S0',for_4_buxian='A0',for_5_buxian='H0',
            for_6_buxian='O0',for_8_buxian='T0')
