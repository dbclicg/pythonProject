# -*- coding: utf-8 -*-
# coding=utf-8
# @Time    : 2021/12/4 10:11
# @Author  : 牛逼哥
# @FileName: te.py
# @Software: PyCharm
import unittest
from appium.webdriver.common.appiumby import AppiumBy
from higreen.base.base_driver.base_driver import Driver
from higreen.page.Call_Page import Call_page
from higreen.page.element import jiaojb_element as element
from ddt import ddt, file_data


@ddt
class Jiaojb(unittest.TestCase):
    driver = None
    sure_text = ["同意", "允许", "始终允许", "取消", "确定"]

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = Driver.driver_get()
        cls.dver = Call_page(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        Driver.driver_quit()

    @file_data(r"E:\git\pythonProject\higreen\test_data\data_jiaojb.json")
    def test_jiaojb(self, wup, wupsl, wup01, wupsl01, beizxx, message, cycle=3):
        if self.dver.login().base_find_element(element.gongz) == None:
            self.dver.login().page_zclogin()
            for a in range(cycle):
                """
                处理系统弹窗
                """
                for i in self.sure_text:
                    try:
                        popup = self.dver.login().base_find_element(AppiumBy.XPATH, "//*[@text='%s']" % i)
                        if popup:
                            popup.click()
                        else:
                            print(">>>>>>>>>>>>app以获取系统权限")
                    except:
                        pass
        else:
            print(">>>>>>>>>>>>程序已登录")
        try:
            self.dver.jiaojb().page_jiaojb(wup, wupsl, wup01, wupsl01, beizxx)
            text = self.dver.jiaojb().get_toast(message)
            print(">>>>>>>>>>",text)
            self.assertTrue(text, ">>>>>>>>>>>>>>测试失败")
        except AssertionError as r:
            self.dver.jiaojb().base_screenshot()
            raise r
