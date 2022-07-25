from appium.webdriver.common.appiumby import AppiumBy

"""工作"""
gongz = AppiumBy.XPATH, '//*[@text="工作"]'

"""交接班"""
jiaojb = AppiumBy.XPATH, '//*[@text="交接班"]'

"""交接"""
jiaojan = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/action_text"]'

"""选择接班人"""
xuanzjbr = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/layout_select_user"]'

"""点击接班人"""
dianjijbr = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/recycler"]/android.view.ViewGroup[1]/android.widget.LinearLayout[1]'

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
xuanztp = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/grid"]/android.widget.FrameLayout[2]/android.widget.ImageView[2]'

"""提交图片"""
tijiaotp = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/bt_right"]'

"""提交交班"""
tijjb = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/bt_commit"]'