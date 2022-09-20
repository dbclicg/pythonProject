# -*- coding: utf-8 -*-
# @Time    : 2021/12/4 10:11
# @Author  :
# @FileName: te.py
# @Software: PyCharm
from higreen.base.comm.base_operate_element import Base_operate_element as base
from higreen.page.element import chouccj_element as element
from higreen.base.comm.config import sql_yj
from higreen.base.comm import sql_oracle
from higreen.base.base_driver.base_driver import Driver
from higreen.base.comm import adb_os


class Page_Chouccj(base):

    def page_click_gongz(self):
        """点击工作tab页"""
        self.base_click(element.gongz)

    def page_click_chouccjcd(self):
        """点击抽查抽检菜单"""
        self.swipe_element(element.chouccjcd)
        self.base_click(element.chouccjcd)

    def page_sebnd_keys_choucdw(self):
        """输入抽查档位号"""
        sql = sql_oracle.oracle_sql_fetchone(sql_yj.einspectitemrecord_sql)
        """sql查询已巡查档位"""
        print('===', sql)
        self.base_sebnd_keys(element.choujcxk, sql)
        self.base_click(element.chax)

    def page_click_chouctg(self):
        """点击通过"""
        self.base_click(element.bt_pass)

    def page_click_qued(self):
        """通过二级确定"""
        self.base_click(element.qiud_bt)

    def page_chouccj_pass(self):
        """抽查抽检---通过"""
        # self.page_click_gongz()
        # self.page_click_chouccjcd()
        self.page_sebnd_keys_choucdw()
        self.page_click_chouctg()
        self.page_click_qued()

    def page_click_not_pass(self):
        """点击不通过"""
        self.base_click(element.bt_not_pass)

    def page_click_xuncxm(self):
        """勾选巡查项目"""
        self.base_click(element.xuncxm)
        self.base_click(element.xunczxm)

    def page_shangcdwtp(self):
        """上传档口图片"""
        self.base_click(element.dangwtp)
        adb_os.adb_keyevent(27)
        self.base_click(element.quedsctp)

    def page_shangcgltp(self):
        """上传阁楼图片"""
        self.base_click(element.geltp)
        adb_os.adb_keyevent(27)
        self.base_click(element.quedsctp)

    def page_xunzsj(self):
        """选择整改时间"""
        self.base_click(element.time_bt)
        self.base_click(element.quedsj)

    def page_dianzqm(self):
        """
        电子签名
        :return:
        """
        self.swipe_element(element.dianzqm)
        self.base_click(element.dianzqm)
        self.swipe_find()
        self.base_click(element.quedqm)

    def page_beiz(self, value):
        """
        输入备注
        :param value: 备注
        :return:
        """
        self.base_sebnd_keys(element.remark, value)

    def page_tij(self):
        """提交"""
        self.base_click(element.tij)

    def page_chouccj_not_pass(self, value='抽查抽检---不通过'):
        """
        抽查抽检---不通过
        :param value: 备注
        :return:
        """
        # self.page_click_gongz()
        # self.page_click_chouccjcd()
        self.page_sebnd_keys_choucdw()
        self.page_click_not_pass()
        self.page_click_xuncxm()
        self.page_shangcdwtp()
        self.page_shangcgltp()
        self.page_xunzsj()
        self.page_dianzqm()
        self.page_beiz(value)
        self.page_tij()


if __name__ == '__main__':
    driver = Driver.driver_get()
    a = Page_Chouccj(driver)
    a.page_chouccj_not_pass()
