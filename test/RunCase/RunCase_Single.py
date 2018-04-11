#!/usr/bin/python

from HTMLTestRunner import HTMLTestRunner
from test.common_package.send_email import new_report
import unittest,time,os,sys
import win32com


sys.path.append(r'G:/MT_online_auto/test')

if __name__=="__main__":
    path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    File_Path = path + '/report/'
    if not os.path.exists(File_Path):
        os.makedirs(File_Path)
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    print('File_Path',File_Path)
    #filename = "G:\\test_result\\result\\" + now + "MT_Test_result.html"
    filename = File_Path + now + " MT_Test_result.html"
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,title="MT_OnLine_Test",description="win7,Chrome")
    test_dir = 'G:/MT_online_auto/test'
   # test_dir = os.path.dirname(os.getcwd())
    print('test_dir ****** ',test_dir)
    now_path = os.getcwd()
    print(1,now_path[:])
    pattern = "login_testcase.py"
    #Tpath = os.path.split(os.path.abspath(pattern))[0]
    Tpath = os.path.dirname(os.path.dirname(os.path.abspath(pattern)))
    print(2,Tpath)

    #pattern =  '*_testcase.py'
    #discover = unittest.defaultTestLoader.discover(test_dir,pattern="bj_secondhouse_testcase.py")
    discover = unittest.defaultTestLoader.discover(test_dir, pattern=pattern)
    runner.run(discover)
    fp.close()
    new_report(File_Path)
    #time.sleep(5)
