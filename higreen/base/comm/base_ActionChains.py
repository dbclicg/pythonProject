
from selenium.webdriver import ActionChains

from higreen.base.comm.base_find_element import Base_element


class Base_ActionChains(Base_element):
    """
    基础类--手势操作类
    """
    def __int__(self):
        self.action = ActionChains(self.driver)

    def base_action_move_to_element(self, elemet):
        """
        鼠标悬停操作
        :param elemet: 元素
        :return: 鼠标悬停操作
        """
        el = self.base_find_element(elemet)
        self.action.move_to_element(el).perform()

    def base_action_click(self, elemet):
        """
        w3c点击操作
        :param elemet: 元素
        :return:el 为空则点击指针当前位置
        """
        el = self.base_find_element(elemet)
        self.action.click(el).perform()


