# -*- coding: utf-8 -*-
# @Time    : 2021/12/4 10:11
# @Author  :
# @FileName: te.py
# @Software: PyCharm
import os


def adb_execute(appActivity):
    isdevices = os.popen(r'adb shell dumpsys window | findstr mCurrentFocus', 'r')
    devices = isdevices.read()
    # appActivity = devices[24:-2].replace('\n', '').replace('\r', '').replace(' ', '').split('/')[1]
    # print(appActivity)
    if devices.find(appActivity) != -1:
        return True
    else:
        return False


def adb_keyevent(keyid):
    """
    :param keyid: 按键标识id
    :return:
    """
    os.system('adb shell input keyevent {}'.format(int(keyid)))


if __name__ == '__main__':
    adb_keyevent(27)
