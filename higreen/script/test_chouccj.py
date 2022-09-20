import unittest
import time
from higreen.base.comm.config import file
from higreen.base.base_driver.base_driver import Driver
from higreen.page.Call_Page import Call_page
from higreen.page.element import login_element as element
from higreen.base.comm.config import appActivity
from ddt import ddt, file_data, unpack


@ddt()
class Test_Chouccj(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = Driver.driver_get()
        cls.login_driver = Call_page(cls.driver).login()
        cls.chouccj_driver = Call_page(cls.driver).chouccj()

    @classmethod
    def tearDownClass(cls) -> None:
        Driver.driver_quit()

    @file_data(file.chouccj_test_data)
    def test_chouccj(self, remark, expect, title, is_pass_not):
        """
        抽查抽检
        :param remark: 备注
        :param expect: 预期结果
        :param title: 测试用例标题
        :param is_pass_not: 是否通过
        :return:
        """
        if self.chouccj_driver.base_find_element(element.lijdl, 2):
            """是否已登录---未登录执行"""
            self.login_driver.page_zclogin()
            self.chouccj_driver.page_click_gongz()
            self.chouccj_driver.page_click_chouccjcd()
            if is_pass_not:
                try:
                    self.chouccj_driver.page_chouccj_pass()
                    self.driver.wait_activity(appActivity.chouccj_appActivity, 5, 0.5)
                    self.chouccj_driver.screenshot()
                    self.assertTrue(self.chouccj_driver.is_text(expect, title))
                except Exception as err:
                    self.chouccj_driver.base_screenshot()
                    raise err
            elif not is_pass_not:
                try:
                    self.chouccj_driver.page_click_chouccjcd()
                    self.chouccj_driver.page_chouccj_not_pass(remark)
                    self.driver.wait_activity(appActivity.chouccj_appActivity, 5, 0.5)
                    self.chouccj_driver.screenshot()
                    self.assertTrue(self.chouccj_driver.is_text(expect, title))
                except Exception as err:
                    self.chouccj_driver.base_screenshot()
                    raise err
            else:
                print('is_pass_not请输入布尔值')
        else:
            if self.chouccj_driver.base_find_element(element.gongz, 2):
                self.chouccj_driver.page_click_gongz()
                self.chouccj_driver.page_click_chouccjcd()
            if is_pass_not:
                try:
                    self.chouccj_driver.page_chouccj_pass()
                    self.driver.wait_activity(appActivity.chouccj_appActivity, 5, 0.5)
                    self.chouccj_driver.screenshot()
                    self.assertTrue(self.chouccj_driver.is_text(expect, title))
                except Exception as err:
                    self.chouccj_driver.base_screenshot()
                    raise err
            elif not is_pass_not:
                try:
                    self.chouccj_driver.page_chouccj_not_pass(remark)
                    self.driver.wait_activity(appActivity.chouccj_appActivity, 5, 0.5)
                    self.chouccj_driver.screenshot()
                    self.assertTrue(self.chouccj_driver.is_text(expect, title))
                except Exception as err:
                    self.chouccj_driver.base_screenshot()
                    raise err
            else:
                print('is_pass_not请输入布尔值')
