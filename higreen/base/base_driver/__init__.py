# -*- coding: utf-8 -*-
# @Time    : 2021/12/4 10:11
# @Author  : 牛逼哥
# @FileName: te.py
# @Software: PyCharm
import os
isdevices = os.popen(r'adb devices', 'r')

devices = isdevices.read()
print(devices[24:-9].replace('\n', '').replace('\r', '').replace(' ', ''))
devices1 = devices[24:-9].replace('\n', '').replace('\r', '').replace(' ', '')
#print(devices[24:-8])#读取执行后返回内容
if devices1 in '127.0.0.1:62001':
    print("123456")

else:
    print('weikai')
