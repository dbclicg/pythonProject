import unittest

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

from higreen.base.base_driver.base_driver import Driver
from higreen.page.element import jiaojb_element as element
from higreen.page.Call_Page import Call_page
from ddt import ddt, file_data
from higreen.base.comm import file

@ddt
class Test_login(unittest.TestCase):
    driver = None
    sure_text = ["同意", "允许", "始终允许", "取消", "确定"]
    @classmethod
    def setUpClass(cls):
        cls.driver = Driver.driver_get()
        cls.logindriver = Call_page(cls.driver).login()


    @classmethod
    def tearDownClass(cls):
        Driver.driver_quit()

    @file_data(file.login)
    def test_login(self, username, pwd, isyonghxy, verdict, expected, tuichu, cycle=3):
        if self.logindriver.base_find_element(element.gongz, time=3, poll=0.05) is not None:
            """
            判断app是否已登录,已登录则执行退出登录
            """
            for i in range(cycle):
                """
                处理系统弹窗
                """
                for i in self.sure_text:
                    try:
                        popup = self.driver.find_element(AppiumBy.XPATH, "//*[@text='%s']" % i)
                        if popup:
                            popup.click()
                        else:
                            print(">>>>>>>>>>>>没有系统权限提示")
                    except:
                        pass
            self.logindriver.page_wod()
            self.logindriver.page_qiehzh()
            self.logindriver.page_querqh()
        else:
            print(">>>>>>>>>>>>没有登录")

        self.logindriver.page_login(username, pwd, isyonghxy)
        for i in range(cycle):
            """
            处理系统弹窗
            """
            for i in self.sure_text:
                try:
                    popup = self.driver.find_element(AppiumBy.XPATH, "//*[@text='%s']"%i)
                    if popup:
                            popup.click()
                    else:
                        print(">>>>>>>>>>>>没有系统权限提示")
                except:
                    pass

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
                self.assertTrue(expecteds, ">>>>>>>>>>:登录验证失败")
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
                    self.assertTrue(self.logindriver.get_toast(tuichu))
                except AttributeError as e:
                    self.logindriver.base_screenshot()
                    raise e
        else:
            try:
                expecteds = self.logindriver.get_toast(expected)
                self.assertTrue(expecteds)
            except Exception as rr:
                self.logindriver.base_screenshot()
                raise rr
