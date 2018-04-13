#!/usr/bin/python
# -*- encoding:UTF-8 -*-
import unittest,time,os,sys
#rootpath=str('/Web_MaiTianOnLineAutoTest/')
rootpath = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))[2:]
syspath=sys.path
sys.path=[]
sys.path.append(rootpath)#将工程根目录加入到python搜索路径中
sys.path.extend([rootpath+'\\'+i for i in os.listdir(rootpath) if i[0]!="."])#将工程目录下的一级目录添加到python搜索路径中
sys.path.extend(syspath)
#print('sys.path',sys.path)
from HTMLTestRunner import HTMLTestRunner
from test.common_package.send_email import new_report


if __name__=="__main__":
    path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    File_Path = path + '/report/'
    if not os.path.exists(File_Path):
        os.makedirs(File_Path)
    now = time.strftime("%Y-%m-%d %H-%M-%S")
  #  print('File_Path',File_Path)
    #filename = "G:\\test_result\\result\\" + now + "MT_Test_result.html"
    filename = File_Path + now + " MT_Test_result.html"
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,title="MT_OnLine_Test",description="win7,Chrome")
    test_dir = '/MT_Auto_get_new_script/test'
   # print('test_dir ****** ',test_dir)
    now_path = os.getcwd()
   # print(1,now_path[:])
    pattern = "login_testcase.py"
    Tpath = os.path.dirname(os.path.dirname(os.path.abspath(pattern)))
    #print(2,Tpath)

    #pattern =  '*_testcase.py'
    #discover = unittest.defaultTestLoader.discover(test_dir,pattern="bj_secondhouse_testcase.py")
    #print('sys.path', sys.path[7])
    discover = unittest.defaultTestLoader.discover(rootpath, pattern=pattern)
    runner.run(discover)
    fp.close()
    new_report(File_Path)
