#!/usr/bin/python
# -*- coding:UTF-8 -*-
import data.shhdata as Data
from test.common_package import myunit
from test.common_package.bj_fz_xm_for_bianli import For_BianLi

#厦门---小区---区域、商圈
XM_XiaoQu_QuYu = Data.XM_XiaoQu_QuYu
XM_XiaoQu_ShangQuan = Data.XM_XiaoQu_ShangQuan
XM_XiaoQu_ShangQuan_index = Data.XM_XiaoQu_ShangQuan_index
#厦门---小区---均价
XM_XiaoQu_JunJia = Data.XM_XiaoQu_JunJia
#厦门---小区---楼龄
XM_XiaoQu_LouLing = Data.XM_XiaoQu_LouLing

class Xm_XiaoQu(myunit.MyTest):
    def test_1(self):
        linkindex = []
        for i, line in enumerate(XM_XiaoQu_QuYu):
            linkindex.append(i)
        For_BianLi(self.driver).tongyidiaoyong(
            cityname=2, leixing='小区',
            fy_xpath_qian_li='//div[@class="list_wrap"]/ul/li[', fy_xpath_hou_li=']/div[2]/h1/a',
            for_1_range=linkindex,
            pricemin=0, pricemax=100, mianjimin=20, mianjimax=90,
            for_1_2_index=XM_XiaoQu_ShangQuan_index,
            for_1_list=XM_XiaoQu_QuYu, for_2_list=XM_XiaoQu_ShangQuan,
            for_3_list=XM_XiaoQu_JunJia, for_4_list=XM_XiaoQu_LouLing,
            for_3_indexmin=0, for_3_indexmax=len(XM_XiaoQu_JunJia),
            for_4_indexmin=0, for_4_indexmax=len(XM_XiaoQu_LouLing),
            for_1_flag=True, for_2_flag=True, for_3_flag=True, for_4_flag=True, for_5_flag=False,
            for_6_flag=False, for_7_flag=False, for_8_flag=False, for_9_flag=False, for_10_flag=False,
            for_3_buxian='JG0', for_4_buxian='J0')
