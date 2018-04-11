#!/usr/bin/python
# -*- coding:UTF-8 -*-
import data.shhdata as Data
from test.common_package import myunit
from test.common_package.bj_fz_xm_for_bianli import For_BianLi

#福州---二手房---区域、商圈
FZ_FangChanGuWen_QuYu = Data.FZ_FangChanGuWen_QuYu
FZ_FangChanGuWen_ShangQuan = Data.FZ_FangChanGuWen_ShangQuan
FZ_FangChanGuWen_ShangQuan_index = Data.FZ_FangChanGuWen_ShangQuan_index


class Fz_FangChanGuWen(myunit.MyTest):
    def test_1(self):
        linkindex = []
        for i, line in enumerate(FZ_FangChanGuWen_QuYu):
            linkindex.append(i)
        For_BianLi(self.driver).tongyidiaoyong(
            cityname=1,leixing='房产顾问',
            fy_xpath_qian_li='//div[@class="list_wrap"]/ul/li[',fy_xpath_hou_li=']/div/div[1]/h6/a',
            for_1_range=linkindex,
            for_1_2_index=FZ_FangChanGuWen_ShangQuan_index,
            for_1_list=FZ_FangChanGuWen_QuYu,for_2_list=FZ_FangChanGuWen_ShangQuan,
            for_1_indexmin=0,for_1_indexmax=len(FZ_FangChanGuWen_QuYu),
            for_2_indexmin=0,for_2_indexmax=len(FZ_FangChanGuWen_ShangQuan),
            for_1_flag=True,for_2_flag=True,for_3_flag=False,for_4_flag=False,for_5_flag=False,
            for_6_flag=False,for_7_flag=False,for_8_flag=False,for_9_flag=False,for_10_flag=False)
