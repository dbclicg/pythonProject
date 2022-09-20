# -*- coding: utf-8 -*-
# coding=utf-8
# @Time    :
# @Author  :
# @FileName: te.py
# @Software: PyCharm
# @交接班页面---定位元素

from appium.webdriver.common.appiumby import AppiumBy

"""<<<<<<<<<<<<<<交班>>>>>>>>>>>>"""

gongz = AppiumBy.XPATH, r'//*[@text="工作"]'
"""工作"""

jiaojbcd = AppiumBy.XPATH, '//*[@text="交接班"]'
"""交接班菜单"""

jiaoban = AppiumBy.ID, 'com.padmatek.szhigreenmb:id/action_text'
"""交班按钮"""

jiebrxzk = AppiumBy.ID, "com.padmatek.szhigreenmb:id/layout_select_user"
"""接班人选择框"""

jiebbcxzk = AppiumBy.ID, "com.padmatek.szhigreenmb:id/layout_select_shifts"
"""班次选择框"""

fuzqyxzk = AppiumBy.ID, "com.padmatek.szhigreenmb:id/layout_select_area"
"""负责区域选择框"""

quyu_list = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/recycler"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]'
"""区域_列表"""

quyutj = AppiumBy.ID, "com.padmatek.szhigreenmb:id/confirmBtn"
"""区域提交按钮"""

wup_name = AppiumBy.XPATH, '//*[@text="物品名称"]'
"""物品名称"""

wup_num = AppiumBy.XPATH, '//*[@text="0"]'
"""物品数量"""

tianjwp = AppiumBy.ID, "com.padmatek.szhigreenmb:id/bt_add_switch_article"
"""添加物品"""

beiz = AppiumBy.ID, "com.padmatek.szhigreenmb:id/et_remark"
"""交接现场管理情况"""

tupscan = AppiumBy.ID, "com.padmatek.szhigreenmb:id/imageIv"
"""图片"""

xuanztp1 = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/grid"]/android.widget.FrameLayout[2]'
xuanztp2 = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/grid"]/android.widget.FrameLayout[3]'
xuanztp3 = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/grid"]/android.widget.FrameLayout[4]'
"""选中图片"""

tijtp = AppiumBy.ID, "com.padmatek.szhigreenmb:id/bt_right"
"""确定上传图片"""

tijiao = AppiumBy.ID, "com.padmatek.szhigreenmb:id/bt_commit"
"""提交"""

fanghui = AppiumBy.XPATH, '//*[@content-desc="转到上一层级"]'
"""返回"""

jiaobsj = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/recycler"]/android.widget.RelativeLayout[1]'
"""交接班列表数据"""

shanc = AppiumBy.XPATH, '//*[@text="删除"]'
"""删除交班"""

quedsc = AppiumBy.ID, 'com.padmatek.szhigreenmb:id/dialog_common_btn_confirm'
"""确定删除"""

"""<<<<<<<<<<<<<<接班>>>>>>>>>>>>"""

dangbgly = AppiumBy.ID, 'com.padmatek.szhigreenmb:id/tv_switch_work_executor'
"""选择当班管理员"""

xuanzdbgly = AppiumBy.XPATH, '//*[@text="邓东升"]'
"""当班管理员"""

qued = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/action_text"]'
"""确定"""

guanlygw = AppiumBy.XPATH, '//*[@text="请选择管理员岗位"]'
"""管理员岗位"""

xuanzglygw = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/recycler"]/android.view.ViewGroup[1]/android.widget.LinearLayout[1]'
"""选择管理员岗位"""

dianzqm = AppiumBy.ID, "com.padmatek.szhigreenmb:id/bt_signature"
"""电子签名按钮"""

X1 = 350
Y1 = 1550
X2 = 700
Y2 = 1550
X3 = 525
Y3 = 1350
X4 = 525
Y4 = 2000
X5 = 525
Y5 = 1550
X6 = 400
Y6 = 1750
X7 = 525
Y7 = 1550
X8 = 650
Y8 = 1750
dianzqmqd = AppiumBy.ID, "com.padmatek.szhigreenmb:id/bt_ok"
"""电子签名确定"""

jiebtj = AppiumBy.ID, "com.padmatek.szhigreenmb:id/bt_commit"
"""接班提交"""
