# -*- coding: utf-8 -*-
# coding=utf-8
# @Time    : 2021/12/4 10:11
# @Author  : 牛逼哥
# @FileName: te.py
# @Software: PyCharm
from appium.webdriver.common.appiumby import AppiumBy

"""工作"""
gongz = AppiumBy.XPATH, r'//*[@text="工作"]'

"""交接班"""
jiaojb = AppiumBy.XPATH, '//*[@text="交接班"]'

"""交接"""
jiaojan = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/action_text"]'

"""选择接班人"""
xuanzjbr = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/layout_select_user"]'

"""点击接班人"""
dianjijbr = AppiumBy.XPATH, '//*[@text="路浩"]'

"""点击选择接班班次"""
dianjixzbc = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/layout_select_shifts"]'

"""选择接班班次"""
xuanzbc = AppiumBy.XPATH, '//*[@text="早班"]'

"""负责区域"""
fuzqy = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/layout_select_area"]'

"""选择负责区域"""
xuanzfzqy = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/recycler"]/android.widget.LinearLayout[6]/android.widget.LinearLayout[' \
                            '1]/android.widget.ImageView[1] '

"""提交负责区域"""
tijiaofzqy = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/confirmBtn"]'

"""输入物品"""
wup = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/et_article_name"]'

"""输入物品数量"""
wupsl = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/et_article_num"]'

"""添加物品"""
tianjiawp = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/bt_add_switch_article"]'
wup01 = AppiumBy.XPATH, '//*[@text="物品名称"]'
wupsl01 = AppiumBy.XPATH, '//*[@text="0"]'

"""备注"""
beiz = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/et_remark"]'

"""图片上传"""
tianjiatpan = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/imageIv"]'

"""选择图片"""
xuanztp = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/grid"]/android.widget.FrameLayout[' \
                          '2]/android.widget.ImageView[2] '

"""提交图片"""
tijiaotp = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/bt_right"]'

"""提交交班"""
tijjb = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/bt_commit"]'

"""点击交接班列表"""
jiaojblist = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/recycler"]/android.widget' \
                             '.RelativeLayout[1] '

"""删除"""
shanc = AppiumBy.XPATH, '//*[@text="删除"]'

"""转到上一层级"""
fanh = AppiumBy.XPATH, '//*[@content-desc="转到上一层级"]'

"""我的"""
wod = AppiumBy.XPATH, '//*[@text="我的"]'

"""切换账号"""
qiehzh = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/layout_change_account"]'

"""确定切换账号"""
quedqh = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/tv_qx"]'

"""选择当班管理员"""
xuanzdbgly = AppiumBy.XPATH, '//*[@text="选择当班管理员"]'
danbgly = AppiumBy.XPATH, '//*[@text="邓东升"]'
danbglyquer = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/action_text"]'


xuanzgw = AppiumBy.XPATH, '//*[@text="请选择管理员岗位"]'

"""确定"""
quedgly = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/action_text"]'

"""岗位"""
gangw = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/recycler"]/android.view.ViewGroup[1]/android.widget.LinearLayout[1]'

"""电子签名"""
dianzqm = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/bt_signature"]'
"""电子签名第一个坐标"""
x1 = 350
y1 = 1600
"""电子签名第二个坐标"""
x2 = 700
y2 = 1600
"""电子签名第三个坐标"""
x3 = 480
y3 = 1300
"""电子签名第四个坐标"""
x4 = 480
y4 = 1900

"""确定电子签名"""
qued = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/bt_ok"]'

"""提交接班"""
tijiaojb = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/bt_commit"]'

""""""
tishi = AppiumBy.XPATH, '//*[@text="操作成功"]'
