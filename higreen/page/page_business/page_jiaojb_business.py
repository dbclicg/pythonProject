# -*- coding: utf-8 -*-
# @Time    : 2021/12/4 10:11
# @Author  : 牛逼哥
# @FileName: te.py
# @Software: PyCharm
import time
from higreen.page.element import jiaojb_element as element
from higreen.base.comm.base_operate_element import Base_operate_element
from higreen.base.comm.base_touchAction import Base_TouchAction as touch

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
        x = False
        while x == False:
            if self.base_find_element(element.dianjijbr, 2, 0.05):
                self.base_click(element.dianjijbr)
                x = True
            else:
                self.swipe_up()
                x = False

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

    def page_clock_xiangq(self):
        """查看交接班详情"""
        if self.base_find_element(element.jiaojblist):
            self.base_click(element.jiaojblist)
            return True
        else:
            print(">>>>>>>>找不到新增交接班信息数据，{}".format(element.jiaojblist))
            return False

    def page_clock_shanc(self):
        """删除按钮"""
        if self.base_find_element(element.shanc):
            self.base_click(element.shanc)
        else:
            print(">>>>>>>>找不到新增交接班信息数据，{}".format(element.shanc))

    def page_fanghui(self):
        """返回"""
        self.base_click(element.fanh)

    def page_clock_tuic(self):
        """切换接班人账号"""
        self.base_click(element.wod)
        self.base_click(element.qiehzh)
        self.base_click(element.quedqh)

    def page_xuanzgly(self):
        """
        选择管理员
        :return:
        """
        self.base_click(element.xuanzdbgly)
        x = False
        while x == False:
            if self.base_find_element(element.danbgly, 2, 0.05):
                self.base_click(element.danbgly)
                time.sleep(1)
                self.base_click(element.danbglyquer)
                x = True
            else:
                self.swipe_up()
                x = False

    def page_quedgly(self):
        """
        选择岗位
        :return:
        """
        #self.base_elements_click(element.xuanzgw)
        elementlist = self.base_find_elements(element.xuanzgw)
        elementlists = len(elementlist)
        print(">>>>>>>>列表：", len(elementlist))
        for i in range(elementlists):
            self.base_click(element.xuanzgw)
            self.base_click(element.gangw)

    def page_dianzqm(self):
        """电子签名"""
        x = False
        while x == False:
            self.swipe_up()
            if self.base_find_element(element.dianzqm, 5, 0.05):
                self.base_click(element.dianzqm)
                time.sleep(1)
                touch(self.driver).swipe_find(element.x1, element.y1, element.x2, element.y2, element.x3, element.y3, element.x4,
                                element.y4)
                self.base_click(element.qued)
                x = True
            else:
                x = False

    def page_tijiaojb(self):
        """提交接班"""
        self.base_click(element.tijiaojb)

    def page_jiaojb(self, wup='ceshui', wupsl=10, wup01='ceshi01', wupsl01=20, beizxx='测试'):
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

    def page_jieb(self):
        self.page_click_gongz()
        self.page_click_jiaojb()
        self.page_clock_xiangq()
        self.page_xuanzgly()
        self.page_quedgly()
        self.page_dianzqm()
        self.page_tijiaojb()

