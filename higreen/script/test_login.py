import unittest

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

from higreen.base.base_driver.base_driver import Driver
from higreen.page.Call_Page import Call_page
from ddt import ddt, file_data


@ddt
class Test_login(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver.driver_get()
        cls.logindriver = Call_page(cls.driver).login()


    @classmethod
    def tearDownClass(cls):
        Driver.driver_quit()

    @file_data(r'E:\git\pythonProject\higreen\test_data\data_login.json')
    def test_login(self, username, pwd, isyonghxy, verdict, expected, tuichu):
        self.logindriver.page_login(username, pwd, isyonghxy)
        """
        登录业务
        """
        if verdict:
            """
            verdict为True执行
            """
            try:
                expecteds = self.logindriver.page_gongz(expected)
                print('++++++', expecteds)
                self.assertEqual(expecteds, expected)
                """
                判断登录是否成功正确
                """
            except AssertionError as err:
                """
                否则保存异常原因并截图保存
                """
                self.logindriver.base_screenshot()
                raise err
            finally:
                self.logindriver.page_wod()
                self.logindriver.page_qiehzh()
                self.logindriver.page_querqh()
                try:
                    self.assertEqual(self.logindriver.get_toast(tuichu), tuichu)
                except AttributeError as e:
                    self.logindriver.base_screenshot()
                    raise e
        else:
            try:
                expecteds = self.logindriver.get_toast(expected)
                self.assertEqual(expecteds, expected)
            except Exception as rr:
                self.logindriver.base_screenshot()
                raise rr
