# -*- coding: utf-8 -*-
# @Time    : 2021/12/4 10:11
# @Author  :
# @FileName: te.py
# @Software: PyCharm
import os


def adb_execute():
    isdevices = os.popen(r'adb shell dumpsys window | findstr mCurrentFocus', 'r')
    devices = isdevices.read()
    appActivity = devices[24:-2].replace('\n', '').replace('\r', '').replace(' ', '').split('/')[1]

    if appActivity in "com.ap.dbc.hjx.marker.app.ui.switchwork.SwitchWorkHomeActivity":
        return True
    else:
        return False


if __name__ == '__main__':
    print(adb_execute())
