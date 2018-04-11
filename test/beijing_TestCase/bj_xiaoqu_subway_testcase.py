#!/usr/bin/python
# -*- coding:UTF-8 -*-
import data.shhdata as Data
from test.common_package import myunit
from test.common_package.bj_fz_xm_for_bianli import For_BianLi

#北京---小区---区域、商圈
BJ_XiaoQu_SubWayLine = Data.BJ_XiaoQu_SubWayLine
BJ_XiaoQu_SubWayLine_ZhanTai = Data.BJ_XiaoQu_SubWayLine_ZhanTai
BJ_XiaoQu_SubWayLine_ZhanTai_index = Data.BJ_XiaoQu_SubWayLine_ZhanTai_index
#北京---小区---均价
BJ_XiaoQu_SubWayLine_JunJia = Data.BJ_XiaoQu_SubWayLine_JunJia
#北京---小区---楼龄
BJ_XiaoQu_SubWayLine_LouLing = Data.BJ_XiaoQu_SubWayLine_LouLing

class Bj_XiaoQu(myunit.MyTest):
    def test_1(self):
        linkindex = []
        for i, line in enumerate(BJ_XiaoQu_SubWayLine):
            linkindex.append(i)
        For_BianLi(self.driver).tongyidiaoyong(
            cityname=0, leixing='小区',
            fy_xpath_qian_li='//div[@class="list_wrap"]/ul/li[', fy_xpath_hou_li=']/div[2]/h1/a',
            subway_f='地铁房', subway_f_xpath='/html/body/div[3]/section[2]/div[1]/div[1]/ul/li[2]/a',
            for_1_range=linkindex,
            for_1_2_index=BJ_XiaoQu_SubWayLine_ZhanTai_index,
            for_1_list=BJ_XiaoQu_SubWayLine, for_2_list=BJ_XiaoQu_SubWayLine_ZhanTai,
            for_3_list=BJ_XiaoQu_SubWayLine_JunJia, for_4_list=BJ_XiaoQu_SubWayLine_LouLing,
            for_3_indexmin=0, for_3_indexmax=len(BJ_XiaoQu_SubWayLine_JunJia),
            for_4_indexmin=0, for_4_indexmax=len(BJ_XiaoQu_SubWayLine_LouLing),
            for_1_flag=True, for_2_flag=True, for_3_flag=True, for_4_flag=True, for_5_flag=False,
            for_6_flag=False, for_7_flag=False, for_8_flag=False, for_9_flag=False, for_10_flag=False,
            for_3_buxian='S0', for_4_buxian='Y0')
