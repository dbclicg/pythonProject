import os
import shutil
import time
import unittest
# from higreen.base.comm.excel_read import excel_to_list
from higreen.base.base_driver.base_driver import Driver
from higreen.page.element import login_element as element
from higreen.page.Call_Page import Call_page
from ddt import file_data, data, ddt
from higreen.base.comm.config import file
from higreen.base.comm.log_loguru import Logings


@ddt
class Test_login(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        time.sleep(1)
        cls.log = Logings()
        cls.driver = Driver.driver_get()
        cls.logindriver = Call_page(cls.driver).login()

    @classmethod
    def tearDownClass(cls):

        Driver.driver_quit()

    @file_data(file.login_test_data)
    def test_login(self, title, user, password, isyonghxy, message, verdict):
        """
        登录用例
        :param title: 用例标题
        :param user: 登录用户
        :param password: 用户密码
        :param isyonghxy: 是否勾选隐私协议
        :param message: 预期结果
        :param verdict: 是否为错误用例
        :return:
        """
        if not self.logindriver.base_find_element(element.lijdl, 2):
            self.log.debug("app已登录正在执行退出.....")
            """
            平湖海吉星——————已登录执行
            判断app是否已登录,已登录则执行退出登录
            """
            self.logindriver.base_click_system()
            self.logindriver.page_wod()
            self.logindriver.page_qiehzh()
            self.logindriver.page_querqh()
            self.log.debug("app已退出登录，开始执行登录用例....")
            if verdict:
                try:
                    self.log.debug("开始执行用例：{}....".format(title))
                    self.logindriver.page_login(user, password, isyonghxy)
                    """
                    正常登录
                    """
                    self.logindriver.page_gongz()
                    toast = self.logindriver.base_toast_content(message)
                    self.assertTrue(toast, "正确用户密码登录断言失败toast = {}".format(toast))
                except AssertionError as ree:
                    self.log.debug(ree)
                    raise ree

                finally:
                    if not self.logindriver.base_find_element(element.lijdl, 2):
                        """
                        判断app是否已登录,已登录则执行退出登录
                        """
                        self.logindriver.base_click_system()
                        self.logindriver.page_wod()
                        self.logindriver.page_qiehzh()
                        self.logindriver.page_querqh()

                    else:
                        pass
            else:
                try:
                    self.logindriver.page_login(user, password, isyonghxy)
                    self.logindriver.screenshot()
                    """
                    断言截图
                    """
                    istext = self.logindriver.is_text(message, title)
                    """
                    调用图片文字识别断言toast
                    """
                    self.assertTrue(istext, "预期结果>>>>>:{}".format(message))
                except AssertionError as ree:
                    raise ree

        else:
            """
            平湖海吉星--------未登录执行
            """
            # try:
            if verdict:
                """
                    """
                try:
                    self.logindriver.page_login(user, password, isyonghxy)
                    self.log.debug("开始执行用例：{}....".format(title))
                    """
                    正常登录
                    """
                    self.logindriver.base_click_system()
                    self.logindriver.page_gongz()
                    toast = self.logindriver.base_toast_content(message)
                    self.assertTrue(toast, "正确用户密码登录断言失败toast =  {}".format(toast))
                except AssertionError as ree:
                    raise ree

                finally:
                    if not self.logindriver.base_find_element(element.lijdl, 2):
                        """
                        判断app是否已登录,已登录则执行退出登录
                        """
                        self.logindriver.page_wod()
                        self.logindriver.page_qiehzh()
                        self.logindriver.page_querqh()

                    else:
                        pass
            else:
                try:
                    self.logindriver.page_login(user, password, isyonghxy)
                    self.log.debug("开始执行用例：{}....".format(title))
                    self.logindriver.screenshot()
                    """
                    断言截图
                    """
                    istext = self.logindriver.is_text(message, title)
                    """
                    调用图片文字识别断言toast
                    """
                    self.assertTrue(istext, "预期结果>>>>>:{}".format(message))
                except AssertionError as ree:
                    self.log.debug(ree)
                    raise ree
