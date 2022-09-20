from higreen.page.page_business.page_login_business import Page_login_business
from higreen.page.page_business.page_jiaojb_business import Page_jiaojb_business
from higreen.page.page_business.page_shicxc_business import Page_shicxc
from higreen.page.page_business.page_chouccj_business import Page_Chouccj


class Call_page:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        """
        登录测试
        :return:
        """
        return Page_login_business(self.driver)

    def jiaojb(self):
        """
        交接班测试
        :return:
        """
        return Page_jiaojb_business(self.driver)

    def shicxc(self):
        """
        市场巡查测试
        :return:
        """
        return Page_shicxc(self.driver)

    def chouccj(self):
        """
        抽查抽检测试
        :return:
        """
        return Page_Chouccj(self.driver)
