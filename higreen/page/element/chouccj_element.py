# -*- coding: utf-8 -*-
# coding=utf-8
# @Time    :
# @Author  :
# @FileName: te.py
# @Software: PyCharm
# @抽查抽检页面---定位元素
from appium.webdriver.common.appiumby import AppiumBy

gongz = AppiumBy.XPATH, r'//*[@text="工作"]'
"""工作"""

chouccjcd = AppiumBy.XPATH, r'//*[@text="抽查抽检"]'
"""抽查抽检菜单"""

choujcxk = AppiumBy.ID, "com.padmatek.szhigreenmb:id/gears_search_cet"
"""抽查档位号搜索框"""

chax = AppiumBy.ID, "com.padmatek.szhigreenmb:id/bt_search"
"""查询"""

bt_pass = AppiumBy.ID, "com.padmatek.szhigreenmb:id/bt_pass"
"""通过"""

bt_not_pass = AppiumBy.ID, "com.padmatek.szhigreenmb:id/bt_not_pass"
"""不通过"""

qiud_bt = AppiumBy.ID, "com.padmatek.szhigreenmb:id/tv_qx"
"""确定是否通过"""

"""不通过提交页面"""
xuncxm = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/list_check"]/android.widget.LinearLayout[2]'
"""巡查项目"""

xunczxm = AppiumBy.ID, "com.padmatek.szhigreenmb:id/fl_iv_select"
"""巡查子项目"""

dangwtp = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/gv_photo_select"]/android.widget.RelativeLayout[1]'
"""档位图片上传控件"""

geltp = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/gv_photo_select2"]/android.widget.RelativeLayout[1]'
"""阁楼图片上传控件"""

quedsctp = AppiumBy.XPATH, '//*[@resource-id="com.android.camera2:id/done_button"]'
"""确定上传图片"""

time_bt = AppiumBy.ID, "com.padmatek.szhigreenmb:id/tv_time"
"""整改时间"""

quedsj = AppiumBy.ID, 'android:id/button1'
"""确定时间"""

dianzqm = AppiumBy.ID, 'com.padmatek.szhigreenmb:id/bt_signature'
"""点击电子签名"""

quedqm = AppiumBy.ID, 'com.padmatek.szhigreenmb:id/bt_ok'
"""确定电子签名"""

remark = AppiumBy.ID, "com.padmatek.szhigreenmb:id/et_remark_check"
"""备注"""

tij = AppiumBy.ID, "com.padmatek.szhigreenmb:id/bt_right"
"""提交"""
