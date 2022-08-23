# -*- coding: utf-8 -*-
# coding=utf-8
# @Time    : 2021/12/4 10:11
# @Author  : 牛逼哥
# @FileName: te.py
# @Software: PyCharm
import time
import unittest
import warnings

from appium.webdriver.common.appiumby import AppiumBy
from ddt import ddt, data, unpack
from higreen.base.comm import excel_read
from higreen.base.base_driver.base_driver import Driver
from higreen.page.Call_Page import Call_page
from higreen.page.element import jiaojb_element as element
from higreen.page.element import login_element as elements
from higreen.base.comm import adb_os


@ddt
class Jiaojb(unittest.TestCase):
    driver = None
    data_list = excel_read.excel_to_list("TestUserLogin")

    @classmethod
    def setUpClass(cls) -> None:
        warnings.simplefilter('ignore', ResourceWarning)
        cls.driver = Driver.driver_get()
        cls.dver = Call_page(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        Driver.driver_quit()

    def test_jiaojb(self):

        pass
