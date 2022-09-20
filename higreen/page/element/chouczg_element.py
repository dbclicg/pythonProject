# -*- coding: utf-8 -*-
# coding=utf-8
# @Time    :
# @Author  :
# @FileName: te.py
# @Software: PyCharm
from appium.webdriver.webdriver import AppiumBy

chouczgcd = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/list_menue_select"]/android.widget.LinearLayout[2]/android.widget.GridView[1]/android.widget.RelativeLayout[7]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]'
"""抽查整改菜单"""

chouczglbsj = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/list_random_check_recorde"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[2]'
"""抽查整改列表数据"""

zhenggtp = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/gv_photo_select"]/android.widget.RelativeLayout[1]'
"""整改图片上传按钮"""

xuanztp = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/grid"]/android.widget.FrameLayout[2]/android.widget.ImageView[2]'
"""选择图片"""

wanc = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/bt_right"]'
"""完成--图片选择"""

zhenggsm = AppiumBy.ID, 'com.padmatek.szhigreenmb:id/et_remark'
"""整改说明"""

tij = AppiumBy.ID, 'com.padmatek.szhigreenmb:id/bt_right'
"""提交"""

