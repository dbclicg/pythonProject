# -*- coding: utf-8 -*-
# @Time    : 2021/12/4 10:11
# @Author  : 牛逼哥
# @FileName: te.py
# @Software: PyCharm
import time

from higreen.page.element import login_element as element
from higreen.base.comm.base_operate_element import Base_operate_element


class Page_login_business(Base_operate_element):
    def page_shic(self):
        self.base_click(element.shic)
        """
        点击选择市场
        :return: 
        """
        self.base_target_click(810, 1200)
        """
        点击确认
        :return: 
        """


    def page_uesr(self, uesrname):
        self.base_sebnd_keys(element.uesr, uesrname)
        """
        输入账户
        :param uesrname: 账户
        :return: 
        """
        time.sleep(2)
    def page_pwd(self, pwd):
        self.base_sebnd_keys(element.pwd, pwd)
        """
        输入密码
        :param pwd: 密码
        :return: 
        """


    def page_yonghxy(self,isyonghxy):
        """
        勾选用户隐私协议
        :return:
        """
        self.base_checked(element.yonghxydxk, isyonghxy)


    def page_lijdl(self):
        """
        立即登录
        :return:
        """
        self.base_click(element.lijdl)



    def page_gongz(self):
        """
        点击工作
        :return:
        """
        self.base_click(element.gongz)


    # def page_yonghm(self):
    #     self.page_gongz()
    #     """
    #     判断登录成功，获取用户名称
    #     :return:
    #     """
    #     self.base_text(element.yonghm)

    def page_wod(self):
        """
        点击我的
        :return:
        """
        if self.base_find_element(element.wod, 2, 0.1):
            self.base_click(element.wod)
            return True
        else:
            return False

    def page_qiehzh(self):
        """
        点击切换账号
        :return:
        """
        self.base_click(element.qiehzh)

    def page_querqh(self):
        """
        点击确认切换
        :return:
        """
        self.base_click(element.quedqh)

    # def page_istuiccg(self):
    #     """
    #     判断是否登录成功
    #     :return:
    #     """
    #     self.base_text(element.tuiccg)

    def page_login(self, uesrname, pwd, isyonghxy):
        self.page_shic()
        self.page_uesr(uesrname)
        self.page_pwd(pwd)
        self.page_yonghxy(isyonghxy)
        self.page_lijdl()

    def page_zclogin(self):
        """正常登录账号"""
        self.page_shic()
        self.page_uesr(element.uesrname)
        self.page_pwd(element.password)
        self.page_yonghxy(element.isyonghxy)
        self.page_lijdl()
        self.base_click_system()

        #self.base_click(element.gongz)

    def page_jiaobrlogin(self, uesr, password1):
        """交接班人登录账号"""
        self.page_shic()
        self.page_uesr(uesr)
        self.page_pwd(password1)
        self.page_yonghxy(element.isyonghxy1)
        self.page_lijdl()



