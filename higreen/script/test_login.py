import os
import shutil
import time
import unittest
from higreen.base.comm.excel_read import excel_to_list
from higreen.base.base_driver.base_driver import Driver
from higreen.page.element import login_element as element
from higreen.page.Call_Page import Call_page
from ddt import file_data, data, ddt
from higreen.base.comm.config import file

@ddt
class Test_login(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        time.sleep(1)
        cls.driver = Driver.driver_get()
        cls.logindriver = Call_page(cls.driver).login()
        # shutil.rmtree(r'E:\git\pythonProject\higreen\Outputs\screenshot')
        # os.mkdir(r'E:\git\pythonProject\higreen\Outputs\screenshot')

    @classmethod
    def tearDownClass(cls):

        Driver.driver_quit()

    @file_data(file.login_test_data)
    def test_login(self, title, user, password, isyonghxy, message, verdict):
        if not self.logindriver.base_find_element(element.lijdl, 2):
            """
            平湖海吉星——————已登录执行
            判断app是否已登录,已登录则执行退出登录
            """
            self.logindriver.base_click_system()
            self.logindriver.page_wod()
            self.logindriver.page_qiehzh()
            self.logindriver.page_querqh()
            if verdict:
                try:
                    self.logindriver.page_login(user, password, isyonghxy)
                    """
                    正常登录
                    """
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
                except Exception as ree:
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
                    self.logindriver.screenshot()
                    """
                    断言截图
                    """
                    istext = self.logindriver.is_text(message, title)
                    """
                    调用图片文字识别断言toast
                    """
                    self.assertTrue(istext, "预期结果>>>>>:{}".format(message))
                except Exception as ree:
                    raise ree
