#!/usr/bin/python
# -*- coding:UTF-8 -*-
from time import sleep
from selenium.webdriver.common.by import By
from test.common_package.basic import Page
import re
from urllib import request
from bs4 import BeautifulSoup
from data import urldata
import datetime

class SearchCommon(Page):
    # 点击地铁房标题
    def subway_house_click(self,subway_house_xpath):
        self.subway_house_loc = (By.XPATH, subway_house_xpath)
        self.find_element(*self.subway_house_loc).click()

    #获取搜索到的房源总数
    def get_fangyuan_zongshu(self,fangyaunzongshu_xpath=''):
        self.fangyuan_zongshu_loc = (By.XPATH, fangyaunzongshu_xpath)
        self.fy_zongshu = self.find_element(*self.fangyuan_zongshu_loc)
        self.script(self.fy_zongshu)
        return self.fy_zongshu.text #返回房源总数，该返回值为字符串行

    # 获取房源总数为零时的文本提示语
    def get_fy_ling_tishiyu(self,lingtishiyu_xpath=''):
        self.tishiyu_loc = (By.XPATH, lingtishiyu_xpath)
        return self.find_element(*self.tishiyu_loc).text

    # 获取检索条件的文本内容
    def get_jiansuotiaojian_text(self,jiansuoneirong_ID=''):
        jiansuotiaojian_loc = (By.ID, jiansuoneirong_ID)
        return [neirong for neirong in self.find_element(*jiansuotiaojian_loc).text.split('\n')]

    # 获取搜索到的房源列表并解析成列表
    def get_fangyuanliebiao_list(self,fangyuanliebiao_className='',fangyuan_url=''):
        fangyuan_list_loc = (By.CLASS_NAME, fangyuanliebiao_className)
        fangyuan_list = self.find_element(*fangyuan_list_loc)
        fangyuan_info = fangyuan_list.text
        fangyuan_info_str = ''.join(fangyuan_info)
        str_fy = ''
        for s in fangyuan_info_str:  # 去掉获取的房源内容中的\n及空格
            if s == '\n' or s == ' ':
                continue
            else:
                    str_fy = s + str_fy

        re_fangyuan = r'[\d]*万元[\d]*元/㎡|数据暂缺|￥[\d]*/月|[\d]*元/㎡|铁杆粉丝'
        re_c = re.compile(re_fangyuan)
        str_fy_fanzhuan = str_fy[::-1]  # str_fy[::-1]字符串翻转
        re_fangyuan_split = re.split(re_c, str_fy_fanzhuan)  # 解析成列表
        for kongge in re_fangyuan_split:
            if kongge == '':  # 去掉''
                re_fangyuan_split.remove(kongge)
        shoujia = r'([0-9]*)万元'  # 匹配售价
        shoujia_all = self.zhengzebioadashi(pipei_re=shoujia, pipei_str=str_fy_fanzhuan)

        zujin = r'([0-9]*)/月'   #匹配租金
        zujin_all = self.zhengzebioadashi(pipei_re=zujin, pipei_str=str_fy_fanzhuan)

        if 'bj' in fangyuan_url and 'way' in fangyuan_url:
            ershoufang_mianji = r'\|([\d]*|[\d]*\.[\d]*)㎡\|'  # 匹配北京二手房---地铁房面积
        else:
            ershoufang_mianji = r'｜([\d]*|[\d]*\.[\d]*)㎡｜'  # 匹配北京全部二手房面积
        ershoufang_mianji_all = self.zhengzebioadashi(pipei_re=ershoufang_mianji, pipei_str=str_fy_fanzhuan)

        fz_xm_ershoufang_mianji = r'([\d]*|[\d]*\.[\d]*)㎡建筑面积'
        fz_xm_ershoufang_mianji_all = self.zhengzebioadashi(pipei_re=fz_xm_ershoufang_mianji, pipei_str=str_fy_fanzhuan)

        zufang_mianji = r'([\d]*|[\d]*\.[\d]*)㎡\|' #匹配租房面积
        zufang_mianji_all = self.zhengzebioadashi(pipei_re=zufang_mianji, pipei_str=str_fy_fanzhuan)

        if 'bj' in fangyuan_url and 'esfall' in fangyuan_url:
            huxing = r'｜([\d]|[\d]*\.[\d]*)室'  # 匹配北京全部二手房
        else:
            huxing = r'\|([\d]|[\d]*\.[\d]*)室'  # 匹配福州、厦门二手房、别墅户型，匹配北京二手房---地铁房、全部租房、地铁租房
        huxing_all = self.zhengzebioadashi(pipei_re=huxing, pipei_str=str_fy_fanzhuan)

        xiaoqu_junjia = r'([0-9]*)元/㎡'  # 匹配小区均价
        xiaoqujunjia_all = self.zhengzebioadashi(pipei_re=xiaoqu_junjia, pipei_str=str_fy_fanzhuan)

        year_louling = r'([\d]{4})年'
        year_louling_all = self.zhengzebioadashi(pipei_re=year_louling, pipei_str=str_fy_fanzhuan)

        fangchanguwen_name = r'([\W]|[^丝]{2,4})(房产顾问|业务经理)'
        fangchanguwen_name_all = self.zhengzebioadashi(pipei_re=fangchanguwen_name, pipei_str=str_fy_fanzhuan,group=True)
        return re_fangyuan_split, shoujia_all, ershoufang_mianji_all, huxing_all,zujin_all,zufang_mianji_all,xiaoqujunjia_all,year_louling_all,fangchanguwen_name_all,fz_xm_ershoufang_mianji_all  # 返回房源列表内容，匹配到的售价、面积数据

    # 户型转换
    def huxing_zhuanhuan_panduan(self,jiansuoneirong_ID='',fangyaunzongshu_xpath='',fangyuanliebiao_className='',fangyuan_url='',fangyuanlist_huxing=''):
        jiansuo_neirong_liebiao = self.get_jiansuotiaojian_text(jiansuoneirong_ID)
        huxing_dict = {1: '一室', 2: '二室', 3: '三室', 4: '四室', 5: '五室以上'}
        fangyuan_zongshu = self.get_fangyuan_zongshu(fangyaunzongshu_xpath)  # 调用房源总数
        for jshx in jiansuo_neirong_liebiao:
            if '室' in jshx:
                jiansuo_huxing = jshx
                huxing_flag = True
                break
            else:
                huxing_flag = False
        if int(fangyuan_zongshu) == 0:  # 判断房源总数是否为零，如果不为零，房源标识为真
            fangyuan_zongshu_flag = False
        else:
            fangyuan_zongshu_flag = True
        if huxing_flag and fangyuan_zongshu_flag:
            get_huxing_zhi = fangyuanlist_huxing  # 获取房源列表中户型数据
            for hx_key, hx_value in huxing_dict.items():
                if jiansuo_huxing == hx_value:
                    huxing_key = hx_key
            if huxing_key == float(5):
                try:
                    for hxzh in get_huxing_zhi:
                        assert float(hxzh) >= float(huxing_key)
                except:
                    print('%s 搜索不正确' % jiansuo_huxing)
            else:
                try:
                    for hxzh in get_huxing_zhi:
                        assert float(hxzh) == float(huxing_key)
                except:
                    print('%s 搜索不正确' % jiansuo_huxing)
        else:
            if not huxing_flag:
                #print('没有搜索户型内容或为不限')
                pass
            if not fangyuan_zongshu_flag:
                #print('没有搜索到相关房源，相关房源为零')
                pass

    # 获取房源列表URL并点击
    def get_fangyuan_liebiao_url(self,fangyuanurl='', shouye_handle='',fangyaunzongshu_xpath='',fy_xpath_qian_li='',fy_xpath_hou_li='',fylist_range=11):
        liebiao_url = self.driver.current_url
        html = request.urlopen(liebiao_url)  # 打开网页
        soup = BeautifulSoup(html.read(), "html.parser")  # 使用BeautifulSoup获取页面源码
        soup_str = str(soup)  # 将页面源码转换位字符型
        if 'bj' in fangyuanurl:
            url_head = urldata.url_head_bj
        elif 'fz' in fangyuanurl:
            url_head = urldata.url_head_fz
        elif 'xm' in fangyuanurl:
            url_head = urldata.url_head_xm

        for urlindex,urlhead in enumerate(url_head):
            if fangyuanurl == urlhead:
                break

        if 'bj' in fangyuanurl:
            re_a = urldata.re_all_bj[urlindex]
            URL_Head = urldata.fangyuanlink_bj[urlindex]
        elif 'fz' in fangyuanurl:
            re_a = urldata.re_all_fz[urlindex]
            URL_Head = urldata.fangyuanlink_fz[urlindex]
        elif 'xm' in fangyuanurl:
            re_a = urldata.re_all_xm[urlindex]
            URL_Head = urldata.fangyuanlink_xm[urlindex]
        re_a_findall = self.zhengzebioadashi(pipei_re=re_a, pipei_str=soup_str)  # 获取到房源编号
        re_a_findall_quchonghou_list = list(set(re_a_findall))  # 房源编号存在重复，使用list(set())去重
        fangyuan_url = []
        for fangyuanbianhao in re_a_findall_quchonghou_list:  # 将获取到的房源编号与头部链接拼接成完整的URL
            fangyuanlinajie = URL_Head + '/' + fangyuanbianhao
            fangyuan_url.append(fangyuanlinajie)
        handle_1 = self.driver.current_window_handle
        for i in range(1, fylist_range + 1):
            fangyuanzongshu = fangyaunzongshu_xpath  # 定位到房源总数模块
            fy_zs = self.find_element(*(By.XPATH, fangyuanzongshu))
            self.script(fy_zs)
            sleep(1)
            fy_xpath = fy_xpath_qian_li + str(i) + fy_xpath_hou_li  # 依次点击房源列表中的房源
            sleep(1)
            self.find_element(*(By.XPATH, fy_xpath)).click() # 依次点击房源列表中的房源
            all_handle = self.driver.window_handles
            for handle in all_handle:
                if handle_1 != handle and shouye_handle != handle:
                    self.driver.switch_to.window(handle)
                    sleep(2)
                    dakaifangyuan_url = self.driver.current_url
                    try:
                        assert dakaifangyuan_url in fangyuan_url
                    except:
                        print('%s 不正确' % dakaifangyuan_url)
                    self.driver.close()
                    self.driver.switch_to.window(handle_1)
        return

    # 判断房源总数为零
    def fangyuan_zongshu_ling(self,fangyaunzongshu_xpath=''):
        fy_zongshu = self.get_fangyuan_zongshu(fangyaunzongshu_xpath)
        if int(fy_zongshu) == 0:
            return False
        else:
            return True

    # 如果房源总数为零，判断提示语
    def fangyuan_zongshu_ling_panduantishiyu(self,lingtishiyu_xpath=''):
        ling_tishiyu = self.get_fy_ling_tishiyu(lingtishiyu_xpath)
        try:
            assert ling_tishiyu, '抱歉！没有找到相关数据，换个条件试试吧~'
        except BaseException as e:
            print('搜索的房源总数为零时，提示语不正确')

    # 判断搜索内容的正确性
    shouye_link_loc = (By.XPATH, '//div[@id="paging"]/a')
    weiye_link_loc = (By.LINK_TEXT, '尾页')
    xiayiye_link_loc = (By.LINK_TEXT, '下一页')
    weiyeshu_loc = (By.CLASS_NAME, 'on')

    def panduan_sousuo(self,for_3_flag,for_4_flag,fangyuan_url='',fy_xpath_qian_li='',fy_xpath_hou_li='',shouye_handle='', subwaylinesontext='',fangyaunzongshu_xpath='',jiansuoneirong_ID='',fangyuanliebiao_className=''):
        fangyuan_zongshu = self.get_fangyuan_zongshu(fangyaunzongshu_xpath)
        try:
            jiansuo_text = self.get_jiansuotiaojian_text(jiansuoneirong_ID)
        except:
            jiansuo_text = []
        fangyuan_list = self.get_fangyuanliebiao_list(fangyuanliebiao_className=fangyuanliebiao_className,fangyuan_url=fangyuan_url)[0]
        for js_neirong in jiansuo_text:
            if 'bj' in fangyuan_url:
                if '楼层' in js_neirong or subwaylinesontext == js_neirong:  # 从列表中删除低楼层、中楼层、高楼层的检索条件
                    jiansuo_text.remove(js_neirong)
            else:
                if js_neirong == '6层以下':
                    jiansuo_text[jiansuo_text.index(js_neirong)] = '低楼层'
                if js_neirong == '6-12层':
                    jiansuo_text[jiansuo_text.index(js_neirong)] = '中楼层'
                if js_neirong == '12层以上':
                    jiansuo_text[jiansuo_text.index(js_neirong)] = '高楼层'

        shoujia_hanzi_wan_list = ['万', '万以下', '万以上']
        zujin_hanzi_yuan_list = ['元', '元以下', '以上']
        mianji_hanzi_ping_list = ['平', '平以下', '平以上']
        louling_hanzi_list = ['年以内','年以内','年以上']
        fangyuan_list_hanzi_shoujia = self.get_fangyuanliebiao_list(fangyuanliebiao_className=fangyuanliebiao_className,fangyuan_url=fangyuan_url)[1]
        if 'bj' in fangyuan_url:
            fangyuan_list_hanzi_mianji_ershoufang = self.get_fangyuanliebiao_list(fangyuanliebiao_className=fangyuanliebiao_className,fangyuan_url=fangyuan_url)[2]
        else:
            fangyuan_list_hanzi_mianji_ershoufang = self.get_fangyuanliebiao_list(fangyuanliebiao_className=fangyuanliebiao_className,fangyuan_url=fangyuan_url)[9]
        fangyuan_list_hanzi_mianji_zufang = self.get_fangyuanliebiao_list(fangyuanliebiao_className=fangyuanliebiao_className,fangyuan_url=fangyuan_url)[5]
        fangyuan_list_hanzi_zujin = self.get_fangyuanliebiao_list(fangyuanliebiao_className=fangyuanliebiao_className,fangyuan_url=fangyuan_url)[4]
        fangyuan_list_hanzi_junjia = self.get_fangyuanliebiao_list(fangyuanliebiao_className=fangyuanliebiao_className,fangyuan_url=fangyuan_url)[6]
        fangyuan_list_hanzi_year = self.get_fangyuanliebiao_list(fangyuanliebiao_className=fangyuanliebiao_className,fangyuan_url=fangyuan_url)[7]
        fangchanguwen_name = self.get_fangyuanliebiao_list(fangyuanliebiao_className=fangyuanliebiao_className,fangyuan_url=fangyuan_url)[8]    #获取房产顾问姓名
        fangyuanlist_huxing = self.get_fangyuanliebiao_list(fangyuanliebiao_className=fangyuanliebiao_className, fangyuan_url=fangyuan_url)[3]

        peizhi_list = ['沙发','电视','冰箱','空调','床','书桌','茶几','餐桌','衣柜','洗碗机','烤箱','洗衣机','热水器','网络','带车位']
        for peizhi in jiansuo_text:
            for pzlist in peizhi_list:
                if pzlist == peizhi:
                    jiansuo_text.remove(peizhi)

        if int(fangyuan_zongshu) <= 10:
            for fy_list in fangyuan_list:
                for js_list in jiansuo_text:
                    if js_list == '临近地铁':
                        js_list = '号线'
                    if '万' in js_list or '平' in js_list or '室' in js_list or '元' in js_list or '以下' in js_list or '年以内' in js_list or '年以上' in js_list or '有' in js_list or '无' in js_list or '装修' in js_list or '毛坯房' in js_list:
                        continue
                    try:
                        assert js_list in fy_list
                       # print('%s 包含在 %s' % (js_list,fy_list))
                    except BaseException as e:
                        print('%s 不包含在 %s' % (js_list, fy_list))

            if 'xqall' in fangyuan_url: #小区
                #print('******均价******')
                self.panduan_mianji_shoujia_zujin(for_3_flag=for_3_flag,for_4_flag=for_4_flag,fangyuanurl=fangyuan_url,hanzilist=shoujia_hanzi_wan_list,fangyuan_list_shuju=fangyuan_list_hanzi_junjia,jiansuoneirong_ID=jiansuoneirong_ID, fangyaunzongshu_xpath=fangyaunzongshu_xpath)
               # print('******楼龄******')
                self.panduan_mianji_shoujia_zujin(for_3_flag=for_3_flag,for_4_flag=for_4_flag,fangyuanurl=fangyuan_url, hanzilist=louling_hanzi_list,fangyuan_list_shuju=fangyuan_list_hanzi_year,jiansuoneirong_ID=jiansuoneirong_ID,fangyaunzongshu_xpath=fangyaunzongshu_xpath)
                #print('******URL******')
                #print('房源URL',fangyuan_url)
                self.get_fangyuan_liebiao_url(fangyuanurl=fangyuan_url, fy_xpath_qian_li=fy_xpath_qian_li,fy_xpath_hou_li=fy_xpath_hou_li,fangyaunzongshu_xpath=fangyaunzongshu_xpath, shouye_handle=shouye_handle,fylist_range=len(fangyuan_list))

            elif 'zfall' in fangyuan_url:#租房
               # print('******租金******')
                self.panduan_mianji_shoujia_zujin(for_3_flag=for_3_flag,for_4_flag=for_4_flag,hanzilist=zujin_hanzi_yuan_list,fangyuan_list_shuju=fangyuan_list_hanzi_zujin,jiansuoneirong_ID=jiansuoneirong_ID, fangyaunzongshu_xpath=fangyaunzongshu_xpath)
               # print('******面积******')
                self.panduan_mianji_shoujia_zujin(for_3_flag=for_3_flag,for_4_flag=for_4_flag,hanzilist=mianji_hanzi_ping_list,fangyuan_list_shuju=fangyuan_list_hanzi_mianji_zufang,jiansuoneirong_ID=jiansuoneirong_ID,fangyaunzongshu_xpath=fangyaunzongshu_xpath)
               # print('******户型******')
                self.huxing_zhuanhuan_panduan(jiansuoneirong_ID=jiansuoneirong_ID,fangyaunzongshu_xpath=fangyaunzongshu_xpath,fangyuanliebiao_className=fangyuanliebiao_className,fangyuanlist_huxing=fangyuanlist_huxing)
              #  print('******URL******')
                self.get_fangyuan_liebiao_url(fangyuanurl=fangyuan_url, fy_xpath_qian_li=fy_xpath_qian_li,fy_xpath_hou_li=fy_xpath_hou_li,fangyaunzongshu_xpath=fangyaunzongshu_xpath, shouye_handle=shouye_handle,fylist_range=len(fangyuan_list))

            elif 'bkesf' in fangyuan_url:#房产顾问
                self.panduan_fangchanguwen(fanchanguwe_name=fangchanguwen_name, fy_xpath_qian_li=fy_xpath_qian_li,fy_xpath_hou_li=fy_xpath_hou_li,fangyaunzongshu_xpath=fangyaunzongshu_xpath, shouye_handle=shouye_handle,fylist_range=len(fangyuan_list))

            elif 'esfall' in fangyuan_url or 'esfbslb' in fangyuan_url:#二手房、别墅
              #  print('******售价******')
                self.panduan_mianji_shoujia_zujin(for_3_flag=for_3_flag,for_4_flag=for_4_flag,hanzilist=shoujia_hanzi_wan_list,fangyuan_list_shuju=fangyuan_list_hanzi_shoujia,jiansuoneirong_ID=jiansuoneirong_ID, fangyaunzongshu_xpath=fangyaunzongshu_xpath)
              #  print('******面积******')
                self.panduan_mianji_shoujia_zujin(for_3_flag=for_3_flag,for_4_flag=for_4_flag,hanzilist=mianji_hanzi_ping_list,fangyuan_list_shuju=fangyuan_list_hanzi_mianji_ershoufang,jiansuoneirong_ID=jiansuoneirong_ID, fangyaunzongshu_xpath=fangyaunzongshu_xpath)
              #  print('******户型******')
                self.huxing_zhuanhuan_panduan(jiansuoneirong_ID=jiansuoneirong_ID,fangyaunzongshu_xpath=fangyaunzongshu_xpath,fangyuanliebiao_className=fangyuanliebiao_className,fangyuanlist_huxing=fangyuanlist_huxing)
              #  print('******URL******')
                self.get_fangyuan_liebiao_url(fangyuanurl=fangyuan_url,fy_xpath_qian_li=fy_xpath_qian_li,fy_xpath_hou_li=fy_xpath_hou_li,fangyaunzongshu_xpath=fangyaunzongshu_xpath,shouye_handle=shouye_handle,fylist_range=len(fangyuan_list))
        else:  # 如果房源总数大于10条检查翻页后的内容
            self.find_element(*self.weiye_link_loc).click()  # 点击尾页
            sleep(2)
            zongshu_ye = self.find_element(*self.weiyeshu_loc).text  # 获取总页数
            self.find_element(*self.shouye_link_loc).click()  # 点首页
            for zs in range(int(zongshu_ye)):  # 生成页码
                fanyehoufangyuan_list = self.get_fangyuanliebiao_list(fangyuanliebiao_className=fangyuanliebiao_className,fangyuan_url=fangyuan_url)[0]  # 获取翻页后的房源列表内容
                fanyehou_fangyuan_list_hanzi_shoujia = self.get_fangyuanliebiao_list(fangyuanliebiao_className=fangyuanliebiao_className,fangyuan_url=fangyuan_url)[1]
                fanyehou_fangyuan_list_hanzi_mianji_ershoufang = self.get_fangyuanliebiao_list(fangyuanliebiao_className=fangyuanliebiao_className,fangyuan_url=fangyuan_url)[2]
                fanyehou_fangyuan_list_hanzi_mianji_zufang = self.get_fangyuanliebiao_list(fangyuanliebiao_className=fangyuanliebiao_className,fangyuan_url=fangyuan_url)[5]
                fanyehou_fangyuan_list_hanzi_zujin = self.get_fangyuanliebiao_list(fangyuanliebiao_className=fangyuanliebiao_className,fangyuan_url=fangyuan_url)[4]
                fanyehou_fangyuan_list_hanzi_junjia = self.get_fangyuanliebiao_list(fangyuanliebiao_className=fangyuanliebiao_className,fangyuan_url=fangyuan_url)[6]
                fanyehou_fangyuan_list_hanzi_year = self.get_fangyuanliebiao_list(fangyuanliebiao_className=fangyuanliebiao_className,fangyuan_url=fangyuan_url)[7]
                fangchanguwen_name = self.get_fangyuanliebiao_list(fangyuanliebiao_className=fangyuanliebiao_className,fangyuan_url=fangyuan_url)[8]
                fangyuanlist_huxing = self.get_fangyuanliebiao_list(fangyuanliebiao_className=fangyuanliebiao_className,fangyuan_url=fangyuan_url)[3]
                for fy_list in fanyehoufangyuan_list:
                    for js_list in jiansuo_text:
                        if js_list == '临近地铁':
                            js_list = '号线'
                        if '万' in js_list or '平' in js_list or '室' in js_list or '元' in js_list or '以下' in js_list or '年以内' in js_list or '年以上' in js_list or '有' in js_list or '无' in js_list or '装修' in js_list or '毛坯房' in js_list:
                            continue
                        try:
                            assert js_list in fy_list
                        except BaseException as e:
                            print('%s 不包含在 %s' % (js_list, fy_list))
                #print('过滤后搜索内容：', jiansuo_text)
                if 'xqall' in fangyuan_url:  # 小区
                 #   print('******均价******')
                    self.panduan_mianji_shoujia_zujin(for_3_flag=for_3_flag,for_4_flag=for_4_flag,fangyuanurl=fangyuan_url,hanzilist=shoujia_hanzi_wan_list,fangyuan_list_shuju=fanyehou_fangyuan_list_hanzi_junjia,jiansuoneirong_ID=jiansuoneirong_ID,fangyaunzongshu_xpath=fangyaunzongshu_xpath)
                #    print('******楼龄******')
                    self.panduan_mianji_shoujia_zujin(for_3_flag=for_3_flag,for_4_flag=for_4_flag,fangyuanurl=fangyuan_url, hanzilist=louling_hanzi_list,fangyuan_list_shuju=fanyehou_fangyuan_list_hanzi_year,jiansuoneirong_ID=jiansuoneirong_ID,fangyaunzongshu_xpath=fangyaunzongshu_xpath)
                 #   print('******URL******')
                    self.get_fangyuan_liebiao_url(fangyuanurl=fangyuan_url, fy_xpath_qian_li=fy_xpath_qian_li,fy_xpath_hou_li=fy_xpath_hou_li,fangyaunzongshu_xpath=fangyaunzongshu_xpath,shouye_handle=shouye_handle, fylist_range=len(fanyehoufangyuan_list))

                elif 'zfall' in fangyuan_url:#租房
                 #   print('******租金******')
                    self.panduan_mianji_shoujia_zujin(for_3_flag=for_3_flag,for_4_flag=for_4_flag,hanzilist=zujin_hanzi_yuan_list,fangyuan_list_shuju=fanyehou_fangyuan_list_hanzi_zujin,jiansuoneirong_ID=jiansuoneirong_ID,fangyaunzongshu_xpath=fangyaunzongshu_xpath)
                  #  print('******面积******')
                    self.panduan_mianji_shoujia_zujin(for_3_flag=for_3_flag,for_4_flag=for_4_flag,hanzilist=mianji_hanzi_ping_list,fangyuan_list_shuju=fanyehou_fangyuan_list_hanzi_mianji_zufang,jiansuoneirong_ID=jiansuoneirong_ID,fangyaunzongshu_xpath=fangyaunzongshu_xpath)
                  #  print('******户型******')
                    self.huxing_zhuanhuan_panduan(jiansuoneirong_ID=jiansuoneirong_ID,fangyaunzongshu_xpath=fangyaunzongshu_xpath,fangyuanliebiao_className=fangyuanliebiao_className,fangyuanlist_huxing=fangyuanlist_huxing)
                  #  print('******URL******')
                    self.get_fangyuan_liebiao_url(fangyuanurl=fangyuan_url, fy_xpath_qian_li=fy_xpath_qian_li,fy_xpath_hou_li=fy_xpath_hou_li,fangyaunzongshu_xpath=fangyaunzongshu_xpath,shouye_handle=shouye_handle, fylist_range=len(fanyehoufangyuan_list))

                elif 'bkesf'in fangyuan_url:#房产顾问
                  #  print('******房产顾问******')
                    self.panduan_fangchanguwen(fanchanguwe_name=fangchanguwen_name, fy_xpath_qian_li=fy_xpath_qian_li,fy_xpath_hou_li=fy_xpath_hou_li,fangyaunzongshu_xpath=fangyaunzongshu_xpath,shouye_handle=shouye_handle, fylist_range=len(fanyehoufangyuan_list))

                elif 'esfall' in fangyuan_url or 'esfbslb' in fangyuan_url:  # 二手房、别墅
                  #  print('******售价******')
                    self.panduan_mianji_shoujia_zujin(for_3_flag=for_3_flag,for_4_flag=for_4_flag,hanzilist=shoujia_hanzi_wan_list,fangyuan_list_shuju=fanyehou_fangyuan_list_hanzi_shoujia,jiansuoneirong_ID=jiansuoneirong_ID,fangyaunzongshu_xpath=fangyaunzongshu_xpath)
                 #   print('******面积******')
                    self.panduan_mianji_shoujia_zujin(for_3_flag=for_3_flag,for_4_flag=for_4_flag,hanzilist=mianji_hanzi_ping_list,fangyuan_list_shuju=fanyehou_fangyuan_list_hanzi_mianji_ershoufang,jiansuoneirong_ID=jiansuoneirong_ID,fangyaunzongshu_xpath=fangyaunzongshu_xpath)
                  #  print('******户型******')
                    self.huxing_zhuanhuan_panduan(jiansuoneirong_ID=jiansuoneirong_ID,fangyaunzongshu_xpath=fangyaunzongshu_xpath,fangyuanliebiao_className=fangyuanliebiao_className,fangyuanlist_huxing=fangyuanlist_huxing)
                  #  print('******URL******')
                    self.get_fangyuan_liebiao_url(fangyuanurl=fangyuan_url, fy_xpath_qian_li=fy_xpath_qian_li,fy_xpath_hou_li=fy_xpath_hou_li,fangyaunzongshu_xpath=fangyaunzongshu_xpath, shouye_handle=shouye_handle,fylist_range=len(fanyehoufangyuan_list))

                self.yeshu_link_loc = (By.LINK_TEXT, str(zs + 1))
                self.find_element(*self.xiayiye_link_loc).click()  # 点击下一页
                sleep(1)
        return '****** panduan_sousuo() 方法调用结束 ******'

    #判断点击房产顾问卡片页面跳转的正确性
    def panduan_fangchanguwen(self,fanchanguwe_name='', shouye_handle='',fangyaunzongshu_xpath='',fy_xpath_qian_li='',fy_xpath_hou_li='',fylist_range=11):
        handle_1 = self.driver.current_window_handle
        for i in range(1, fylist_range + 1):
            fangyuanzongshu = fangyaunzongshu_xpath  # 定位到房源总数模块
            fy_zs = self.find_element(*(By.XPATH, fangyuanzongshu))
            self.script(fy_zs)
            sleep(1)
            fy_xpath = fy_xpath_qian_li + str(i) + fy_xpath_hou_li  # 依次点击顾问列表中的顾问卡片
            sleep(1)
            self.find_element(*(By.XPATH, fy_xpath)).click()
            all_handle = self.driver.window_handles
            for handle in all_handle:
                if handle_1 != handle and shouye_handle != handle:
                    self.driver.switch_to.window(handle)
                    sleep(2)
                    self.fg_name_loc = (By.XPATH, '/html/body/section[2]/div/ul/li[1]/a')
                    fg_name = self.find_element(*self.fg_name_loc).text
                    try:
                        assert fg_name in fanchanguwe_name
                    except:
                        print('%s 不正确' % fg_name)
                    self.driver.close()
                    self.driver.switch_to.window(handle_1)

    #定义判断面积、租金、售价
    def panduan_mianji_shoujia_zujin(self,for_3_flag,for_4_flag,hanzilist,fangyuan_list_shuju, jiansuoneirong_ID,fangyaunzongshu_xpath,fangyuanurl=''):
        jiansuo_neirong_liebiao = self.get_jiansuotiaojian_text(jiansuoneirong_ID)  # 获取搜索内容
        get_fangyuan_list_shuju = fangyuan_list_shuju  # 获取房源列表内容中的需要判断的数据
        fangyuan_zongshu = self.get_fangyuan_zongshu(fangyaunzongshu_xpath)  # 调用房源总数
        if int(fangyuan_zongshu) == 0:  # 判断房源总数是否为零，如果不为零，房源标识为真
            fangyuan_zongshu_flag = False
        else:
            fangyuan_zongshu_flag = True
        hanzi_list = hanzilist

        for jian_s in jiansuo_neirong_liebiao:
            if '小于等于' in jian_s:
                jiansuo_neirong_liebiao[jiansuo_neirong_liebiao.index(jian_s)] = '0-' + jian_s[4:]
            if '大于等于' in jian_s:
                jiansuo_neirong_liebiao[jiansuo_neirong_liebiao.index(jian_s)] = jian_s[4:9] + '-99999万'

        for shoujia_mianji_zujin in jiansuo_neirong_liebiao:  # 判断检索内容中是否有要判断的数据字段
            if hanzilist[0] in shoujia_mianji_zujin or hanzilist[2] in shoujia_mianji_zujin:  # 如果有，该字段标识为真
                jiansuoshuju_flag = True
                break
            else:
                jiansuoshuju_flag = False
        if jiansuoshuju_flag and fangyuan_zongshu_flag:
            for jiansuoshuju in jiansuo_neirong_liebiao:
                for hanzi in hanzi_list:
                    if hanzi in jiansuoshuju:
                        jiansuoshuju_shanchuhanzi = jiansuoshuju.strip(hanzi)
                        jiansuoshuju_shanchuhanzi_list = [mj for mj in jiansuoshuju_shanchuhanzi.split('-')]
                        hanzi_index = hanzi_list.index(hanzi)
            hanzi_len = len(jiansuoshuju_shanchuhanzi_list)
            for erciguolv in jiansuoshuju_shanchuhanzi_list:#二次过滤
                for hanzi in hanzi_list:
                    if hanzi in erciguolv:
                        jiansuoshuju_shanchuhanzi_list[jiansuoshuju_shanchuhanzi_list.index(erciguolv)] = erciguolv[0:len(erciguolv)-len(hanzi)]
            if '年' in  hanzi_list[0]:#判断楼龄
                today = datetime.date.today()
                year_today = today.year #获取当前年份
                if hanzi_index == 0 or hanzi_index == 1:
                    for fy_year in get_fangyuan_list_shuju:
                        year = year_today - int(fy_year)
                        try:
                            assert year <= int(jiansuoshuju_shanchuhanzi_list[0])
                        except BaseException as e:
                            print('%s 楼龄搜索错误' % jiansuo_neirong_liebiao)
                if hanzi_index == 2:
                    for fy_year in get_fangyuan_list_shuju:
                        year = year_today - int(fy_year)    #当前年份减去房源列表中获取的年份，差值与搜索内容比较
                        try:
                            assert year >= int(jiansuoshuju_shanchuhanzi_list[0])
                        except BaseException as e:
                            print('%s 楼龄搜索错误' % jiansuo_neirong_liebiao)

            else:#判断售价、租金、面积
                if hanzi_len == 2:
                    num_min = float(jiansuoshuju_shanchuhanzi_list[0])
                    num_max = float(jiansuoshuju_shanchuhanzi_list[1])
                else:
                    if hanzi_index == 1:
                        num_min = 0
                        num_max = float(jiansuoshuju_shanchuhanzi_list[0])
                    elif hanzi_index == 2:
                        num_min = float(jiansuoshuju_shanchuhanzi_list[0])
                        num_max = 99999

                global num_min,num_max
                if 'xqall' in fangyuanurl:
                    num_min = num_min * 10000
                    num_max = num_max * 10000

                if for_3_flag == True or for_4_flag == True:
                    for fanyuanshuju in get_fangyuan_list_shuju:
                        print(fanyuanshuju)
                        try:
                            assert num_min <= float(fanyuanshuju) <= num_max
                            #print('%s 内容在 %s - %s 搜索范围内' % (fanyuanshuju, num_min, num_max))
                        except BaseException as e:
                            print('%s 内容不在 %s - %s 搜索范围内' % (fanyuanshuju, num_min, num_max))
        else:
            if not jiansuoshuju_flag:
                #print('没有搜索内容或搜索内容为不限')
                pass
            if not fangyuan_zongshu_flag:
                #print('没有搜索到相关房源，相关房源为零')
                pass

    #判断排序的正确性
    """
    paixu_list()在调用时，传入要判断的名称（总价、单价、面积、租金、楼龄、建成年代、均价、待售量、成交量、
    从业年限、服务客户、近期成交、铁杆粉丝、在售房源量），该方法不能判断星级、最新排序。
    """
    paixuqian = []
    paixuhou = []
    def paixu_list(self,paixuname,fangyaunzongshu_xpath="//p[@class='search_result']/span"):
        #starttime = time.strftime("%Y-%m-%d %H:%M:%S")
        #ST = datetime.datetime.strptime(starttime,"%Y-%m-%d %H:%M:%S")
        #print('开始时间：',starttime)
        page_url = self.driver.current_url
        if paixuname == '总价':
            re_zhengze =  r'([0-9]*)万元'
        elif paixuname == '单价':
            re_zhengze = r'([\d]*)元/㎡'
        elif paixuname == '面积':
            if 'fz' in page_url or 'xm' in  page_url:
                re_zhengze = r'([\d]*|[\d]*\.[\d]*)㎡建筑面积'
            else:
                re_zhengze = r'\|([\d]*|[\d]*\.[\d]*)㎡\||([\d]*|[\d]*\.[\d]*)㎡\|'
        elif paixuname == '租金':
            re_zhengze = r'([0-9]*)/月'
        elif paixuname == '楼龄' or paixuname == '建成年代':
            re_zhengze = r'([\d]{4})年'
        elif paixuname == '均价':
            re_zhengze = r'([0-9]*)元/㎡'
        elif paixuname == '待售量':
            re_zhengze = r'([\d]*)套在售套数'
        elif paixuname == '成交量':
            re_zhengze = r'累计成交([\d]*)套'
        elif paixuname == '从业年限':
            re_zhengze = r'([^:]|[^\.][\d]*)从业年限'
        elif paixuname == '服务客户':
            re_zhengze = r'([\d]*)服务客户'
        elif paixuname == '近期成交':
            re_zhengze = r'([\d]*)近期成交'
        elif paixuname == '铁杆粉丝':
            re_zhengze = r'([\d]*)铁杆粉丝'
        elif paixuname == '在售房源量':
            re_zhengze = r'([\d]*)待售房源'

        fangyuanzongshu = self.get_fangyuan_zongshu(fangyaunzongshu_xpath=fangyaunzongshu_xpath)
        if int(fangyuanzongshu) <= 10:
            self.paixuqian = self.get_paixuneirong(re_zhengze=re_zhengze)
            #print('排序前：',self.paixuqian)
            if paixuname == '从业年限':
                for date in self.paixuqian:
                    if ':'in date:
                        self.paixuqian[self.paixuqian.index(date)] = date[3:]
            self.paixuqian = [float(e) for e in self.paixuqian]
            if paixuname == '楼龄':
                self.paixuqian.sort(reverse=True)
            else:
                self.paixuqian.sort()
            #print('排序前sort：', self.paixuqian)
            self.find_element(*(By.LINK_TEXT, paixuname)).click()
            self.paixuhou = self.get_paixuneirong(re_zhengze=re_zhengze)
            if paixuname == '从业年限':
                for date in self.paixuhou:
                    if ':'in date:
                        self.paixuhou[self.paixuhou.index(date)] = date[3:]
            self.paixuhou = [float(e) for e in self.paixuhou]
            #print('排序后：',self.paixuhou)
        else:
            self.find_element(*self.weiye_link_loc).click()  # 点击尾页
            sleep(2)
            zongshu_ye = self.find_element(*self.weiyeshu_loc).text  # 获取总页数
            """获取排序前的内容"""
            self.find_element(*self.shouye_link_loc).click()  # 点首页
            for zs in range(int(zongshu_ye)):  # 生成页码
                getshuju_qian = self.get_paixuneirong(re_zhengze=re_zhengze)
                for data_Q in getshuju_qian:
                    self.paixuqian.append(data_Q)
                self.yeshu_link_loc = (By.LINK_TEXT, str(zs + 1))
                self.find_element(*self.xiayiye_link_loc).click()  # 点击下一页
                sleep(1)
            #print('排序前：', self.paixuqian)
            if paixuname == '从业年限':
                for date in self.paixuqian:
                    if ':'in date:
                        self.paixuqian[self.paixuqian.index(date)] = date[3:]
            self.paixuqian = [float(e) for e in self.paixuqian]
            if paixuname == '楼龄':
                self.paixuqian.sort(reverse=True)
            else:
                self.paixuqian.sort()
            #print('排序前sort：', self.paixuqian)
            """获取点击排序后的内容"""
            self.find_element(*self.shouye_link_loc).click()  # 点首页
            self.find_element(*(By.LINK_TEXT, paixuname)).click()
            for zs in range(int(zongshu_ye)):  # 生成页码
                getshuju_hou = self.get_paixuneirong(re_zhengze=re_zhengze)
                for data_H in getshuju_hou:
                    self.paixuhou.append(data_H)
                self.yeshu_link_loc = (By.LINK_TEXT, str(zs + 1))
                self.find_element(*self.xiayiye_link_loc).click()  # 点击下一页
                sleep(1)
            #print('排序后：', self.paixuhou)
            if paixuname == '从业年限':
                for date in self.paixuhou:
                    if ':'in date:
                        self.paixuhou[self.paixuhou.index(date)] = date[3:]
            self.paixuhou = [float(e) for e in self.paixuhou]
            #print('排序后_转换：', self.paixuhou)
        try:
            assert self.paixuhou == self.paixuqian
            #print('排序正确')
        except BaseException as e:
            print('排序错误')
        #endtime = time.strftime("%Y-%m-%d %H:%M:%S")
        #ET = datetime.datetime.strptime(endtime, "%Y-%m-%d %H:%M:%S")
        #print('结束时间：', endtime)
        #print('耗时：',ET-ST)
        #return True

    # 使用正则表达式获取需要排序的内容值
    def get_paixuneirong(self,fangyuanliebiao_className='list_wrap',re_zhengze=''):
        fangyuan_list_loc = (By.CLASS_NAME, fangyuanliebiao_className)
        fangyuan_list = self.find_element(*fangyuan_list_loc)
        fangyuan_info = fangyuan_list.text
        fangyuan_info_str = ''.join(fangyuan_info)
        str_fy = ''
        for s in fangyuan_info_str:  # 去掉获取的房源内容中的\n及空格
            if s == '\n' or s == ' ':
                continue
            else:
                    str_fy = s + str_fy
        str_fy_fanzhuan = str_fy[::-1]  # str_fy[::-1]字符串翻转
        #print('列表信息',str_fy_fanzhuan)
        zhengze = re_zhengze  # 匹配排序内容
        paixu_re = self.zhengzebioadashi(pipei_re=zhengze, pipei_str=str_fy_fanzhuan)
        return paixu_re

if __name__=="__main__":
    from selenium import webdriver
    import data.urldata as URL

    driver = webdriver.Chrome()
    url = URL.maitian_online_url
    #driver.get(url)
    driver.get('http://xm-test.imtfc.com/esfall/R1/S1')
    driver.implicitly_wait(2)
    driver.maximize_window()
    #SearchCommon(driver).panduan_zujin(jiansuoneirong_ID='SearchHouseTerm',fangyaunzongshu_xpath='/html/body/section[2]/div[2]/p/span',fangyuanliebiao_className='list_wrap')
   # SearchCommon(driver).paixu_list(paixuname='服务客户')

   # a=SearchCommon(driver).get_fangyuanliebiao_list(fangyuanliebiao_className='list_wrap',
  #                                       fangyuan_url='http://xm-test.imtfc.com/esfall')
   # print(a[3])
    SearchCommon(driver).panduan_sousuo(fangyuan_url='http://xm-test.imtfc.com/esfall/R1/S1',
                    fangyaunzongshu_xpath="//p[@class='search_result']/span",
                    fangyuanliebiao_className='list_wrap',
                      jiansuoneirong_ID='SearchHouseTerm', )