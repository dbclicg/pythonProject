# -*- coding: utf-8 -*-
# @Time    : 2021/12/4 10:11
# @Author  : 牛逼哥
# @FileName: te.py
# @Software: PyCharm
caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "127.0.0.1:62001"  # 手机名称
caps["appPackage"] = "com.padmatek.szhigreenmb"  # 包名
caps["appActivity"] = "com.ap.dbc.hjx.marker.app.Activity.Other.LauncherActivity"  # 程序启动名
caps["platformVersion"] = "7.1.2"  # 安卓版本
caps['automationName'] = 'Uiautomator2'  # 用于捕捉3秒提示文案
caps["unicodeKeyboard"] = True  # 使用自带输入法，输入中文时填True
caps["resetKeyboard"] = True  # 执行完程序恢复原来输入法
caps["noReset"] = True  # 不要重置App
caps["newCommandTimeout"] = "6000"
caps["autoGrantPermissions"] = True  # 获取所有权限
caps["XCUITest"] = True
