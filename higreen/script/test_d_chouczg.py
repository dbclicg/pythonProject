# -*- coding: utf-8 -*-
# coding=utf-8
# @Time    : 
# @Author  : lcg
# @FileName: te.py
# @Software: PyCharm
import time
import unittest
from higreen.base.base_driver.base_driver import Driver
from higreen.base.comm.config.appActivity import chouczg
from higreen.page.Call_Page import Call_page
from higreen.page.element import login_element
from higreen.base.comm.log_loguru import Logings


class Test_Chouczg(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        time.sleep(1)
        cls.logs = Logings()
        cls.driver = Driver.driver_get()
        cls.chouczg_driver = Call_page(cls.driver).chouczg()
        cls.login_driver = Call_page(cls.driver).login()

    @classmethod
    def tearDownClass(cls) -> None:
        Driver.driver_quit()

    def test_chouczg(self, expect_text='修改成功', title='正常', zgsm="ccc"):
        if self.chouczg_driver.base_find_element(login_element.lijdl, 2):
            self.logs.debug('开始登录....')
            try:
                self.login_driver.page_zclogin()
                self.chouczg_driver.page_click_gongz()
                self.chouczg_driver.page_click_chouczgcd()
                self.chouczg_driver.page_chouczg(zgsm)
                self.driver.wait_activity(chouczg, 3, 0.3)
                self.chouczg_driver.screenshot()
                self.assertTrue(self.chouczg_driver.is_text(expect_text, title))
            except AssertionError as err:
                self.logs.exception(err)
                raise err
        else:
            try:
                if self.chouczg_driver.base_find_element(login_element.gongz, 2):
                    self.chouczg_driver.page_click_gongz()
                    self.chouczg_driver.page_click_chouczgcd()
                self.chouczg_driver.page_chouczg(zgsm)
                self.driver.wait_activity(chouczg, 3, 0.3)
                self.chouczg_driver.screenshot()
                self.assertTrue(self.chouczg_driver.is_text(expect_text, title))
            except AssertionError as err:
                self.logs.exception(err)
                raise err

