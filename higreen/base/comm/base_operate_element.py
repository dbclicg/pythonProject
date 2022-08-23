# -*- coding: utf-8 -*-
# coding=utf-8
# @Time    : 2021/12/4 10:11
# @Author  :
# @FileName: te.py
# @Software: PyCharm
import os
import time
import shutil
from PIL import Image
from selenium.webdriver.common.by import By
import easyocr
from higreen.base import comm
from appium.webdriver.common.appiumby import AppiumBy
from higreen.base.comm.config import file
from higreen.base.comm import base_find_element
from fuzzywuzzy import process

PATH = lambda p: os.path.abspath(p)
sure_text = comm.sure_text


class Base_operate_element(base_find_element.Base_element):
    # PATH = lambda p: os.path.abspath(p)
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
        print(">>>>>>>>>提示：", el_toast)
        return el_toast

    def base_toast_content(self, message):
        """
        自定义一个获取 toast内容的方法
        获取3秒提示信息
        :param message: 提示信息
        :return:
        """
        tmp_feature = By.XPATH, "//*[contains(@text,'%s')]" % message
        ele = self.base_find_element(tmp_feature, 3, 0.05).text
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", ele)
        return ele

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
            toast_loc = (By.XPATH, ".//*[contains(@text,'%s')]" % text)
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
        self.driver.get_screenshot_as_file(file.jietbc + r'\{}.png'.format(
            time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))))

    def screenshot(self, testcase="123"):
        """
        截图。并剪切截图
        :param testcase:
        :return:
        """
        path = PATH(os.getcwd() + "/TestResult")  # 获取当前目录拼接/TestResult
        if not os.path.isdir(PATH(os.getcwd() + "/TestResult")):  # 判断 /TestResult 是否存在，不存在则创建
            os.makedirs(path)
        os.popen("adb wait-for-device")
        time.sleep(1)  # 由于多次出现截图延迟现象（每次截图都截的是上次操作的画面），故此处设置一个等待
        os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
        time.sleep(1)
        os.popen("adb pull /data/local/tmp/tmp.png " + PATH(path + "/" + testcase + '.png'))
        time.sleep(1)
        os.popen("adb shell rm /data/local/tmp/tmp.png")
        time.sleep(1)
        im = Image.open(PATH(path + "/" + testcase + '.png'))
        cropedIm = im.crop((0, 400, 720, 1000))
        cropedIm.save(PATH(path + "/" + testcase + '.png'))

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

    def base_target_click(self, X1, Y1):  # x1,y1为你编写脚本时适用设备的实际坐标
        """
        使用坐标定位元素
        """
        x_1 = X1 / 900  # 计算坐标在横坐标上的比例，其中900为宽810
        y_1 = Y1 / 1600  # 计算坐标在纵坐标1600为高1200
        x = self.driver.get_window_size()['width']  # 获取设备的屏幕宽度
        y = self.driver.get_window_size()['height']  # 获取设备屏幕的高度
        self.driver.tap([(x_1 * x, y_1 * y)], 500)  # 模拟单手点击操作

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
        """
        向右滑动
        :param t:
        :param n:
        :return:
        """
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
        """
        向左滑动
        :param t:
        :param n:
        :return:
        """

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

    def seipe_all(self, direction, t=10, n=1):
        """
        'down'：向下滑动
        'up'：向上滑动
        'left'：向左滑动
        'right'：向右滑动
        :param n: 滑动次数
        :param t: 滑动时间
        :param direction: 滑动方向
        :return:
        """
        if direction == 'down':
            self.swipe_down(t, n)
        elif direction == 'up':
            self.swipe_up(t, n)
        elif direction == 'left':
            self.swipe_left(t, n)
        elif direction == 'right':
            self.swipe_right(t, n)
        else:
            print("请传参数 'down' or 'up' or 'left' or 'right'")

    def swipe_element(self, el):
        """
        边滑动边定位查找元素
        :param el:
        :return:
        """
        x = False
        t = 0
        try:
            while not x or t == 5:
                if self.base_find_element(el, time=2, poll=0.05):
                    x = True
                    print(">>>>>>>>", x)
                    return x

                else:
                    self.swipe_up()
                    t += 1
                    x = False
                    return x
        except Exception as ree:
            print("未查找到>>>>>>>>>>：{}， 详情查看下述报错信息".format(el))
            return ree

    def is_text(self, expect_text, title):
        """
        识别截图文字获取提示信息，判断测试结果
        :param desc:
        :param expect_text:  预期结果
        :return:
        """
        reader = easyocr.Reader(['ch_sim', 'en'])
        result = reader.readtext(file.shib_file_im, detail=0)
        try:
            ext = process.extractOne(expect_text, result)
            if ext[1] >= 80:
                print("截图识别的比较相似度为：{}>>>>>>>>>实际识别结果:".format(ext[1]), ext[0])
                return True
            if ext[1] <= 50:
                print("截图识别的比较相似度为：{}>>>>>>>>>实际识别结果:".format(ext[1]), ext[0])
                self.copy_files(title)
                return False
        except Exception:
            self.copy_files(title)
            return False

    def copy_files(self, newname):
        """
        复制文件到指定目录下并重命名文件名称
        :param newname: 文件新名称
        :return:
        """
        for foldName, subfolders, filenames in os.walk(file.Original_file_path):
            """
            使用os.walk方法将传入文件路径分解成：目录路径、目录名称、子文件名（是一个列表）
            """
            for filename in filenames:
                if filename == r'123.png':
                    if filename.endswith('.png'):
                        new_name = filename.replace('123.png', '{}.png'.format(newname))
                        """
                        将123.png文件名，重命名为调用传入的newname
                        """
                        if os.path.isdir(os.path.join(file.new_file_path, new_name)):
                            """
                            判断newname文件是否存在，存在则执行删除
                            """
                            os.remove(os.path.join(file.new_file_path, new_name))
                            shutil.copyfile(os.path.join(foldName, filename),
                                            os.path.join(file.new_file_path, new_name))
                        else:
                            shutil.copyfile(os.path.join(foldName, filename),
                                            os.path.join(file.new_file_path, new_name))
                            """
                            将文件复制到
                            """
                        print(os.path.join(foldName, filename), "<<<复制到>>>",
                              os.path.join(file.new_file_path, new_name))

    def base_checked(self, loc, isyonghxy):
        if not isyonghxy:
            self.base_click(loc)
            print('勾选成功')
        else:
            print('已勾选协议')
        time.sleep(1)

    def base_is_enabled(self, el):
        """判断元素是否可用"""
        elemen = self.base_find_element(el)
        return elemen.is_enabled()

    def base_click_system(self, suretext=comm.sure_text, cycle=3):
        for i in range(cycle):
            """
            处理系统弹窗
            """
            for a in suretext:
                try:
                    popup = self.driver.find_element(AppiumBy.XPATH, "//*[@text='%s']" % a)
                    if popup:
                        popup.click()
                    else:
                        print(">>>>>>>>>>>>没有系统权限提示")
                except:
                    pass


if __name__ == '__main__':
    base = Base_operate_element(driver=None)
    print(base.is_text("234", "用户名或密码错误"))
