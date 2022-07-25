# -*- coding: utf-8 -*-
# @Time    : 2021/12/4 10:11
# @Author  : 牛逼哥
# @FileName: te.py
# @Software: PyCharm
import warnings

from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium import webdriver
import os
from higreen.base.base_driver import appium_ini


class Driver:
    driver = None
    sure_text = ["同意", "允许", "始终允许", "取消", "确定"]
    @classmethod
    def driver_get(cls, cycle=3):
        if cls.driver is None:
            warnings.filterwarnings("ignore", category=DeprecationWarning)  # 忽略selenium4.0后desired_capabilities被启用警告
            cls.driver = Remote("http://localhost:4723/wd/hub", appium_ini.caps)
            for i in range(cycle):
                """
                处理系统弹窗
                """
                for i in cls.sure_text:
                    try:
                        popup = cls.driver.find_element(AppiumBy.XPATH, "//*[@text='%s']"%i)
                        if popup:
                            popup.click()
                        else:
                            print(">>>>>>>>>>>>没有系统权限提示")
                    except:
                        pass
        return cls.driver

    @classmethod
    def driver_quit(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None


if __name__ == '__main__':
    driver = Driver.driver_get()
    #driver.switch_to.alert.accept()
    x = driver.get_window_size()['width']  # 获取设备的屏幕宽度
    y = driver.get_window_size()['height']  # 获取设备屏幕的高度
    print(x, y)  # 打印出点击的坐标点
    # print(x_1 * x, y_1 * y)
