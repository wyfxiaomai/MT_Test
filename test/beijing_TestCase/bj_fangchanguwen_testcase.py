#!/usr/bin/python
# -*- coding:UTF-8 -*-
import data.shhdata as Data
from test.common_package import myunit
from test.common_package.bj_fz_xm_for_bianli import For_BianLi

#北京---房产顾问---区域、商圈
BJ_FangChanGuWen_QuYu = Data.BJ_FangChanGuWen_QuYu
BJ_FangChanGuWen_ShangQuan = Data.BJ_FangChanGuWen_ShangQuan
BJ_FangChanGuWen_ShangQuan_index = Data.BJ_FangChanGuWen_ShangQuan_index


class Fz_FangChanGuWen(myunit.MyTest):
    def __test(self,for_1_flag, for_2_flag, for_3_flag, for_4_flag, for_5_flag,for_6_flag, for_7_flag, for_8_flag, for_9_flag, for_10_flag):
        linkindex = []
        for i, line in enumerate(BJ_FangChanGuWen_QuYu):
            linkindex.append(i)
        For_BianLi(self.driver).tongyidiaoyong(
            cityname=0,leixing='房产顾问',
            fy_xpath_qian_li='//div[@class="list_wrap"]/ul/li[',fy_xpath_hou_li=']/div/div[1]/h6/a',
            for_1_range=linkindex,
            for_1_2_index=BJ_FangChanGuWen_ShangQuan_index,
            for_1_list=BJ_FangChanGuWen_QuYu,for_2_list=BJ_FangChanGuWen_ShangQuan,
            for_1_indexmin=0,for_1_indexmax=len(BJ_FangChanGuWen_QuYu),
            for_2_indexmin=0,for_2_indexmax=len(BJ_FangChanGuWen_ShangQuan),
            for_1_flag=for_1_flag, for_2_flag=for_2_flag, for_3_flag=for_3_flag,
            for_4_flag=for_4_flag, for_5_flag=for_5_flag, for_6_flag=for_6_flag,
            for_7_flag=for_7_flag, for_8_flag=for_8_flag, for_9_flag=for_9_flag,
            for_10_flag=for_10_flag)

    def test_1(self):
        '''遍历每一个查询条件，校验房源详情'''
        self.__test(
            for_1_flag=True, for_2_flag=True, for_3_flag=False, for_4_flag=False, for_5_flag=False,
            for_6_flag=False, for_7_flag=False, for_8_flag=False, for_9_flag=False, for_10_flag=False
        )
