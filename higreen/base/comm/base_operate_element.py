# -*- coding: utf-8 -*-
# coding=utf-8
# @Time    : 2021/12/4 10:11
# @Author  : 牛逼哥
# @FileName: te.py
# @Software: PyCharm
import os
import time
import shutil

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from higreen.base.comm import file
from higreen.base.comm import base_find_element


class Base_operate_element(base_find_element.Base_element):
    __checked = False

    """
    常用元素操作类
    """

    def base_click(self, loc):
        """
        :点击操作封装
        :param loc:
        :return:
        """
        self.base_find_element(loc).click()

    def base_elements_click(self, loc):
        elementlist = self.base_find_elements(loc)
        print(">>>>>>>>列表：", len(elementlist))
        for list in elementlist:
            list.click()

    def base_sebnd_keys(self, loc, value):
        """
        ：输入操作封装
        :param loc:
        :value 输入的值
        :param value:
        :return:
        """
        self.base_find_element(loc).clear().send_keys(value)

    def base_text(self, loc):
        """
        获取text
        :param loc:
        :return:
        """
        ele_toast = self.base_find_element_located(loc)
        el_toast = ele_toast.text
        print(">>>>>>>>>提示：", ele_toast.text)
        return el_toast

    def get_toast(self, text):
        """
        is toast exist, return True or False

        :Agrs:

         - driver - 传driver

         - text   - 页面上看到的文本内容

         - timeout - 最大超时时间，默认30s

         - poll_frequency  - 间隔查询时间，默认0.5s查询一次

        :Usage:

         is_toast_exist(driver, "看到的内容")

        """

        try:
            toast_loc = (AppiumBy.XPATH, ".//*[contains(@text,'%s')]" % text)
            element = self.base_find_element(toast_loc, time=5, poll=0.01)
            print(">>>>>>>>>提示：", element.text)
            return True

        except:

            return False

    def base_screenshot(self):
        """
        截图保存
        :return:
        """
        shutil.rmtree(r'E:\git\pythonProject\higreen\Outputs\screenshot')
        os.mkdir(r'E:\git\pythonProject\higreen\Outputs\screenshot')
        self.driver.get_screenshot_as_file(file.jietbc + r'\{}.png'.format(
            time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))))

    def base_target_click(self, X1, Y1):  # x1,y1为你编写脚本时适用设备的实际坐标
        """
        使用坐标定位元素
        """
        x_1 = X1 / 900  # 计算坐标在横坐标上的比例，其中900为宽810
        y_1 = Y1 / 1600  # 计算坐标在纵坐标1600为高1200
        x = self.driver.get_window_size()['width']  # 获取设备的屏幕宽度
        y = self.driver.get_window_size()['height']  # 获取设备屏幕的高度
        print(x, y)  # 打印出点击的坐标点
        print(x_1 * x, y_1 * y)
        self.driver.tap([(x_1 * x, y_1 * y)], 500)  # 模拟单手点击操作

    def get_window_size(self):
        """
        获取当前手机屏幕大小
        :return:手机width，height
        """
        try:
            size = self.driver.get_window_size()
            width = size["width"]
            height = size["height"]
            return width, height
        except:
            raise

    def swipe_down(self, t=10, n=1):
        """
        向下滑动
        :return:
        """
        try:
            size = self.get_window_size()
            start_x = size[0] * 0.5
            start_y = size[1] * 0.25
            end_x = size[0] * 0.5
            end_y = size[1] * 0.75
            for i in range(n):
                self.driver.swipe(start_x, start_y, end_x, end_y, t)
        except:
            print("没有找到该元素")

    def swipe_up(self, t=10, n=1):
        """
        向上滑动
        :return:
        """
        try:
            size = self.get_window_size()
            start_x = size[0] * 0.5
            start_y = size[1] * 0.8
            end_x = size[0] * 0.5
            end_y = size[1] * 0.4
            for i in range(n):
                self.driver.swipe(start_x, start_y, end_x, end_y, t)

        except:
            print("没有找到该元素")

    def swipe_right(self, t=10, n=1):

        try:
            size = self.get_window_size()
            start_x = size[0] * 0.1
            start_y = size[1] * 0.5
            end_x = size[0] * 0.9
            end_y = size[1] * 0.5
            for i in range(n):
                self.driver.swipe(start_x, start_y, end_x, end_y, t)
        except:

            raise

    def swipe_left(self, t=10, n=1):
        try:
            size = self.get_window_size()
            start_x = size[0] * 0.9
            start_y = size[1] * 0.5
            end_x = size[0] * 0.1
            end_y = size[1] * 0.5
            for i in range(n):
                self.driver.swipe(start_x, start_y, end_x, end_y, t)
        except:
            raise

    def seipe_all(self):
        self.swipe_down()
        self.swipe_up()
        self.swipe_left()
        self.swipe_right()

    def base_checked(self, loc, isyonghxy):

        if isyonghxy == False:
            self.base_click(loc)
            print('勾选成功')
        else:
            print('已勾选协议')
        time.sleep(1)
