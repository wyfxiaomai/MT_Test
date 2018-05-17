#!/usr/bin/python
# -*- coding:UTF-8 -*-
import data.shhdata as Data
from test.common_package import myunit
from test.common_package.bj_fz_xm_for_bianli import For_BianLi

#北京---小区---区域、商圈
BJ_XiaoQu_QuYu = Data.BJ_XiaoQu_QuYu
BJ_XiaoQu_ShangQuan = Data.BJ_XiaoQu_ShangQuan
BJ_XiaoQu_ShangQuan_index = Data.BJ_XiaoQu_ShangQuan_index
#北京---小区---均价
BJ_XiaoQu_JunJia = Data.BJ_XiaoQu_JunJia
#北京---小区---楼龄
BJ_XiaoQu_LouLing = Data.BJ_XiaoQu_LouLing

class Bj_XiaoQu(myunit.MyTest):
    def __test(self,for_1_flag, for_2_flag, for_3_flag, for_4_flag, for_5_flag,for_6_flag, for_7_flag, for_8_flag, for_9_flag, for_10_flag):
        linkindex = []
        for i, line in enumerate(BJ_XiaoQu_QuYu):
            linkindex.append(i)
        For_BianLi(self.driver).tongyidiaoyong(
            cityname=0, leixing='小区',
            fy_xpath_qian_li='//div[@class="list_wrap"]/ul/li[', fy_xpath_hou_li=']/div[2]/h1/a',
            for_1_range=linkindex,
            for_1_2_index=BJ_XiaoQu_ShangQuan_index,
            for_1_list=BJ_XiaoQu_QuYu, for_2_list=BJ_XiaoQu_ShangQuan,
            for_3_list=BJ_XiaoQu_JunJia, for_4_list=BJ_XiaoQu_LouLing,
            for_3_indexmin=0, for_3_indexmax=len(BJ_XiaoQu_JunJia),
            for_4_indexmin=0, for_4_indexmax=len(BJ_XiaoQu_LouLing),
            for_1_flag=for_1_flag, for_2_flag=for_2_flag, for_3_flag=for_3_flag,
            for_4_flag=for_4_flag, for_5_flag=for_5_flag, for_6_flag=for_6_flag,
            for_7_flag=for_7_flag, for_8_flag=for_8_flag, for_9_flag=for_9_flag,
            for_10_flag=for_10_flag,
            for_3_buxian='S0', for_4_buxian='Y0')

    def test_1(self):
        '''遍历每一个查询条件，校验房源详情'''
        self.__test(
            for_1_flag=True, for_2_flag=True, for_3_flag=True, for_4_flag=True, for_5_flag=False,
            for_6_flag=False, for_7_flag=False, for_8_flag=False, for_9_flag=False, for_10_flag=False
        )
