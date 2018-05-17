#!/usr/bin/python
# -*- coding:UTF-8 -*-
import data.shhdata as Data
from test.common_package import myunit
from test.common_package.bj_fz_xm_for_bianli import For_BianLi

#福州---别墅---区域、商圈
FZ_BieShu_QuYu = Data.FZ_BieShu_QuYu
FZ_BieShu_ShangQuan = Data.FZ_BieShu_ShangQuan
FZ_BieShu_ShangQuan_index = Data.FZ_BieShu_ShangQuan_index
#福州---别墅---售价
FZ_BieShu_ShouJia = Data.FZ_BieShu_ShouJia
#福州---别墅---面积
FZ_BieShu_MianJi = Data.FZ_BieShu_MianJi
#福州---别墅---户型
FZ_BieShu_HuXing = Data.FZ_BieShu_HuXing
#福州---别墅---电梯
FZ_BieShu_DianTi = Data.FZ_BieShu_DianTi
#福州---别墅---装修
FZ_BieShu_ZhuangXiu = Data.FZ_BieShu_ZhuangXiu
#福州---别墅---卖点
FZ_BieShu_MaiDian = Data.FZ_BieShu_MaiDian
#福州---别墅---楼龄
FZ_BieShu_LouLing = Data.FZ_BieShu_LouLing

class Fz_BieShu(myunit.MyTest):
    def __test(self,for_1_flag, for_2_flag, for_3_flag, for_4_flag, for_5_flag, for_6_flag, for_7_flag, for_8_flag,for_9_flag, for_10_flag):
        linkindex = []
        for i, line in enumerate(FZ_BieShu_QuYu):
            linkindex.append(i)
        For_BianLi(self.driver).tongyidiaoyong(
            cityname=1, leixing='别墅',
            fy_xpath_qian_li='//div[@class="list_wrap"]/ul/li[', fy_xpath_hou_li=']/div[2]/h1/a',
            for_1_range=linkindex,
            louling_xpath='/html/body/section[2]/div[1]/div/div[8]/div[1]/a',
            pricemin=0, pricemax=100, mianjimin=20, mianjimax=90,
            for_1_2_index=FZ_BieShu_ShangQuan_index,
            for_1_list=FZ_BieShu_QuYu, for_2_list=FZ_BieShu_ShangQuan,
            for_3_list=FZ_BieShu_ShouJia, for_4_list=FZ_BieShu_MianJi,
            for_5_list=FZ_BieShu_HuXing, for_6_list=FZ_BieShu_DianTi,
            for_7_list=FZ_BieShu_ZhuangXiu, for_8_list=FZ_BieShu_MaiDian,
            for_10_list=FZ_BieShu_LouLing,
            for_1_indexmin=0, for_1_indexmax=len(FZ_BieShu_QuYu),
            for_2_indexmin=0, for_2_indexmax=len(FZ_BieShu_ShangQuan),
            for_3_indexmin=0, for_3_indexmax=len(FZ_BieShu_ShouJia),
            for_4_indexmin=0, for_4_indexmax=len(FZ_BieShu_MianJi),
            for_5_indexmin=0, for_5_indexmax=len(FZ_BieShu_HuXing),
            for_6_indexmin=0, for_6_indexmax=len(FZ_BieShu_DianTi),
            for_7_indexmin=0, for_7_indexmax=len(FZ_BieShu_ZhuangXiu),
            for_8_indexmin=0, for_8_indexmax=len(FZ_BieShu_MaiDian),
            for_10_indexmin=0, for_10_indexmax=len(FZ_BieShu_LouLing),
            for_1_flag=for_1_flag, for_2_flag=for_2_flag, for_3_flag=for_3_flag,
            for_4_flag=for_4_flag, for_5_flag=for_5_flag, for_6_flag=for_6_flag,
            for_7_flag=for_7_flag, for_8_flag=for_8_flag, for_9_flag=for_9_flag,
            for_10_flag=for_10_flag,
            for_3_buxian='S0', for_4_buxian='A0', for_5_buxian='BS0',
            for_6_buxian='DT2', for_7_buxian='ZX0', for_8_buxian='T0')

    def test_1(self):
        '''遍历每一个查询条件，校验房源详情'''
        self.__test(
            for_1_flag=True, for_2_flag=True, for_3_flag=True, for_4_flag=True, for_5_flag=True,
            for_6_flag=True, for_7_flag=True, for_8_flag=True, for_9_flag=False, for_10_flag=True
        )
