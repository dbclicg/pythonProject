from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class Base_element:
    def __init__(self, driver):
        self.driver = driver

    def base_find_element(self, loc, time=30, poll=0.5):
        """
        :find元素函数
        :param loc: 元素---转换成元组
        :param time: find超时时长
        :param poll: 每隔xx秒find一次
        :return:
        """
        try:
            return WebDriverWait(self.driver, timeout=time, poll_frequency=poll).until(lambda x: x.find_element(*loc))

        except Exception:
            print("元素获取失败，正在重新定位元素：{}".format(loc))

    def base_find_elements(self, loc, time=30, poll=0.5):
        """
        :find元素函数__返回一个列表
        :param loc: 元素---转换成元组
        :param time: find超时时长
        :param poll: 每隔xx秒find一次
        :return:
        """
        try:
            return WebDriverWait(self.driver, timeout=time, poll_frequency=poll).until(lambda x: x.find_elements(*loc))
        except Exception:
            print("元素获取失败，正在重新定位元素：{}".format(loc))

    def base_find_element_located(self, loc):
        """
        :find元素函数
        :param loc: 元素
        :param time: find超时时长
        :param poll: 每隔xx秒find一次
        :return:
        """
        try:

            return WebDriverWait(self.driver, 5, 0.001).until(ec.presence_of_element_located((By.XPATH, loc))).text

        except Exception:
            print("元素获取失败，正在重新定位元素：{}".format(loc))



