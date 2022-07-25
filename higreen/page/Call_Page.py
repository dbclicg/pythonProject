from higreen.page.page_business.page_login_business import Page_login_business
from higreen.page.page_business.page_jiaojb_business import Page_jiaojb_business


class Call_page:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        return Page_login_business(self.driver)

    def jiaojb(self):
        return Page_jiaojb_business(self.driver)
