#!/usr/bin/python
# -*- coding:UTF-8 -*-
from time import sleep
from selenium.webdriver.common.by import By
from test.common_package.basic import Page
import requests,json
from lib.log import *


"""
header = {Authorization:basic ios_ad9a3d13a089df11ef95448e02d19e12}
"""
class FangYuanXiangQing(Page):
    def guolv_fangyuanbianhao(self):
        fangyuanbianhao = ['IH00325371', 'IH00084919', 'IH00647217', 'IH00466329', 'IH00540822', 'IH00343884', 'IH00637100']
        fangyuanbianhao = [fybh[1:] for fybh in fangyuanbianhao]
        return fangyuanbianhao

    def get_json(self,fynum):
        url = 'http://172.16.5.35:84/service/HouseSecond/GetHouseByHouseCode'
        header = {'Authorization': 'basic ios_ad9a3d13a089df11ef95448e02d19e12'}

        keyword = {'AreaKey':'FZ','AreaValue':'3','HouseCode':fynum[1:]}
        try:
            resp = requests.get(url,params=keyword,headers=header)
            resp.raise_for_status()
            resp.encoding = resp.apparent_encoding
            resp_json = resp.json()
            print('123',resp_json)
            HouseCode = resp_json["data"]["HouseInfo"]["HouseCode"]  # 房源编号
            PriceTotal = resp_json["data"]["HouseInfo"]["PriceTotal"]  # 总价
            PriceSingle = resp_json["data"]["HouseInfo"]["PriceSingle"]  # 单价
            AreaSize = resp_json["data"]["HouseInfo"]["AreaSize"]  # 面积
            Layout = resp_json["data"]["HouseInfo"]["Layout"]  # 户型
            Direction = resp_json["data"]["HouseInfo"]["Direction"]  # 朝向
            Floor = resp_json["data"]["HouseInfo"]["Floor"]  # 楼层
            Dict_Name = resp_json["data"]["HouseInfo"]["Dict_Name"]  # 区域
            Hou_Name = resp_json["data"]["HouseInfo"]["Hou_Name"]  # 小区名称
            PlateName = resp_json["data"]["HouseInfo"]["PlateName"]  # 商圈
            ReFinishdate = resp_json["data"]["HouseInfo"]["ReFinishdate"]  # 建成年代
            Per_Name = resp_json["data"]["HouseInfo"]["Per_Name"]  # 跟单人
            #return HouseCode,PriceTotal,PriceSingle,AreaSize,Layout,Direction,Floor,Dict_Name,Hou_Name,PlateName,ReFinishdate,Hou_Remark,Per_Name
            get_json_fydata_dict = {'HouseCode': HouseCode, 'PriceTotal': PriceTotal,'PriceSingle': PriceSingle, 'AreaSize': AreaSize, 'Layout': Layout,
                                        'Direction': Direction,'Floor': Floor, 'Dict_Name': Dict_Name, 'Hou_Name': Hou_Name,
                                        'PlateName': PlateName,'ReFinishdate': ReFinishdate, 'Per_Name': Per_Name}
            print(json.dumps(resp_json, sort_keys=True, indent=2,ensure_ascii=False))  # sort_keys=True, indent=2以json格式输出，ensure_ascii=False，编码格式，显示汉字

            return get_json_fydata_dict
            #for js in resp_json:
            #print(resp_json)
            #print(json.dumps(resp_json,sort_keys=True, indent=2,ensure_ascii=False))#sort_keys=True, indent=2以json格式输出，ensure_ascii=False，编码格式，显示汉字
        except BaseException as e:
            logger.error(e)
    #def get_fangyuanxiangqing(self,HouseCode,PriceTotal,PriceSingle,AreaSize,Layout,Direction,Floor,Dict_Name,Hou_Name,PlateName,ReFinishdate,Hou_Remark,Per_Name):
    def get_fangyuanxiangqing(self,**kwargs):
        #self.find_element(*(By.XPATH,'/html/body/div[6]/article/section[2]/section/div/table/tbody/tr/td[2]/label[1]/i')).click()
        HouseCode = self.find_element(*(By.XPATH,kwargs['HouseCode'])).text
        PriceTotal = self.find_element(*(By.XPATH,kwargs['PriceTotal'])).text
        PriceSingle = self.find_element(*(By.XPATH,kwargs['PriceSingle'])).text[:-3]
        AreaSize = self.find_element(*(By.XPATH,kwargs['AreaSize'])).text
        Layout = [ly[:-1] for ly in self.find_element(*(By.XPATH,kwargs['Layout'])).text.split(' ')]
        Direction = self.find_element(*(By.XPATH,kwargs['Direction'])).text
        Floor = self.find_element(*(By.XPATH,kwargs['Floor'])).text.split(' ')[0]
        Dict_Name = self.find_element(*(By.XPATH,kwargs['Dict_Name'])).text
        Hou_Name = self.find_element(*(By.XPATH,kwargs['Hou_Name'])).text
        PlateName = self.find_element(*(By.XPATH,kwargs['PlateName'])).text[4:]
        ReFinishdate = self.find_element(*(By.XPATH,kwargs['ReFinishdate'])).text[:-2]
        Per_Name = self.find_element(*(By.XPATH,kwargs['Per_Name'])).text
        PlateName = PlateName.split(' ')
        for ps in PlateName:
            if ps == '':
                PlateName[PlateName.index(ps)] = ','
        s=''
        for i in range(len(PlateName)):
            s = s + PlateName[i]
        PlateName = s


        #Layout = [ly[:-1] for ly in Layout.split(' ')]
        #ReFinishdate = ReFinishdate[:-2]
        #print(HouseCode,PriceTotal,PriceSingle,AreaSize,Layout,Direction,Floor,Dict_Name,Hou_Name,PlateName,ReFinishdate,Hou_Remark,Per_Name)
        get_fangyuanxiangqing_dict = {'HouseCode': HouseCode,'PriceTotal': PriceTotal,
                         'PriceSingle': PriceSingle,'AreaSize': AreaSize,'Layout': Layout,'Direction': Direction,
                         'Floor': Floor,'Dict_Name': Dict_Name,'Hou_Name': Hou_Name,'PlateName': PlateName,
                         'ReFinishdate': ReFinishdate,'Per_Name': Per_Name}
        return get_fangyuanxiangqing_dict

    def json_fyxq_bijiao(self,fynum,**kwargs):
        try:
            assert self.get_json(fynum=fynum) == self.get_fangyuanxiangqing(**kwargs)
            logger.info('\nJSON: %s \n== \nHTML:%s' % (self.get_json(fynum=fynum),self.get_fangyuanxiangqing(**kwargs)))
        except BaseException as e:
            logger.error('\nJSON: %s \n!= \nHTML:%s' % (self.get_json(fynum=fynum),self.get_fangyuanxiangqing(**kwargs)))



if __name__=="__main__":
    from selenium import webdriver
    import data.urldata as URL

    driver = webdriver.Chrome()
    url = URL.maitian_online_url
    # driver.get(url)
    driver.get('http://fz-test.imtfc.com/esfxq/IH00494493')
    driver.implicitly_wait(2)
    driver.maximize_window()
    fy_xpath_dict = {'HouseCode' : '/html/body/div[6]/article/section[2]/aside/p[4]/em',
    'PriceTotal' : '/html/body/div[6]/article/section[2]/section/ul/li[1]/b',
    'PriceSingle' : '/html/body/div[6]/article/section[2]/section/ul/li[2]/em',
    'AreaSize' : '/html/body/div[6]/article/section[2]/section/ul/li[3]/em',
    'Layout' : '/html/body/div[6]/article/section[2]/section/ul/li[4]/em',
    'Direction' : '/html/body/div[6]/article/section[2]/section/ul/li[5]/em',
    'Floor' : '/html/body/div[6]/article/section[2]/section/ul/li[6]/em',
    'Dict_Name' : '/html/body/div[6]/article/section[2]/section/ul/li[7]/em/a',
    'Hou_Name' : '/html/body/div[6]/article/section[2]/section/ul/li[9]/em/a',
    'PlateName' : '/html/body/div[6]/article/section[2]/section/ul/li[8]',
    'ReFinishdate' : '/html/body/div[6]/article/section[2]/section/ul/li[10]/em',
    'Per_Name' : '/html/body/div[6]/article/section[2]/aside/p[1]/a'}
    dakaifangyuan_url = driver.current_url
    # print('打开的URl：',dakaifangyuan_url)
    if 'I' in  dakaifangyuan_url:
        fybh = dakaifangyuan_url[dakaifangyuan_url.index('I'):]
    print(fybh)
    FangYuanXiangQing(driver).json_fyxq_bijiao(fynum=fybh,**fy_xpath_dict)
