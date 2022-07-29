# -*- coding: utf-8 -*-
# @Time    : 2021/12/4 10:11
# @Author  : 牛逼哥
# @FileName: te.py
# @Software: PyCharm

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

"""市场"""
shic = By.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/base_content"]/android.widget.RelativeLayout[' \
                 '2]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1] '

"""确定市场"""
quedsc = By.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/bt_ok"]'

"""用户输入框"""
uesr = By.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/uesr_name"]'

"""密码输入框"""
pwd = By.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/user_pwd"]'

"""用户协议单选框"""
yonghxydxk = By.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/login_iv_privacyAgree"]'

"""立即登录"""
lijdl = By.XPATH, '//*[@text="立即登录"]'

"""工作"""
gongz = By.XPATH, '//*[@text="工作"]'

"""用户名称"""
yonghm = By.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/tv_user_name"]'

"""我的"""
wod = By.XPATH, '//*[@text="我的"]'

"""切换账号"""
qiehzh = By.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/layout_change_account"]'

"""确定切换账号"""
quedqh = By.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/tv_qx"]'

"""取消允许后台定位"""
quxhtdw = By.XPATH, "com.padmatek.szhigreenmb:id/dialog_common_btn_cancel"

"""退出成功text"""
tuiccg = By.XPATH, "//*[contains(@text,'退出')]"
