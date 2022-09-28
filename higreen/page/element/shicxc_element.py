# -*- coding: utf-8 -*-
# coding=utf-8
# @Time    :
# @Author  :
# @FileName: te.py
# @Software: PyCharm
# @市场巡查页面---定位元素
import random

from appium.webdriver.common.appiumby import AppiumBy

"市场巡查--页面元素"

gongz = AppiumBy.XPATH, r'//*[@text="工作"]'
"""工作"""

shicxccd = AppiumBy.XPATH, "//*[contains(@text,'市场巡查')]"
"市场巡查--市场巡查菜单"

dangwei = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/tv_shop_id"]'
"市场巡查--档位选择框"

dangweissk = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/gears_search_cet"]'
"市场巡查--档位搜索框"

sousxzdw = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/lv_search_result_popupwindow"]/android' \
                           '.widget.LinearLayout[2] '
"市场巡查--搜索选中档位"

xuanzdangw = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/list_select_shop_id"]/android.widget' \
                             '.LinearLayout[{}]/android.view.ViewGroup[1]/android.widget.FrameLayout[' \
                             '{}]/android.widget.FrameLayout[1] '.format(random.randint(1, 10), random.randint(1, 4))
"市场巡查--选中档位"

xuncxm = AppiumBy.XPATH, '//*[@text="消防巡查"]'
"""市场巡查--巡查项目"""

xuncnr = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/list_check"]/android.widget.LinearLayout[1]'
"市场巡查--巡查内容"

xuanzbhgx = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/list_small"]'
"""勾选不合格项"""

dangwpz = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/layout_select_time"]/android.widget' \
                          '.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.GridView[' \
                          '1]/android.widget.RelativeLayout[1] '
"""档位拍照"""

shoujpz = AppiumBy.XPATH, '//*[@resource-id="com.android.camera:id/v9_shutter_button_internal"]'
"""手机拍照"""

quedtp = AppiumBy.ID, "com.android.camera2:id/done_button"
"""确定图片"""

gelpz = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/gv_photo_select2"]/android.widget' \
                        '.RelativeLayout[1] '
"""阁楼拍照"""

zhenggsj = AppiumBy.ID, 'com.padmatek.szhigreenmb:id/tv_time'
"""整改时间"""

quedrq = AppiumBy.ID, 'android:id/button1'
"""确定日期"""

pingf = AppiumBy.ID, 'com.padmatek.szhigreenmb:id/tv_score_1'
"""综合管理评分"""

dianzqm = AppiumBy.ID, 'com.padmatek.szhigreenmb:id/bt_signature'
"""点击电子签名"""

# """电子签名第一个坐标"""
# x1 = 350
# y1 = 1600
# """电子签名第二个坐标"""
# x2 = 700
# y2 = 1600
# """电子签名第三个坐标"""
# x3 = 480
# y3 = 1300
# """电子签名第四个坐标"""
# x4 = 480
# y4 = 1900

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

quedqm = AppiumBy.ID, 'com.padmatek.szhigreenmb:id/bt_ok'
"""确定电子签名"""

beiz = AppiumBy.ID, 'com.padmatek.szhigreenmb:id/et_remark_check'
"""备注"""

tij = AppiumBy.ID, 'com.padmatek.szhigreenmb:id/bt_right'
"""提交"""

chakjcd = AppiumBy.ID, "com.padmatek.szhigreenmb:id/ly_look_check_time"
"""查看监测点"""

benyyxcjl = AppiumBy.ID, "com.padmatek.szhigreenmb:id/layout_check_over_record"
"""本月已巡查记录"""

"""=====巡查整改====="""
buhgjl = AppiumBy.ID, "com.padmatek.szhigreenmb:id/layout_check_unqualified"
"""不合格记录"""

buhglbsj = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/list_unqualifiled_recorde"]/android.widget.LinearLayout[1]'
"""不合格整改数据"""

zhenggtp = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/gv_photo_select"]/android.widget.RelativeLayout[1]'
"""整改图片"""

xuanztp = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/grid"]/android.widget.FrameLayout[2]/android.widget.ImageView[2]'
"""选择整改图片"""

wanc = AppiumBy.ID, "com.padmatek.szhigreenmb:id/bt_right"
"""完成图片选择"""

zhenggsm = AppiumBy.ID, "com.padmatek.szhigreenmb:id/et_remark"
"""整改说明"""

tijiao = AppiumBy.ID, "com.padmatek.szhigreenmb:id/bt_right"
"""提交"""

fanghui = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/iv_back"]/android.widget.ImageView[1]'
"""返回"""
