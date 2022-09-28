# -*- coding: utf-8 -*-
# coding=utf-8
# @Time    : 2021/12/4 10:11
# @Author  :
# @FileName: te.py
# @Software: PyCharm
import os
import shutil
import time
import unittest
import warnings

import pytest

from higreen.base.comm.config import file
from appium.webdriver.common.appiumby import AppiumBy
from ddt import ddt, data, unpack, file_data
from higreen.base.comm import excel_read
from higreen.base.base_driver.base_driver import Driver
from higreen.page.Call_Page import Call_page
from higreen.page.element import jiaojb_element as element
from higreen.page.element import login_element as elements
from higreen.base.comm import adb_os
from higreen.base.comm.config import appActivity


@ddt
class Jiaojb(unittest.TestCase):
    driver = None
    data_list = excel_read.excel_to_list("TestUserLogin")

    @classmethod
    def setUpClass(cls) -> None:
        time.sleep(1)
        warnings.simplefilter('ignore', ResourceWarning)
        cls.driver = Driver.driver_get()
        cls.login_dver = Call_page(cls.driver).login()
        cls.dver = Call_page(cls.driver).jiaojb()

    @classmethod
    def tearDownClass(cls) -> None:
        Driver.driver_quit()

    @file_data(file.jiaojb_test_data)
    def test_jiaojb(self, successor, shift, name, num, value, expected, title, verdict):
        """
        交班测试用例
        :param successor: 交班人
        :param shift: 班次
        :param name: 物品名称
        :param num: 物品数量
        :param value: 交接班现场管理情况
        :param expected: 预期结果
        :param title: 用于测试报告的用例描述----->且用于判断执行指定方法
        :param verdict: 是否为异常用例
        :return:
        """
        if self.dver.base_find_element(elements.lijdl, 1, 0.05):
            """
            判断是否已登录
            """
            self.login_dver.page_zclogin()
            self.dver.page_click_gongz()
            self.dver.page_click_jiaojbcd()
            try:
                if verdict:
                    """
                    判断是否为正常用例
                    """
                    self.dver.page_normal_jiaob(successor, shift, name, num, value)
                    self.driver.wait_activity(appActivity.jiaojblist_appActivity, 5, 0.05)
                    """等待交接班列表activity"""
                else:
                    if title == "接班人为空":
                        self.dver.page_jiebrk_jiaob(shift, name, num, value)
                    elif title == "接班班次为空":
                        self.dver.page_jiebbck_jiaob(successor, name, num, value)
                    elif title == "负责区域为空":
                        self.dver.page_fuzqyk_jiaob(successor, shift, name, num, value)
                    elif title == "图片为空":
                        self.dver.page_tupwk_jiaob(successor, shift, name, num, value)
                    elif title == "为空提交":
                        self.dver.page_kon_jiaob()

                # time.sleep(1)
                self.dver.screenshot()
                text = self.dver.is_text(expected, title)
                self.assertTrue(text, "{}用例断言失败".format(title))
                if verdict:
                    try:
                        try:
                            self.dver.page_xiangq()
                            text1 = self.dver.base_toast_content("删除")
                            self.assertTrue(text1, "{}查看详情失败".format(title))
                        except Exception as ree:
                            raise ree
                        self.dver.page_shanc()
                        self.assertTrue(self.driver.wait_activity(appActivity.jiaojblist_appActivity, 5, 0.05), "{}删除失败".format(title))
                    except Exception as ree:
                        raise ree
            except Exception as ree:
                raise ree
            finally:
                if not verdict:
                    self.dver.page_fanghui()
                    self.dver.page_click_jiaoban()
        else:
            if adb_os.adb_execute(appActivity.jiaojblist_appActivity):
                """判断当前应用活动页是否为>>>>交接班列表"""
                try:
                    if verdict:
                        self.dver.page_normal_jiaob(successor, shift, name, num, value)
                        self.driver.wait_activity(appActivity.jiaojblist_appActivity, 5, 0.05)
                    else:
                        self.dver.page_click_jiaoban()
                        if title == "接班人为空":
                            self.dver.page_jiebrk_jiaob(shift, name, num, value)
                        elif title == "接班班次为空":
                            self.dver.page_jiebbck_jiaob(successor, name, num, value)
                        elif title == "负责区域为空":
                            self.dver.page_fuzqyk_jiaob(successor, shift, name, num, value)
                        elif title == "图片为空":
                            self.dver.page_tupwk_jiaob(successor, shift, name, num, value)
                        elif title == "为空提交":
                            self.dver.page_kon_jiaob()
                    # time.sleep(1)
                    self.dver.screenshot()
                    text = self.dver.is_text(expected, title)
                    self.assertTrue(text, "{}用例断言失败".format(title))
                    if verdict:
                        try:
                            try:
                                self.dver.page_xiangq()
                                text1 = self.dver.base_toast_content("删除")
                                self.assertTrue(text1, "{}查看详情失败".format(title))
                            except Exception as ree:
                                raise ree
                            self.dver.page_shanc()
                            self.assertTrue(self.driver.wait_activity(appActivity.jiaojblist_appActivity, 5, 0.05),
                                            "{}删除失败".format(title))
                        except Exception as ree:
                            raise ree
                except Exception as ree:
                    raise ree

                finally:
                    if not verdict:
                        self.dver.page_fanghui()
                        self.dver.page_click_jiaoban()
                    # elif verdict:
                    #     try:
                    #         self.dver.page_xiangq()
                    #         text = self.dver.base_toast_content("删除")
                    #         self.assertTrue(text, "{}删除失败".format(title))
                    #         self.dver.page_shanc()
                    #         self.driver.wait_activity(appActivity.jiaojblist_appActivity, 5, 0.05)
                    #     except Exception as ree:
                    #         raise ree
                    # else:
                    #     print("verdict参数，请输入True或False")

            elif adb_os.adb_execute(appActivity.jiaob_appActivity):
                """判断当前应用活动页是否为>>>>交班页面"""
                self.dver.page_fanghui()
                self.dver.page_click_jiaoban()
                try:
                    if verdict:
                        self.dver.page_jiaob(successor, shift, name, num, value)
                        self.driver.wait_activity(appActivity.jiaojblist_appActivity, 5, 0.05)
                    else:
                        if title == "接班人为空":
                            self.dver.page_jiebrk_jiaob(shift, name, num, value)
                        elif title == "接班班次为空":
                            self.dver.page_jiebbck_jiaob(successor, name, num, value)
                        elif title == "负责区域为空":
                            self.dver.page_fuzqyk_jiaob(successor, shift, name, num, value)
                        elif title == "图片为空":
                            self.dver.page_tupwk_jiaob(successor, shift, name, num, value)
                        elif title == "为空提交":
                            self.dver.page_kon_jiaob()
                    # time.sleep(1)
                    self.dver.screenshot()
                    text = self.dver.is_text(expected, title)
                    self.assertTrue(text, "{}用例断言失败".format(title))
                except Exception as ree:
                    raise ree
                finally:
                    if not verdict:
                        self.dver.page_fanghui()
                        self.dver.page_click_jiaoban()
            else:
                self.dver.page_click_gongz()
                if not self.dver.base_toast_content(successor):
                    """
                    当登录账号不等于接班人时，执行交接班
                    """
                    self.dver.page_click_jiaojbcd()
                    try:
                        if verdict:
                            self.dver.page_normal_jiaob(successor, shift, name, num, value)
                            self.driver.wait_activity(appActivity.jiaojblist_appActivity, 5, 0.05)
                        else:
                            self.dver.page_click_jiaoban()
                            if title == "接班人为空":
                                self.dver.page_jiebrk_jiaob(shift, name, num, value)
                            elif title == "接班班次为空":
                                self.dver.page_jiebbck_jiaob(successor, name, num, value)
                            elif title == "负责区域为空":
                                self.dver.page_fuzqyk_jiaob(successor, shift, name, num, value)
                            elif title == "图片为空":
                                self.dver.page_tupwk_jiaob(successor, shift, name, num, value)
                            elif title == "为空提交":
                                self.dver.page_kon_jiaob()
                        # time.sleep(1)
                        self.dver.screenshot()
                        text = self.dver.is_text(expected, title)
                        self.assertTrue(text, "{}用例断言失败".format(title))
                        if verdict:
                            try:
                                try:
                                    self.dver.page_xiangq()
                                    text1 = self.dver.base_toast_content("删除")
                                    self.assertTrue(text1, "{}查看详情失败".format(title))
                                except Exception as ree:
                                    raise ree
                                self.dver.page_shanc()
                                self.assertTrue(self.driver.wait_activity(appActivity.jiaojblist_appActivity, 5, 0.05),
                                                "{}删除失败".format(title))
                            except Exception as ree:
                                raise ree
                    except Exception as ree:
                        raise ree

                    finally:
                        if not verdict:
                            self.dver.page_fanghui()
                            self.dver.page_click_jiaoban()
                elif self.dver.base_toast_content(successor):
                    """
                    当登录账号等于接班人时，退出账号并重新登录账号
                    """
                    self.login_dver.page_tuiczh()
                    self.login_dver.page_zclogin()
                    self.dver.page_click_gongz()
                    self.dver.page_click_jiaojbcd()
                    try:
                        if verdict:
                            """
                            判断是否为正常用例
                            """
                            self.dver.page_normal_jiaob(successor, shift, name, num, value)
                            self.driver.wait_activity(appActivity.jiaojblist_appActivity, 5, 0.05)
                            """等待交接班列表activity"""
                        else:
                            if title == "接班人为空":
                                self.dver.page_jiebrk_jiaob(shift, name, num, value)
                            elif title == "接班班次为空":
                                self.dver.page_jiebbck_jiaob(successor, name, num, value)
                            elif title == "负责区域为空":
                                self.dver.page_fuzqyk_jiaob(successor, shift, name, num, value)
                            elif title == "图片为空":
                                self.dver.page_tupwk_jiaob(successor, shift, name, num, value)
                            elif title == "为空提交":
                                self.dver.page_kon_jiaob()

                        # time.sleep(1)
                        self.dver.screenshot()
                        text = self.dver.is_text(expected, title)
                        self.assertTrue(text, "{}用例断言失败".format(title))
                        if verdict:
                            try:
                                try:
                                    self.dver.page_xiangq()
                                    text1 = self.dver.base_toast_content("删除")
                                    self.assertTrue(text1, "{}查看详情失败".format(title))
                                except Exception as ree:
                                    raise ree
                                self.dver.page_shanc()
                                self.assertTrue(self.driver.wait_activity(appActivity.jiaojblist_appActivity, 5, 0.05),
                                                "{}删除失败".format(title))
                            except Exception as ree:
                                raise ree
                    except Exception as ree:
                        raise ree
                    finally:
                        if not verdict:
                            self.dver.page_fanghui()
                            self.dver.page_click_jiaoban()



