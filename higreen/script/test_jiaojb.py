# -*- coding: utf-8 -*-
# coding=utf-8
# @Time    : 2021/12/4 10:11
# @Author  : 牛逼哥
# @FileName: te.py
# @Software: PyCharm
import time
import unittest

from appium.webdriver.common.appiumby import AppiumBy
from ddt import ddt, file_data

from higreen.base.base_driver.base_driver import Driver
from higreen.base.comm import file
from higreen.page.Call_Page import Call_page
from higreen.page.element import jiaojb_element as element


@ddt
class Jiaojb(unittest.TestCase):
    driver = None
    sure_text = ["同意", "允许", "始终允许", "取消", "确定"]

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = Driver.driver_get()
        cls.dver = Call_page(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        Driver.driver_quit()

    @file_data(file.jiaojb)
    def test_jiaojb(self, wup, wupsl, wup01, wupsl01, beizxx, message, cycle=3, isdelete=False):
        """
        交班流程测试
        :param wup: 物品
        :param wupsl: 物品数量
        :param wup01: 物品+1
        :param wupsl01: 物品数量+1
        :param beizxx: 交班情况描述
        :param message: 预期结果
        :param cycle: 处理系统弹窗循环次数
        :param isdelete: 是否删除交接班  删除则不执行接班流程 默认False   ----False不执行    ---True执行删除
        :return:
        """

        if self.dver.login().base_find_element(element.gongz, time=3, poll=0.05) == None:
            """
            判断app是否已登录，否则执行登录操作
            """
            self.dver.login().page_zclogin()
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

        else:
            print(">>>>>>>>>>>>程序已登录")
        try:

            self.dver.jiaojb().page_jiaojb(wup, wupsl, wup01, wupsl01, beizxx)
            """
            交班提交
            """
            text01 = self.dver.jiaojb().get_toast(message)
            self.assertTrue(text01, ">>>>>>>>>>>>>>提交交班测试失败")
            """判断交班提交是否成功"""
        except AssertionError as r:
            self.dver.jiaojb().base_screenshot()
            """
            异常时截图
            """
            raise r
        finally:
            try:
                judge = self.dver.jiaojb().page_clock_xiangq()
                if judge:
                    """判断交接班列表是否存在数据"""
                    if isdelete:
                        self.dver.jiaojb().page_clock_shanc()
                    else:
                        while not self.dver.login().page_wod():
                            """循环查找"我的"元素，没有找到则循环点击返回"""
                            self.dver.jiaojb().page_fanghui()
                            time.sleep(1)
                        self.dver.login().page_qiehzh()
                        self.dver.login().page_querqh()
                        self.dver.login().page_jiaobrlogin()
                        """切换到接班人账号"""
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
                        self.dver.jiaojb().page_jieb()
                        """接班提交"""
                else:
                    pass
                text02 = self.dver.jiaojb().get_toast(message)
                self.assertTrue(text02, ">>>>>>>>>>>>>>提交交班测试失败")
                time.sleep(2)
            except AssertionError as err:
                self.dver.jiaojb().base_screenshot()
                raise err
