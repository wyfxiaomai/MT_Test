#!/usr/bin/python
# -*- coding:UTF-8 -*-
import data.shhdata as Data
from test.common_package import myunit
from test.common_package.bj_fz_xm_for_bianli import For_BianLi

#福州---小区---区域、商圈
FZ_XiaoQu_QuYu = Data.FZ_XiaoQu_QuYu
FZ_XiaoQu_ShangQuan = Data.FZ_XiaoQu_ShangQuan
FZ_XiaoQu_ShangQuan_index = Data.FZ_XiaoQu_ShangQuan_index
#福州---小区---均价
FZ_XiaoQu_JunJia = Data.FZ_XiaoQu_JunJia
#福州---小区---楼龄
FZ_XiaoQu_LouLing = Data.FZ_XiaoQu_LouLing

class Fz_XiaoQu(myunit.MyTest):
    def __test(self, for_1_flag, for_2_flag, for_3_flag, for_4_flag, for_5_flag, for_6_flag, for_7_flag, for_8_flag,for_9_flag, for_10_flag):
        linkindex = []
        for i, line in enumerate(FZ_XiaoQu_QuYu):
            linkindex.append(i)
        For_BianLi(self.driver).tongyidiaoyong(
            cityname=1, leixing='小区',
            fy_xpath_qian_li='//div[@class="list_wrap"]/ul/li[', fy_xpath_hou_li=']/div[2]/h1/a',
            for_1_range=linkindex,
            pricemin=0, pricemax=100, mianjimin=20, mianjimax=90,
            for_1_2_index=FZ_XiaoQu_ShangQuan_index,
            for_1_list=FZ_XiaoQu_QuYu, for_2_list=FZ_XiaoQu_ShangQuan,
            for_3_list=FZ_XiaoQu_JunJia, for_4_list=FZ_XiaoQu_LouLing,
            for_3_indexmin=0, for_3_indexmax=len(FZ_XiaoQu_JunJia),
            for_4_indexmin=0, for_4_indexmax=len(FZ_XiaoQu_LouLing),
            for_1_flag=for_1_flag, for_2_flag=for_2_flag, for_3_flag=for_3_flag,
            for_4_flag=for_4_flag, for_5_flag=for_5_flag, for_6_flag=for_6_flag,
            for_7_flag=for_7_flag, for_8_flag=for_8_flag, for_9_flag=for_9_flag,
            for_10_flag=for_10_flag,
            for_3_buxian='JG0', for_4_buxian='J0')

    def test_1(self):
        '''遍历每一个查询条件，校验房源详情'''
        self.__test(
            for_1_flag=True, for_2_flag=True, for_3_flag=True, for_4_flag=True, for_5_flag=False,
            for_6_flag=False, for_7_flag=False, for_8_flag=False, for_9_flag=False, for_10_flag=False
        )
