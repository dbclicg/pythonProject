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
        el = self.base_find_element(elemet)
        self.ta.tap(el, x, y).perform()

    def base_press(self, elemet, x=None, y=None, ms=0):
        """
        press、release按下和抬起操作
        :param ms: 等待时间
        :param elemet: 元素
        :param x:
        :param y:
        :return: press按下，release抬起，wuit等待时间，perform执行
        """
        el = self.base_find_element(elemet)
        self.ta.press(el, x, y).wait(ms).release().perform()

    def base_long_press(self, elemet, x=None, y=None, duration=1000):
        """
        long_press长按操作
        :param elemet:
        :param x:
        :param y:
        :param duration: 长按时间，默认1000毫秒
        :return:
        """
        el = self.base_find_element(elemet)
        self.ta.long_press(el, x, y, duration)

    def swipe_find(self, X1, Y1, X2, Y2, X3, Y3, X4, Y4):
        ta = TouchAction(self.driver)
        try:
            ta.press(x=X1, y=Y1, pressure=1).move_to(x=X2, y=Y2).wait(1000).move_to(x=X3, y=Y3).wait(
                1000).move_to(x=X4, y=Y4).wait(1000).release().perform()
            print(">>>>>>>>>>>>>滑动坐标:第一个坐标X1:{} ,Y1:{} ,X2:{} ,Y2:{}".format(X1, Y1, X2, Y2, X3, Y3, X4, Y4))
        except AssertionError as err:
            raise err
