import unittest
import time
from appium.webdriver.common.appiumby import AppiumBy
from higreen.page import Call_Page
from higreen.base.base_driver.base_driver import Driver
from higreen.base.comm.config import appActivity, file
from higreen.base.comm.adb_os import adb_execute
from higreen.page.element import shicxc_element as element
from ddt import ddt, file_data


@ddt()
class Test_Shicxc(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        time.sleep(1)
        cls.driver = Driver.driver_get()
        cls.shic_driver = Call_Page.Page_shicxc(cls.driver)
        cls.login_driver = Call_Page.Page_login_business(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        Driver.driver_quit()

    @file_data(file.shicxc_test_data)
    def test_shicxc(self, message, zgmessage, title, Rectification, Rectification_explain):
        """
        市场巡查-正常流程用例
        :param message:预期结果
        :param zgmessage:整改预期结果
        :param title: 用例标题
        :param value: 整改说明
        :return: 初稿---待优化
        """
        if self.shic_driver.base_find_element((AppiumBy.XPATH, '//*[@text="立即登录"]'), 2):
            """
            判断是否已登录----True执行登录
            """
            self.login_driver.page_zclogin()
            self.shic_driver.page_click_gongz()
            self.shic_driver.page_click_shicxccd()
            try:
                self.shic_driver.page_fail_shicxc()
                time.sleep(2)
                self.shic_driver.screenshot()
                self.assertTrue(self.shic_driver.is_text(message, title),
                                ">>>>>>>>>查看预期结果是否正确：{}".format(message))
            except Exception as error:
                print("page_pass_shicxc,提交断言失败>>>>>>>报错：", error)
                raise error
            finally:
                if Rectification:
                    """是否执行整改"""
                    if adb_execute(appActivity.shicxc_appActivity):
                        try:
                            self.shic_driver.page_zhengg(Rectification_explain)
                            self.driver.wait_activity(appActivity.shicxcbhglb_appActivity, 3, 0.5)
                            """等待指定 activity 页出现再执行后面代码"""
                            self.shic_driver.screenshot()
                            self.assertTrue(self.shic_driver.is_text(zgmessage, title))
                        except Exception as err:
                            raise err
                        finally:
                            self.shic_driver.page_click_fanhui()
        else:
            if self.shic_driver.base_find_element(element.gongz, 2):
                self.shic_driver.page_click_gongz()
                self.shic_driver.page_click_shicxccd()
            try:
                self.shic_driver.page_fail_shicxc()
                time.sleep(2)
                self.shic_driver.screenshot()
                self.assertTrue(self.shic_driver.is_text(message, title),
                                ">>>>>>>>>查看预期结果是否正确：{}".format("提交成功"))
            except Exception as err:
                print("page_pass_shicxc,提交断言失败>>>>>>>报错：结果不为真")
                raise err

            finally:
                if Rectification:
                    """是否执行整改"""
                    if adb_execute(appActivity.shicxc_appActivity):
                        try:
                            self.shic_driver.page_zhengg(Rectification_explain)
                            self.driver.wait_activity(appActivity.shicxcbhglb_appActivity, 3, 0.5)
                            """等待指定 activity 页出现再执行后面代码"""
                            self.shic_driver.screenshot()
                            self.assertTrue(self.shic_driver.is_text(zgmessage, title))
                        except Exception as err:
                            raise err
                        finally:
                            self.shic_driver.page_click_fanhui()
