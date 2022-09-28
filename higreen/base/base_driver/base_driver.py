# -*- coding: utf-8 -*-
# @Time    : 2021/12/4 10:11
# @Author  : 牛逼哥
# @FileName: te.py
# @Software: PyCharm
import time
import warnings
from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy

from higreen.base.comm.base_operate_element import Base_operate_element
import os
from higreen.base.base_driver import appium_ini
from higreen.base.comm.config import file
from higreen.base.comm.log_loguru import Logings


class Driver:
    driver = None
    base = Base_operate_element

    @classmethod
    def driver_get(cls):
        if cls.driver is None:
            Logings().debug("正在启动appium服务中....")
            os.system(file.startAppiumServer)
            """
            自启动appium服务
            """
            Logings().debug("=========appium服务启动成功=========")
            warnings.filterwarnings("ignore", category=DeprecationWarning)  # 忽略selenium4.0后desired_capabilities被启用警告
            Logings().debug("=========appium启动成功=========")
            cls.driver = Remote("http://127.0.0.1:4723/wd/hub", appium_ini.caps)
            cls.base(cls.driver).base_click_system()
        return cls.driver

    @classmethod
    def driver_quit(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None
            os.system(file.stopAppiumServer)


if __name__ == '__main__':

    driver = Driver.driver_get()
    """实例driver对象"""
    a = driver.current_package
    print(a)
    driver.start_activity(a, "com.ap.dbc.hjx.marker.app.Activity.RandomInspection.RandomCheckActivity")
    b = driver.current_activity
    print("当前activity", b)
    c = driver.network_connection
    print(c)
    driver.set_network_connection(1)
    driver.quit()



