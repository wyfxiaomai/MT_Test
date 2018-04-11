#!/usr/bin/python
# -*- coding:UTF-8 -*-

maitian_online_url = 'http://bj-test.imtfc.com/VIEW/Index/Index2.html'  #测试环境
#maitian_online_url = 'http://www.maitian.cn'   #正式环境地址

#测试环境
urlhead_bj = 'http://bj-test.imtfc.com/'
urlhead_fz = 'http://fz-test.imtfc.com/'
urlhead_xm = 'http://xm-test.imtfc.com/'

"""
#正式环境
urlhead_bj = 'http://bj.maitian.cn/'
urlhead_fz = 'http://fz.maitian.cn/'
urlhead_xm = 'http://xm.maitian.cn/'
"""

#用于判断点击的是那个城市的那种类型
url_head_bj = [urlhead_bj + 'esfall',urlhead_bj + 'zfall',urlhead_bj + 'xqall']
url_head_fz = [urlhead_fz + 'esfall',urlhead_fz + 'esfbslb/VH1',urlhead_fz + 'xqall']
url_head_xm = [urlhead_xm + 'esfall',urlhead_xm + 'esfbslb/VALL1',urlhead_xm + 'xqall']

#用于从页面源码中获取房源编号
re_all_bj = ['<a href="[\s]*/esfxq/(IFY[\d]*)','<a href="[\s]*/zfxq/(I[\d]*)','<a href="[\s]*/xqxqgk/([\w]*)']
re_all_fz = ['<a href="[\s]*/esfxq/([\w]*)','<a href="[\s]*/esfbsxq/([\w]*)','<a href="[\s]*/xqxqgk/([\w]*)']
re_all_xm = ['<a href="[\s]*/esfxq/([\w]*)','<a href="[\s]*/esfbsxq/([\w]*)','<a href="[\s]*/xqxqgk/([\w]*)']

#用于与获取的房源编号拼接成房源详情页的URL
fangyuanlink_bj = [urlhead_bj + 'esfxq',urlhead_bj + 'zfxq',urlhead_bj + 'xqxqgk']
fangyuanlink_fz = [urlhead_fz + 'esfxq',urlhead_fz + 'esfbsxq',urlhead_fz + 'xqxqgk']
fangyuanlink_xm = [urlhead_xm + 'esfxq',urlhead_xm + 'esfbsxq',urlhead_xm + 'xqxqgk']


