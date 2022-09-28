# -*- coding: utf-8 -*-
# coding=utf-8
# @Time    : 
# @Author  : lcg
# @FileName: te.py
# @Software: PyCharm
from higreen.base.comm.base_operate_element import Base_operate_element
from higreen.page.element import chouczg_element as element


class Page_Chouczg(Base_operate_element):
    """抽查整改"""
    def page_click_chouczgcd(self):
        """点击抽查整改菜单"""
        self.swipe_element(element.chouczgcd)
        self.base_click(element.chouczgcd)

    def page_click_chouczgsj(self):
        """点击抽查整改数据"""
        self.base_click(element.chouczglbsj)

    def page_shangctp(self):
        """上传图片"""
        self.swipe_element(element.zhenggtp)
        self.base_click(element.zhenggtp)
        self.base_click(element.xuanztp)
        self.base_click(element.wanc)

    def page_sebnd_keys_zhenggsm(self, zgsm):
        """整改说明"""
        self.swipe_element(element.zhenggsm)
        self.base_sebnd_keys(element.zhenggsm, zgsm)

    def page_click_tij(self):
        """提交"""
        self.base_click(element.tij)

    def page_click_gongz(self):
        """点击工作"""
        self.base_click(element.gongz)

    def page_chouczg(self, zgsm):
        """提交抽查整改数据"""
        self.page_click_chouczgsj()
        self.page_shangctp()
        self.page_sebnd_keys_zhenggsm(zgsm)
        self.page_click_tij()