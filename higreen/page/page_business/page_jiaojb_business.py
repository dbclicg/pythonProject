# -*- coding: utf-8 -*-
# @Time    : 2021/12/4 10:11
# @Author  : 牛逼哥
# @FileName: te.py
# @Software: PyCharm
import time

from higreen.page.element import jiaojb_element as element
from higreen.base.comm.base_operate_element import Base_operate_element


class Page_jiaojb_business(Base_operate_element):
    def page_click_gongz(self):
        """
        点击工作
        :return:
        """
        self.base_click(element.gongz)

    def page_click_jiaojb(self):
        """
        点击交接班
        :return:
        """
        x = False
        while x == False:
            self.swipe_up()
            if self.base_find_element(element.jiaojb, 5, 0.05):
                self.base_click(element.jiaojb)
                x = True
            else:
                x = False

    def page_click_jiaojan(self):
        """
        点击交班
        :return:
       """
        self.base_click(element.jiaojan)

    def page_clock_xuanzjbr(self):
        """
        点击选择接班人
        :return:
        """
        self.base_click(element.xuanzjbr)
        time.sleep(1)
        self.base_click(element.dianjijbr)

    def page_clock_xuanzbc(self):
        """
        选择接班班次
        :return:
        """
        self.base_click(element.dianjixzbc)
        time.sleep(1)
        self.base_click(element.xuanzbc)

    def page_clock_xuanzfzqy(self):
        """
        选择负责区域
        :return:
        """
        self.base_click(element.fuzqy)
        time.sleep(1)
        self.base_click(element.xuanzfzqy)
        time.sleep(1)
        self.base_click(element.tijiaofzqy)

    def page_sebnd_keys_wup(self, wup, wupsl):
        """
        输入物品与数量
        :return:
        """
        self.base_sebnd_keys(element.wup, wup)
        self.base_sebnd_keys(element.wupsl, wupsl)

    def page_clock_tianjiawp(self, wup01, wupsl01):
        """
        添加物品
        :return:
        """
        self.base_click(element.tianjiawp)
        self.base_sebnd_keys(element.wup01, wup01)
        self.base_sebnd_keys(element.wupsl01, wupsl01)

    def page_sebnd_keys_beiz(self, beizxx):
        """
        交接班现场情况描述
        :return:
        """
        self.base_sebnd_keys(element.beiz, beizxx)

    def page_clock_shangctp(self):
        """
        上传提交图片
        :return:
        """
        x = False
        while x == False:
            self.swipe_up()
            if self.base_find_element(element.tianjiatpan, 5, 0.05):
                self.base_click(element.tianjiatpan)
                time.sleep(1)
                self.base_click(element.xuanztp)
                self.base_click(element.tijiaotp)
                x = True
            else:
                x = False

    def page_clock_tijjb(self):
        """提交交班"""
        self.base_click(element.tijjb)

    def page_jiaojb(self, wup='ceshui', wupsl=10, wup01='ceshi01', wupsl01=20, beizxx='测试'):
        # Call_page(driver).login()
        self.page_click_gongz()
        self.page_click_jiaojb()
        self.page_click_jiaojan()
        self.page_clock_xuanzjbr()
        self.page_clock_xuanzbc()
        self.page_clock_xuanzfzqy()
        self.page_sebnd_keys_wup(wup, wupsl)
        self.page_clock_tianjiawp(wup01, wupsl01)
        self.page_sebnd_keys_beiz(beizxx)
        self.page_clock_shangctp()
        self.page_clock_tijjb()
