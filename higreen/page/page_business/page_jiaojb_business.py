# -*- coding: utf-8 -*-
# @Time    : 2021/12/4 10:11
# @Author  :
# @FileName: te.py
# @Software: PyCharm
import os
import time
from uiautomator2 import connect
from appium.webdriver.common.appiumby import AppiumBy
from higreen.page.element import jiaojb_element as element
from higreen.base.comm.base_operate_element import Base_operate_element
from higreen.base.comm.base_touchAction import Base_TouchAction as touch
from higreen.base.comm.base_ActionChains import Base_ActionChains


class Page_jiaojb_business(Base_operate_element):
    """>>>>>>>>>>>>>>>>>交班<<<<<<<<<<<<<<"""

    def page_click_gongz(self):
        """
        点击工作
        :return:
        """
        self.base_click(element.gongz)

    def page_click_jiaojbcd(self):
        """
        点击交接班菜单
        :return:
        """
        self.swipe_element(element.jiaojbcd)
        self.base_click(element.jiaojbcd)

    def page_click_jiaoban(self):
        """
        点击交班按钮
        :return:
        """
        self.base_click(element.jiaoban)

    def page_click_jiebrxzk(self, successor):
        """
        选择接班人
        :return:
        """
        self.base_click(element.jiebrxzk)
        """点击选择接班人"""
        el = (AppiumBy.XPATH, '//*[@text="{}"]'.format(successor))
        self.swipe_element(el)
        self.base_click(el)

    def page_click_jiebbcxzk(self, shift):
        """
        选择接班班次
        :return:
        """
        self.base_click(element.jiebbcxzk)
        """点击选择接班班次"""
        el = (AppiumBy.XPATH, '//*[@text="{}"]'.format(shift))
        self.base_click(el)

    def page_click_fuzqyxzk(self):
        """
        选择负责区域
        :return:
        """
        self.base_click(element.fuzqyxzk)
        """点击负责区域"""
        self.base_click(element.quyu_list)
        """选择点击负责区域"""
        self.base_click(element.quyutj)
        """提交"""

    def page_sebnd_wup(self, name, num):
        """
        输入物品
        :param num: 输入物品数量
        :param name: 输入物品名称
        :return:
        """
        self.base_sebnd_keys(element.wup_name, name)
        """输入物品名称"""
        self.base_sebnd_keys(element.wup_num, num)
        """输入物品数量"""

    def page_tianjwp(self, name, num, n=1):
        """添加物品"""
        for i in range(n):
            self.base_click(element.tianjwp)
            self.page_sebnd_wup(name, num)

    def page_sebnd_beiz(self, value):
        """
        交接班现场管理情况
        :param value: 情况描述
        :return:
        """
        self.base_sebnd_keys(element.beiz, value)

    def page_xiangq(self):
        """
        查看详情
        :return:
        """
        self.base_click(element.jiaobsj)

    def page_shanc(self):
        """
        删除交班数据
        :return:
        """
        self.base_click(element.shanc)
        self.base_click(element.quedsc)

    def page_tup(self):
        """
        拍照上传图片
        :return:
        """
        self.swipe_element(element.tupscan)
        self.base_click(element.tupscan)
        self.base_click(element.xuanztp1)
        self.base_click(element.xuanztp2)
        self.base_click(element.xuanztp3)
        self.base_click(element.tijtp)

    def page_tijiao(self):
        """
        交班提交
        :return:
        """
        self.base_click(element.tijiao)

    def page_fanghui(self):
        """返回"""
        self.base_click(element.fanghui)

    def page_normal_jiaob(self, successor, shift, name, num, value):
        """正常交班"""
        self.page_click_jiaoban()
        self.page_click_jiebrxzk(successor)
        self.page_click_jiebbcxzk(shift)
        self.page_click_fuzqyxzk()
        self.page_sebnd_wup(name, num)
        self.page_tianjwp(name, num)
        self.page_sebnd_beiz(value)
        self.page_tup()
        self.page_tijiao()

    def page_jiaob(self, successor, shift, name, num, value):
        """不点击交班按钮"""
        self.page_click_jiebrxzk(successor)
        self.page_click_jiebbcxzk(shift)
        self.page_click_fuzqyxzk()
        self.page_sebnd_wup(name, num)
        self.page_sebnd_beiz(value)
        self.page_tup()
        self.page_tijiao()

    def page_jiebrk_jiaob(self, shift, name, num, value):
        """接班人为空"""
        self.page_click_jiebbcxzk(shift)
        self.page_click_fuzqyxzk()
        self.page_sebnd_wup(name, num)
        self.page_sebnd_beiz(value)
        self.page_tup()
        self.page_tijiao()

    def page_jiebbck_jiaob(self, successor, name, num, value):
        """接班班次为空"""
        self.page_click_jiebrxzk(successor)
        self.page_click_fuzqyxzk()
        self.page_sebnd_wup(name, num)
        self.page_sebnd_beiz(value)
        self.page_tup()
        self.page_tijiao()

    def page_fuzqyk_jiaob(self, successor, shift, name, num, value):
        """负责区域为空"""
        self.page_click_jiebrxzk(successor)
        self.page_click_jiebbcxzk(shift)
        self.page_sebnd_wup(name, num)
        self.page_sebnd_beiz(value)
        self.page_tup()
        self.page_tijiao()

    def page_tupwk_jiaob(self, successor, shift, name, num, value):
        """图片为空"""
        self.page_click_jiebrxzk(successor)
        self.page_click_jiebbcxzk(shift)
        self.page_click_fuzqyxzk()
        self.page_sebnd_wup(name, num)
        self.page_sebnd_beiz(value)
        self.page_tijiao()

    def page_kon_jiaob(self):
        """为空提交"""
        self.page_tijiao()

    def page_wup_jiaob(self, successor, shift, name, num, value):
        """添加物品"""
        self.page_click_jiaoban()
        self.page_click_jiebrxzk(successor)
        self.page_click_jiebbcxzk(shift)
        self.page_click_fuzqyxzk()
        self.page_sebnd_wup(name, num)
        self.page_tianjwp(name, num)
        self.page_sebnd_beiz(value)
        self.page_tup()
        self.page_tijiao()

    """>>>>>>>>>>>>>>>>>接班<<<<<<<<<<<<<<"""

    def page_click_xuanzdbgly(self):
        """
        选择当班管理员
        :return:
        """
        self.base_click(element.dangbgly)
        self.base_click(element.xuanzdbgly)
        self.base_click(element.qued)

    def page_click_xuanzgw(self):
        """
        选择管理员岗位
        :return:
        """
        elements = self.base_find_elements(element.guanlygw)
        for i in range(len(elements)):
            self.base_click(element.guanlygw)
            self.base_click(element.xuanzglygw)

    def page_dianzqm(self):
        """
        电子签名
        :return:
        """
        self.swipe_element(element.dianzqm)
        self.base_click(element.dianzqm)

        self.swipe_find(element.X1, element.Y1, element.X2, element.Y2, element.X3, element.Y3, element.X4, element.Y4,
                        element.X5, element.Y5, element.X6, element.Y6, element.X7, element.Y7, element.X8, element.Y8)
        self.base_click(element.dianzqmqd)

    def page_jiebtj(self):
        """
        点击接班提交
        :return:
        """
        self.base_click(element.jiebtj)

    def page_normal_jieb(self, successor, shift, name, num, value):
        """
        正常接班
        :param successor: 接班人
        :param shift: 班次
        :param name: 物品名称
        :param num: 物品数量
        :param value: 交接班现场管理情况
        :return:
        """
        self.page_normal_jiaob(successor, shift, name, num, value)
        self.page_xiangq()
        self.page_click_xuanzdbgly()
        self.page_click_xuanzgw()
        self.page_dianzqm()
        time.sleep(2)
        self.page_jiebtj()
        time.sleep(5)
