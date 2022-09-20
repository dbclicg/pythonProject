# -*- coding: utf-8 -*-
# @Time    : 2021/12/4 10:11
# @Author  : 牛逼哥
# @FileName: te.py
# @Software: PyCharm
# @登录页面---定位元素
from appium.webdriver.common.mobileby import AppiumBy
from selenium.webdriver.common.by import By

"""正常登录账号密码"""
uesrname = 'licc'
password = '123456'
isyonghxy = False

"""正常登录账号密码"""
uesrname1 = 'luhao'
password1 = '1234'
isyonghxy1 = False


shic = By.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/base_content"]/android.widget.RelativeLayout[' \
                 '2]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1] '
"""市场"""


quedsc = By.XPATH, '//*[@text="确定"]'
"""确定市场"""

uesr = By.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/uesr_name"]'
"""用户输入框"""

pwd = By.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/user_pwd"]'
"""密码输入框"""

yonghxydxk = By.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/login_iv_privacyAgree"]'
"""用户协议单选框"""

lijdl = By.XPATH, '//*[@text="立即登录"]'
"""立即登录"""

gongz = By.XPATH, '//*[@text="工作"]'
"""工作"""

yonghm = By.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/tv_user_name"]'
"""用户名称"""

wod = By.XPATH, '//*[@text="我的"]'
"""我的"""

qiehzh = By.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/layout_change_account"]'
"""切换账号"""

quedqh = By.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/tv_qx"]'
"""确定切换账号"""

quxhtdw = By.XPATH, "com.padmatek.szhigreenmb:id/dialog_common_btn_cancel"
"""取消允许后台定位"""

tuiccg = By.XPATH, "//*[contains(@text,'退出')]"
"""退出成功text"""