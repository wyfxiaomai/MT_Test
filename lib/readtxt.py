#!/usr/bin/python
# -*- coding:UTF-8 -*-
import config
from data import usedata
def readtxt(file_name):
    filename = usedata.filepath + file_name
    with open(filename,"r", encoding="utf-8") as f:
        line = [line.strip('\n') for line in f]
    return line

"""
def readtxt(file_name):
    filename = usedata.filepath + file_name
    file = open(filename,"r", encoding="utf-8")
    lines = file.readlines()#读取全部内容
    line = [line.strip('\n') for line in lines]
    file.close()
    return line
"""
if __name__=="__main__":
    print(readtxt('shouye_searchtext'))