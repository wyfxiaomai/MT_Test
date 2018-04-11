import os
s
file = "login_testcase.py"
testpath = os.getcwd()
projectName = r'Web_MaiTianOnLineAutoTest'
Tpath = os.path.split(os.path.abspath(file))[0]
print(2,Tpath+os.sep+projectName+os.sep+'test')
print(3,testpath)
test_dir = os.path.dirname(os.path.dirname(__file__))
print(4,test_dir)
print(5,os.path.abspath(file))

import time
time.sleep(10)