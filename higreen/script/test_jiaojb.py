import unittest
from higreen.base.base_driver.base_driver import Driver
from higreen.page.Call_Page import Call_page
from higreen.page.element import jiaojb_element as element
from ddt import ddt, file_data


@ddt
class Jiaojb(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = Driver.driver_get()
        cls.dver = Call_page(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        Driver.driver_quit()

    @file_data(r"C:\Users\23226\PycharmProjects\pythonProject\higreen\test_data\data_jiaojb.json")
    def test_jiaojb(self, wup, wupsl, wup01, wupsl01, beizxx, message):
        if self.dver.login().base_find_element(element.gongz) == False:
            self.dver.login().page_zclogin()
        else:
            print(">>>>>>>>>>>>程序已登录")
        try:
            self.dver.jiaojb().page_jiaojb(wup, wupsl, wup01, wupsl01, beizxx)
            self.assertEqual(self.dver.jiaojb().get_toast(message), message)
        except AssertionError as r:
            self.dver.jiaojb().base_screenshot()
            raise r
