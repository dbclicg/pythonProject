from higreen.page.element import shicxc_element as element
from higreen.base.comm.base_operate_element import Base_operate_element
from time import sleep
from higreen.base.comm.base_touchAction import Base_TouchAction as touch


class Page_shicxc(Base_operate_element):
    def page_click_gongz(self):
        """
        点击工作
        :return:
        """
        self.base_click(element.gongz)

    def page_click_shicxccd(self):
        """
        点击市场巡查菜单
        :return:
        """
        self.swipe_element(element.shicxccd)
        self.base_click(element.shicxccd)

    def page_click_dangw(self):
        """
        点击档位选择框
        :return:
        """
        self.base_click(element.dangwei)

    def page_sebnd_keys_shousk(self, value):
        """
        搜索框——搜索
        :param value:
        :return:
        """
        self.base_sebnd_keys(element.dangweissk, value)
        self.base_click(element.sousxzdw)  # 点击搜索内容

    def page_click_xuanzdangw(self):
        """
        选中档位
        :return:
        """
        self.base_click(element.xuanzdangw)

    def page_click_xuncxm(self):
        """
        点击巡查项目
        :return:
        """
        self.base_click(element.xuncxm)

    def page_click_xuncnr(self):
        """
        点击巡查子项目
        勾选不合格巡查项
        :return:
        """
        self.base_click(element.xuncnr)

        self.base_click(element.xuanzbhgx)
        r = self.base_find_element(element.xuanzbhgx).is_selected()
        print("::::::::::::::::::::::::::", r)

    def page_shangcdwtp(self):
        """
        上传档位图片
        :return:
        """
        self.base_click(element.dangwpz)
        self.base_click_system()
        self.base_click(element.shoujpz)
        sleep(2)
        self.base_click(element.quedtp)

    def page_sahngcgltp(self):
        """
        上传阁楼图片
        :return:
        """
        self.base_click(element.gelpz)
        self.base_click_system()
        self.base_click(element.shoujpz)
        sleep(2)
        self.base_click(element.quedtp)

    def page_zhenggsj(self):
        """
        选择整改时间
        :return:
        """
        self.base_click(element.zhenggsj)
        self.base_click(element.quedrq)

    def page_zonghpf(self):
        """
        选择综合管理评分
        :return:
        """
        self.base_click(element.pingf)

    def page_dianzqm(self):
        """
        电子签名
        :return:
        """
        self.swipe_element(element.dianzqm)
        self.base_click(element.dianzqm)
        touch(self.driver).swipe_find(element.x1, element.y1, element.x2, element.y2, element.x3, element.y3, element.x4, element.y4)
        self.base_click(element.quedqm)

    def page_beiz(self, value):
        """
        输入备注
        :param value:
        :return:
        """
        self.swipe_element(element.beiz)
        self.base_sebnd_keys(element.beiz, value)

    def page_tij(self):
        """
        提交
        :return:
        """
        self.base_click(element.tij)

    def page_fail_shicxc(self, beiz='该数据为appium自动化测试数据'):
        """
        正常流程提交----不合格
        :param beiz:备注
        :return:
        """
        self.page_click_gongz()
        self.page_click_shicxccd()
        self.page_click_dangw()
        self.page_click_xuanzdangw()
        self.page_click_xuncxm()
        self.page_click_xuncnr()
        self.page_shangcdwtp()
        self.page_sahngcgltp()
        self.page_zhenggsj()
        self.page_zonghpf()
        self.page_dianzqm()
        self.page_beiz(beiz)
        self.page_tij()

    def page_pass_shicxc(self, beiz='该数据为appium自动化测试数据'):
        """
        正常流程提交----合格
        :param beiz:备注
        :return:
        """
        self.page_click_gongz()
        self.page_click_shicxccd()
        self.page_click_dangw()
        self.page_click_xuanzdangw()
        self.page_click_xuncxm()
        self.page_shangcdwtp()
        self.page_sahngcgltp()
        self.page_zonghpf()
        self.page_dianzqm()
        self.page_beiz(beiz)
        self.page_tij()

    def page_weikong_tijiao(self):
        """
        为空提交
        :return:
        """
        self.page_tij()

    def page_dangktpwk_tijiao(self):
        """
        档口图片为空提交
        :return:
        """
        self.page_click_dangw()
        self.page_click_xuanzdangw()
        self.page_sahngcgltp()
        self.page_zonghpf()
        self.page_dianzqm()
        self.page_tij()

    def page_zonghpfwk_tijiao(self):
        """
        综合评分为空提交
        :return:
        """
        self.page_click_dangw()
        self.page_click_xuanzdangw()
        self.page_shangcdwtp()
        self.page_sahngcgltp()
        self.page_dianzqm()
        self.page_tij()

    def page_dianzqmwk_tijiao(self):
        """
        电子签名为空提交
        :return:
        """
        self.page_click_dangw()
        self.page_click_xuanzdangw()
        self.page_shangcdwtp()
        self.page_sahngcgltp()
        self.page_zonghpf()
        self.page_tij()

    def fail_weikong_tijiao(self, beiz='该数据为appium自动化测试数据'):
        """
        为空提交
        :return:
        """
        self.page_click_xuncxm()
        self.page_click_xuncnr()
        self.page_shangcdwtp()
        self.page_sahngcgltp()
        self.page_zhenggsj()
        self.page_zonghpf()
        self.page_dianzqm()
        self.page_beiz(beiz)
        self.page_tij()

    def fail_dangktpwk_tijiao(self):
        """
        档口图片为空提交
        :return:
        """
        self.page_click_dangw()
        self.page_click_xuanzdangw()
        self.page_click_xuncxm()
        self.page_click_xuncnr()
        self.page_sahngcgltp()
        self.page_zhenggsj()
        self.page_zonghpf()
        self.page_dianzqm()
        self.page_tij()

    def fail_zonghpfwk_tijiao(self):
        """
        综合评分为空提交
        :return:
        """
        self.page_click_dangw()
        self.page_click_xuanzdangw()
        self.page_click_xuncxm()
        self.page_click_xuncnr()
        self.page_shangcdwtp()
        self.page_sahngcgltp()
        self.page_zhenggsj()
        self.page_dianzqm()
        self.page_tij()

    def fail_dianzqmwk_tijiao(self):
        """
        电子签名为空提交
        :return:
        """
        self.page_click_dangw()
        self.page_click_xuanzdangw()
        self.page_click_xuncxm()
        self.page_click_xuncnr()
        self.page_shangcdwtp()
        self.page_sahngcgltp()
        self.page_zhenggsj()
        self.page_zonghpf()
        self.page_tij()
