# -*- coding: utf-8 -*-
# coding=utf-8
# @Time    :
# @Author  :
# @FileName: te.py
# @Software: PyCharm
# @市场督导页面---定位元素

from appium.webdriver.common.appiumby import AppiumBy

shicddcd = AppiumBy.XPATH, '//*[@text="市场督导"]'
"""市场督导菜单"""

faqdd = AppiumBy.ID, "com.padmatek.szhigreenmb:id/start_supervision_btn"
"""发起督导"""

dudbt = AppiumBy.ID, "com.padmatek.szhigreenmb:id/title_edit"
"""督导标题"""

xuanzbt = AppiumBy.XPATH, '//*[@text="现场巡查"]'
"""选择督导标题"""

dudnr = AppiumBy.ID, "com.padmatek.szhigreenmb:id/content_edit"
"""请输入督导内容"""

dudwz = AppiumBy.ID, "com.padmatek.szhigreenmb:id/position_edit"
"""请输入督导位置"""

tupan = AppiumBy.ID, "com.padmatek.szhigreenmb:id/pic_iv"
"""上传图片按钮"""

xuanztup = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/grid"]/android.widget.FrameLayout[2]/android.widget.ImageView[2]'
"""选择上传图片"""

wanc = AppiumBy.ID, "com.padmatek.szhigreenmb:id/bt_right"
"""确认上传图片"""

tijbtn = AppiumBy.ID, "com.padmatek.szhigreenmb:id/commit_review_btn"
"""提交"""
