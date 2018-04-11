#!/usr/bin/python
# -*- coding:UTF-8 -*-
import data.shhdata as Data
from test.common_package import myunit
from test.common_package.bj_fz_xm_for_bianli import For_BianLi

#北京---租房---地铁房线路、站台
BJ_ZuFang_SubWayLine = Data.BJ_ZuFang_SubWayLine
BJ_ZuFang_SubWayLine_ZhanTai = Data.BJ_ZuFang_SubWayLine_ZhanTai
BJ_ZuFang_SubWayLine_ZhanTai_index = Data.BJ_ZuFang_SubWayLine_ZhanTai_index
#北京---租房---租金
BJ_ZuFang_SubWay_ZuJin = Data.BJ_ZuFang_SubWay_ZuJin
#北京---租房---面积
BJ_ZuFang_SubWay_MianJi = Data.BJ_ZuFang_SubWay_MianJi
#北京---租房---户型
BJ_ZuFang_SubWay_HuXing = Data.BJ_ZuFang_SubWay_HuXing
#北京---租房---朝向
BJ_ZuFang_SubWay_ChaoXiang = Data.BJ_ZuFang_SubWay_ChaoXiang
#北京---租房---特色
BJ_ZuFang_SubWay_TeSe = Data.BJ_ZuFang_SubWay_TeSe
#北京---租房---配置
BJ_ZuFang_SubWay_PeiZhi = Data.BJ_ZuFang_SubWay_PeiZhi
#北京---租房---装修
BJ_ZuFang_SubWay_ZhuangXiu = Data.BJ_ZuFang_SubWay_ZhuangXiu
#北京---租房---方式
BJ_ZuFang_SubWay_FangShi = Data.BJ_ZuFang_SubWay_FangShi


class Bj_ZuFang_SubWay(myunit.MyTest):
    def test_1(self):
        linkindex = []
        for i, line in enumerate(BJ_ZuFang_SubWayLine):
            linkindex.append(i)
        For_BianLi(self.driver).tongyidiaoyong(
            cityname=0, leixing='租房',
            fy_xpath_qian_li='//div[@class="list_wrap"]/ul/li[', fy_xpath_hou_li=']/div[3]/h1/a',
            for_1_range=linkindex,
            subway_f='地铁房',
            for_1_2_index=BJ_ZuFang_SubWayLine_ZhanTai_index,
            for_1_list=BJ_ZuFang_SubWayLine,for_2_list=BJ_ZuFang_SubWayLine_ZhanTai,
            for_3_list=BJ_ZuFang_SubWay_ZuJin,for_4_list=BJ_ZuFang_SubWay_MianJi,
            for_5_list=BJ_ZuFang_SubWay_HuXing,for_6_list=BJ_ZuFang_SubWay_ChaoXiang,
            for_7_list=BJ_ZuFang_SubWay_TeSe,for_8_list=BJ_ZuFang_SubWay_PeiZhi,
            for_9_list=BJ_ZuFang_SubWay_ZhuangXiu,for_10_list=BJ_ZuFang_SubWay_FangShi,
            for_1_indexmin=0,for_1_indexmax=len(BJ_ZuFang_SubWayLine),
            for_2_indexmin=0,for_2_indexmax=len(BJ_ZuFang_SubWayLine_ZhanTai),
            for_3_indexmin=0,for_3_indexmax=len(BJ_ZuFang_SubWay_ZuJin),
            for_4_indexmin=0,for_4_indexmax=len(BJ_ZuFang_SubWay_MianJi),
            for_5_indexmin=0,for_5_indexmax=len(BJ_ZuFang_SubWay_HuXing),
            for_6_indexmin=0, for_6_indexmax=len(BJ_ZuFang_SubWay_ChaoXiang),
            for_7_indexmin=0,for_7_indexmax=len(BJ_ZuFang_SubWay_TeSe),
            for_8_indexmin=0, for_8_indexmax=len(BJ_ZuFang_SubWay_PeiZhi),
            for_9_indexmin=0, for_9_indexmax=len(BJ_ZuFang_SubWay_ZhuangXiu),
            for_10_indexmin=0, for_10_indexmax=len(BJ_ZuFang_SubWay_FangShi),
            for_1_flag=True,for_2_flag=True,for_3_flag=True,for_4_flag=True,for_5_flag=True,
            for_6_flag=True,for_7_flag=True,for_8_flag=True,for_9_flag=True,for_10_flag=True,
            for_3_buxian='S0',for_4_buxian='A0',for_5_buxian='H0',
            for_6_buxian='O0',for_7_buxian='T0',for_8_buxian='P0')