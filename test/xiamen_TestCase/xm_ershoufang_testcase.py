#!/usr/bin/python
# -*- coding:UTF-8 -*-
import data.shhdata as Data
from test.common_package import myunit
from test.common_package.bj_fz_xm_for_bianli import For_BianLi

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

class Xm_ErShouFang(myunit.MyTest):
    def __test(self, for_1_flag, for_2_flag, for_3_flag, for_4_flag, for_5_flag, for_6_flag, for_7_flag, for_8_flag,for_9_flag, for_10_flag):
        linkindex = []
        for i, line in enumerate(XM_ErShouFang_QuYu):
            linkindex.append(i)
        For_BianLi(self.driver).tongyidiaoyong(
            cityname=2,leixing='二手房',
            fy_xpath_qian_li='//div[@class="list_wrap"]/ul/li[',fy_xpath_hou_li=']/div[2]/h1/a',
            for_1_range=linkindex,
            louceng_xpath='/html/body/section[2]/div[1]/div[2]/div[8]/div[1]/a',
            louling_xpath='/html/body/section[2]/div[1]/div[2]/div[8]/div[2]/a',
            pricemin=0, pricemax=100, mianjimin=20, mianjimax=90,
            for_1_2_index=XM_ErShouFang_ShangQuan_index,
            for_1_list=XM_ErShouFang_QuYu,for_2_list=XM_ErShouFang_ShangQuan,
            for_3_list=XM_ErShouFang_ShouJia,for_4_list=XM_ErShouFang_MianJi,
            for_5_list=XM_ErShouFang_HuXing,for_6_list=XM_ErShouFang_DianTi,
            for_7_list=XM_ErShouFang_ZhuangXiu,for_8_list=XM_ErShouFang_MaiDian,
            for_9_list=XM_ErShouFang_LouCeng,for_10_list=XM_ErShouFang_LouLing,
            for_1_indexmin=0,for_1_indexmax=len(XM_ErShouFang_QuYu),
            for_2_indexmin=0,for_2_indexmax=len(XM_ErShouFang_ShangQuan),
            for_3_indexmin=0,for_3_indexmax=len(XM_ErShouFang_ShouJia),
            for_4_indexmin=0,for_4_indexmax=len(XM_ErShouFang_MianJi),
            for_5_indexmin=0,for_5_indexmax=len(XM_ErShouFang_HuXing),
            for_6_indexmin=0, for_6_indexmax=len(XM_ErShouFang_DianTi),
            for_7_indexmin=0,for_7_indexmax=len(XM_ErShouFang_ZhuangXiu),
            for_8_indexmin=0,for_8_indexmax=len(XM_ErShouFang_MaiDian),
            for_9_indexmin=0, for_9_indexmax=len(XM_ErShouFang_LouCeng),
            for_10_indexmin=0,for_10_indexmax=len(XM_ErShouFang_LouLing),
            for_1_flag=for_1_flag, for_2_flag=for_2_flag, for_3_flag=for_3_flag,
            for_4_flag=for_4_flag, for_5_flag=for_5_flag, for_6_flag=for_6_flag,
            for_7_flag=for_7_flag, for_8_flag=for_8_flag, for_9_flag=for_9_flag,
            for_10_flag=for_10_flag,
            for_3_buxian='S0',for_4_buxian='A0',for_5_buxian='H0',
            for_6_buxian='DT2',for_7_buxian='ZX0',for_8_buxian='T0')

    def test_1(self):
        '''遍历每一个查询条件，校验房源详情'''
        self.__test(
            for_1_flag=True, for_2_flag=True, for_3_flag=True, for_4_flag=True, for_5_flag=True,
            for_6_flag=True, for_7_flag=True, for_8_flag=True, for_9_flag=True, for_10_flag=True
        )

