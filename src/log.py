# coding: utf-8
__author__ = 'Insality'

from constants import *
from datetime import datetime

class Logger:
    def __init__(self):
        self.to_file = False
        pass

    def get_time(self):
        ''' return current time in format [HH:MM:SS] '''
        time_format = "[%H:%M:%S]: "
        return datetime.now().strftime(time_format)

    def log(self, msg):
        if DEBUG:
            message = self.get_time() + msg
            print(message)




_inst = Logger()
log = _inst.log