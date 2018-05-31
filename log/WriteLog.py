# _*_ coding: utf-8 _*_

import logging
import os.path
import time

class Logger(object):
    def __init__(self):
        """
        指定保存日志的文件路径，日志级别，以及调用文件将日志存入到指定的文件中
        :param logger:
        """
        # 创建一个logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG )

        # 创建日志名称。
        rq = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
        # os.getcwd()获取当前文件的路径，os.path.dirname()获取指定文件路径的上级路径
        log_path = os.path.dirname(os.getcwd()) + '/log/'
        log_name = log_path + rq + '.log'
        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(log_name,encoding='utf-8')
        fh.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger

if __name__=="__main__":
    Logger().getlog()