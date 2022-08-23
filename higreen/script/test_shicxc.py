import unittest
import time
from appium.webdriver.common.appiumby import AppiumBy

from higreen.page import Call_Page
from higreen.base.base_driver.base_driver import Driver




class Test_Shicxc(unittest.TestCase):
    driver = None
    #data_list = excel_read.excel_to_list("TestShicxc")

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = Driver.driver_get()
        cls.shic_driver = Call_Page.Page_shicxc(cls.driver)
        cls.login_driver = Call_Page.Page_login_business(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        Driver.driver_quit()

    def test_shicxc(self):
        """
        :param patrol_passed: 判断巡查是否通过合格 --True合格  --False不合格
        :param message: 预期结果
        :param abnormalcondition:  判断是否为异常用例 --True不正常用例  --False正常用例
        :param is_null: 判断执行用例那个字段要为空 接受 1=档位为空 ，2=档口图片为空 ， 3=评分为空 ， 4=电子签名为空
        :return:
        """
        if self.shic_driver.base_find_element((AppiumBy.XPATH, '//*[@text="立即登录"]'), 2):
            """
            判断是否已登录----True执行登录
            """
            self.login_driver.page_zclogin()
            time.sleep(4)
            try:
                self.shic_driver.page_fail_shicxc()
                time.sleep(0.5)
                self.assertTrue(self.shic_driver.get_toast("提交成功"),
                                ">>>>>>>>>查看预期结果是否正确：{}".format("提交成功"))

                print(">>>>>>>>>>>>>>>>>>>判断是否为True：", self.shic_driver.get_toast("提交成功"))
            except AssertionError as error:
                self.shic_driver.base_screenshot()
                print("page_pass_shicxc,提交断言失败>>>>>>>报错：", error)
                raise error
