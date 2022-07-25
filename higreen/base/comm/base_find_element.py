from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


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
        except Exception as ree:
            print('element,find{}元素错误输出：'.format(loc), ree)

    def base_find_elements(self, loc, time=30, poll=0.5):
        """
        :find元素函数
        :param loc: 元素---转换成元组
        :param time: find超时时长
        :param poll: 每隔xx秒find一次
        :return:
        """
        try:
            return WebDriverWait(self.driver, timeout=time, poll_frequency=poll).until(lambda x: x.find_elements(*loc))
        except Exception as ree:
            print('elements,find{}元素错误输出：'.format(loc), ree)

    def base_find_element_located(self, loc, time=10, poll=0.01):
        """
        :find元素函数
        :param loc: 元素---转换成元组
        :param time: find超时时长
        :param poll: 每隔xx秒find一次
        :return:
        """
        try:
            return WebDriverWait(self, time, poll).until(ec.presence_of_element_located(*loc))
        except Exception as ree:
            print('element,find{}元素错误输出：'.format(loc), ree)

    def base_find_elements_located(self, loc, time=10, poll=0.01):
        """
        :find元素函数
        :param loc: 元素---转换成元组
        :param time: find超时时长
        :param poll: 每隔xx秒find一次
        :return:
        """
        try:
            return WebDriverWait(self, time, poll).until(ec.presence_of_all_elements_located(*loc))
        except Exception as ree:
            print('element,find{}元素错误输出：'.format(loc), ree)

    def aatest(self, message):

        TEST = WebDriverWait(self.driver, 8, 0.1).until(
            ec.presence_of_element_located((MobileBy.XPATH, '//*[contains(@text,{})]'.format(message))))
        print('=====', TEST.text)
        return TEST.text
