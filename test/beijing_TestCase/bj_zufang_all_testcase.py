#!/usr/bin/python
# -*- coding:UTF-8 -*-
import data.shhdata as Data
from test.common_package import myunit
from test.common_package.bj_fz_xm_for_bianli import For_BianLi

#北京---租房---区域、商圈
BJ_ZuFang_QuYu = Data.BJ_ZuFang_QuYu
BJ_ZuFang_ShangQuan = Data.BJ_ZuFang_ShangQuan
BJ_ZuFang_ShangQuan_index = Data.BJ_ZuFang_ShangQuan_index
#北京---租房---租金
BJ_ZuFang_ZuJin = Data.BJ_ZuFang_ZuJin
#北京---租房---面积
BJ_ZuFang_MianJi = Data.BJ_ZuFang_MianJi
#北京---租房---户型
BJ_ZuFang_HuXing = Data.BJ_ZuFang_HuXing
#北京---租房---朝向
BJ_ZuFang_ChaoXiang = Data.BJ_ZuFang_ChaoXiang
#北京---租房---特色
BJ_ZuFang_TeSe = Data.BJ_ZuFang_TeSe
#北京---租房---配置
BJ_ZuFang_PeiZhi = Data.BJ_ZuFang_PeiZhi
#北京---租房---装修
BJ_ZuFang_ZhuangXiu = Data.BJ_ZuFang_ZhuangXiu
#北京---租房---方式
BJ_ZuFang_FangShi = Data.BJ_ZuFang_FangShi

class Bj_ZuFang(myunit.MyTest):
    def __test(self,for_1_flag, for_2_flag, for_3_flag, for_4_flag, for_5_flag,for_6_flag, for_7_flag, for_8_flag, for_9_flag, for_10_flag):
        linkindex = []
        for i, line in enumerate(BJ_ZuFang_QuYu):
            linkindex.append(i)
        For_BianLi(self.driver).tongyidiaoyong(
            cityname=0,leixing='租房',
            fy_xpath_qian_li='//div[@class="list_wrap"]/ul/li[',fy_xpath_hou_li=']/div[2]/h1/a',
            for_1_range=linkindex,
            pricemin=0, pricemax=100, mianjimin=20, mianjimax=90,
            for_1_2_index=BJ_ZuFang_ShangQuan_index,
            for_1_list=BJ_ZuFang_QuYu,for_2_list=BJ_ZuFang_ShangQuan,
            for_3_list=BJ_ZuFang_ZuJin,for_4_list=BJ_ZuFang_MianJi,
            for_5_list=BJ_ZuFang_HuXing,for_6_list=BJ_ZuFang_ChaoXiang,
            for_7_list=BJ_ZuFang_TeSe,for_8_list=BJ_ZuFang_PeiZhi,
            for_9_list=BJ_ZuFang_ZhuangXiu,for_10_list=BJ_ZuFang_FangShi,
            for_1_indexmin=0,for_1_indexmax=len(BJ_ZuFang_QuYu),
            for_2_indexmin=0,for_2_indexmax=len(BJ_ZuFang_ShangQuan),
            for_3_indexmin=0,for_3_indexmax=len(BJ_ZuFang_ZuJin),
            for_4_indexmin=0,for_4_indexmax=len(BJ_ZuFang_MianJi),
            for_5_indexmin=0,for_5_indexmax=len(BJ_ZuFang_HuXing),
            for_6_indexmin=0, for_6_indexmax=len(BJ_ZuFang_ChaoXiang),
            for_7_indexmin=0,for_7_indexmax=len(BJ_ZuFang_TeSe),
            for_8_indexmin=0, for_8_indexmax=len(BJ_ZuFang_PeiZhi),
            for_9_indexmin=0, for_9_indexmax=len(BJ_ZuFang_ZhuangXiu),
            for_10_indexmin=0, for_10_indexmax=len(BJ_ZuFang_FangShi),
            for_1_flag=for_1_flag, for_2_flag=for_2_flag, for_3_flag=for_3_flag,
            for_4_flag=for_4_flag, for_5_flag=for_5_flag, for_6_flag=for_6_flag,
            for_7_flag=for_7_flag, for_8_flag=for_8_flag, for_9_flag=for_9_flag,
            for_10_flag=for_10_flag,
            for_3_buxian='S0',for_4_buxian='A0',for_5_buxian='H0',
            for_6_buxian='O0',for_7_buxian='T0',for_8_buxian='P0')

    def test_1(self):
        '''遍历每一个查询条件，校验房源详情'''
        self.__test(
            for_1_flag=True, for_2_flag=True, for_3_flag=True, for_4_flag=True, for_5_flag=True,
            for_6_flag=True, for_7_flag=True, for_8_flag=True, for_9_flag=True, for_10_flag=True
        )

