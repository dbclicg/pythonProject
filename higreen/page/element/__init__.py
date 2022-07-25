# coding=utf-8
import unittest
import selenium
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MyTestCase(unittest.TestCase):

    def setUp(self):
        # super().setUp()
        print('selenium version = ', selenium.__version__)
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.2'
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps['appPackage'] = 'com.padmatek.szhigreenmb'
        desired_caps["noReset"] = True
        desired_caps['automationName'] = 'Uiautomator2'
        desired_caps['appActivity'] = 'com.ap.dbc.hjx.marker.app.Activity.Other.LauncherActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


    def testQQLogin(self):
        time.sleep(2)
        # self.driver.find_element(By.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/uesr_name"]').send_keys()
        # time.sleep(2)
        # self.driver.find_element(By.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/uesr_name"]').send_keys()
        # time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/login_iv_privacyAgree"]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@text="立即登录"]').click()
        time.sleep(0.5)
        print(self.driver.find_element(By.XPATH, ".//*[contains(@text,'用户密码不能')]").text)
        time.sleep(0.5)
        ele_toast = WebDriverWait(self.driver, 3, 0.01).until(
            EC.presence_of_element_located((By.XPATH, ".//*[contains(@text,'用户密码不能')]")))
        print(ele_toast)
        print(ele_toast.text)
        # 检查密码错误时候的toast信息：账号或密码错误，请重新输入。
        # time.sleep(5)
        # self.driver.find_element_by_xpath('//android.widget.EditText[@content-desc="请输入QQ号码或手机或邮箱"]').send_keys("2572652583")
        # time.sleep(5)
        # self.driver.find_element_by_id('com.tencent.qqlite:id/password').send_keys("1213213aa")
        # 检查用户名和密码均为空时候的提示信息:请输入账号
        # time.sleep(5)
        # self.driver.find_element_by_id('com.tencent.qqlite:id/login').click()
        # time.sleep(1)
        # ele_toast = WebDriverWait(self.driver, 3, 0.01).until(
        #     EC.presence_of_element_located((By.XPATH, ".//*[contains(@text,'请输入')]")))
        # print(ele_toast.text)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()