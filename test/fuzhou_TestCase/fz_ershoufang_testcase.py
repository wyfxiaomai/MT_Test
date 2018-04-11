#!/usr/bin/python
# -*- coding:UTF-8 -*-

import data.shhdata as Data
from test.common_package.bj_fz_xm_for_bianli import For_BianLi
from test.common_package import myunit

#福州---二手房---区域、商圈
FZ_ErShouFang_QuYu = Data.FZ_ErShouFang_QuYu
FZ_ErShouFang_ShangQuan = Data.FZ_ErShouFang_ShangQuan
FZ_ErShouFang_ShangQuan_index = Data.FZ_ErShouFang_ShangQuan_index
#福州---二手房---售价
FZ_ErShouFang_ShouJia = Data.FZ_ErShouFang_ShouJia
#福州---二手房---面积
FZ_ErShouFang_MianJi = Data.FZ_ErShouFang_MianJi
#福州---二手房---户型
FZ_ErShouFang_HuXing = Data.FZ_ErShouFang_HuXing
#福州---二手房---电梯
FZ_ErShouFang_DianTi = Data.FZ_ErShouFang_DianTi
#福州---二手房---装修
FZ_ErShouFang_ZhuangXiu = Data.FZ_ErShouFang_ZhuangXiu
#福州---二手房---卖点
FZ_ErShouFang_MaiDian = Data.FZ_ErShouFang_MaiDian
#福州---二手房---楼层
FZ_ErShouFang_LouCeng = Data.FZ_ErShouFang_LouCeng
#福州---二手房---楼龄
FZ_ErShouFang_LouLing = Data.FZ_ErShouFang_LouLing

class Fz_ErShouFang(myunit.MyTest):
    def test_1(self):
        linkindex = []
        for i, line in enumerate(FZ_ErShouFang_QuYu):
            linkindex.append(i)
        For_BianLi(self.driver).tongyidiaoyong(
            cityname=1,leixing='二手房',
            fy_xpath_qian_li='//div[@class="list_wrap"]/ul/li[',fy_xpath_hou_li=']/div[2]/h1/a',
            for_1_range=linkindex,louceng_xpath='/html/body/section[2]/div[1]/div[2]/div[8]/div[1]/a',
            louling_xpath='/html/body/section[2]/div[1]/div[2]/div[8]/div[2]/a',
            pricemin=0, pricemax=100, mianjimin=20, mianjimax=90,
            for_1_2_index=FZ_ErShouFang_ShangQuan_index,
            for_1_list=FZ_ErShouFang_QuYu,for_2_list=FZ_ErShouFang_ShangQuan,
            for_3_list=FZ_ErShouFang_ShouJia,for_4_list=FZ_ErShouFang_MianJi,
            for_5_list=FZ_ErShouFang_HuXing,for_6_list=FZ_ErShouFang_DianTi,
            for_7_list=FZ_ErShouFang_ZhuangXiu,for_8_list=FZ_ErShouFang_MaiDian,
            for_9_list=FZ_ErShouFang_LouCeng,for_10_list=FZ_ErShouFang_LouLing,
            for_1_indexmin=0,for_1_indexmax=len(FZ_ErShouFang_QuYu),
            for_2_indexmin=0,for_2_indexmax=len(FZ_ErShouFang_ShangQuan),
            for_3_indexmin=0,for_3_indexmax=len(FZ_ErShouFang_ShouJia),
            for_4_indexmin=0,for_4_indexmax=len(FZ_ErShouFang_MianJi),
            for_5_indexmin=0,for_5_indexmax=len(FZ_ErShouFang_HuXing),
            for_6_indexmin=0, for_6_indexmax=len(FZ_ErShouFang_DianTi),
            for_7_indexmin=0,for_7_indexmax=len(FZ_ErShouFang_ZhuangXiu),
            for_8_indexmin=0,for_8_indexmax=len(FZ_ErShouFang_MaiDian),
            for_9_indexmin=0, for_9_indexmax=len(FZ_ErShouFang_LouCeng),
            for_10_indexmin=0,for_10_indexmax=len(FZ_ErShouFang_LouLing),
            for_1_flag=True,for_2_flag=True,for_3_flag=True,for_4_flag=True,for_5_flag=False,
            for_6_flag=False,for_7_flag=False,for_8_flag=False,for_9_flag=False,for_10_flag=False,
            for_3_buxian='S0',for_4_buxian='A0',for_5_buxian='H0',
            for_6_buxian='DT2',for_7_buxian='ZX0',for_8_buxian='T0')

import unittest
if __name__=="__main__":
    unittest.main()