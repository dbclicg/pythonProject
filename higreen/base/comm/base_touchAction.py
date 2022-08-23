from appium.webdriver.common.touch_action import TouchAction
from higreen.base.comm.base_find_element import Base_element


class Base_TouchAction(Base_element):
    """
    基础类--手势操作类
    """

    def base_tap(self, elemet, x=None, y=None):
        """
        tap轻敲操作
        :param y: Y轴坐标
        :param x: X轴坐标
        :param elemet: 元素
        :return: 可使用坐标或元素两种方式执行
        """
        ta = TouchAction(self.driver)
        el = self.base_find_element(elemet)
        ta.tap(el, x, y).perform()

    def base_press(self, elemet, x=None, y=None, ms=0):
        """
        press、release按下和抬起操作
        :param ms: 等待时间
        :param elemet: 元素
        :param x:
        :param y:
        :return: press按下，release抬起，wuit等待时间，perform执行
        """
        ta = TouchAction(self.driver)
        el = self.base_find_element(elemet)
        ta.press(el, x, y).wait(ms).release().perform()

    def base_long_press(self, elemet, x=None, y=None, duration=1000):
        """
        long_press长按操作
        :param elemet:
        :param x:
        :param y:
        :param duration: 长按时间，默认1000毫秒
        :return:
        """
        ta = TouchAction(self.driver)
        el = self.base_find_element(elemet)
        ta.long_press(el, x, y, duration)

    def swipe_find(self, X1, Y1, X2, Y2, X3, Y3, X4, Y4):
        """
        临时代码，适用部分多点连续滑动
        :param X1:
        :param Y1:
        :param X2:
        :param Y2:
        :param X3:
        :param Y3:
        :param X4:
        :param Y4:
        :return:
        """
        x_1 = X1 / 1080
        y_1 = Y1 / 2280
        x_2 = X2 / 1080
        y_2 = Y2 / 2280
        x_3 = X3 / 1080
        y_3 = Y3 / 2280
        x_4 = X4 / 1080
        y_4 = Y4 / 2280
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        ta = TouchAction(self.driver)
        try:
            ta.press(x=x_1 * x, y=y_1 * y, pressure=1).move_to(x=x_2 * x, y=y_2 * y,).wait(1000).move_to(x=x_3 * x, y=y_3 * y,).wait(
                1000).move_to(x=x_4 * x, y=y_4 * y).wait(1000).release().perform()
        except AssertionError as err:
            raise err

