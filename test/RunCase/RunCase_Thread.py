#!/usr/bin/python
# coding=utf-8
import unittest,os,time
import HTMLTestRunner
import threading
import sys
#sys.path.append('G:/Web_MaiTianOnLineAutoTest/test')#使用编辑器，要指定当前目录，不然无法执行第20行代码

rootpath = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))[2:]
syspath=sys.path
sys.path=[]
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+'/test')
sys.path.append(rootpath)#将工程根目录加入到python搜索路径中
sys.path.extend([rootpath+'\\'+i for i in os.listdir(rootpath) if i[0]!="."])#将工程目录下的一级目录添加到python搜索路径中
sys.path.extend(syspath)

def creatsuite():
    casedir = []
    list = os.listdir(os.path.dirname(os.getcwd()))#获取当前路径的上一级,这里可以改成绝对路径(要搜索的文件路径)
    for xx in list:
        if "TestCase" in xx:
            casedir.append(xx)
    #print(casedir)

    suite =[]
    for n in casedir:
        testunit = unittest.TestSuite()
        unittest.defaultTestLoader._top_level_dir = None
        discover = unittest.defaultTestLoader.discover(str(n),pattern='*_testcase.py',top_level_dir=None)
        #print(discover)
        for test_suite in discover:
            for test_case in test_suite:
                testunit.addTests(test_case)
        suite.append(testunit)
    #print(suite)
    return suite, casedir

def runcase(suite,casedir):
    #lastPath = os.path.dirname(os.getcwd())#获取当前路径的上一级
    now = time.strftime("%Y-%m-%d %H-%M-%S")

    #filename = "G:/Web_MaiTianOnLineAutoTest/report/" + now + "MT_Test_result.html"
    filename = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + "/report/" + now + "MT_Test_result.html"
    fp = open(filename, 'wb')
    proclist=[]
    s=0

    for i in suite:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="MT_OnLine_Test",description="win7,Chrome")
        proc = threading.Thread(target=runner.run,args=(i,))
        proclist.append(proc)
        s=s+1
    for proc in proclist:
        proc.start()
    for proc in proclist:
        proc.join()
    fp.close()

if __name__ == "__main__":
    path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    File_Path = path + '/report/'
    if not os.path.exists(File_Path):
        os.makedirs(File_Path)
    runtmp=creatsuite()
    #print(runtmp[0])
    #print(runtmp[1])
    runcase(runtmp[0],runtmp[1])
