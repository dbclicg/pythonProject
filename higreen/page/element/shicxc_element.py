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

xuncnr = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/list_check"]'
"市场巡查--巡查内容"

xuanzbhgx = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/list_small"]/android.widget.RelativeLayout[' \
                            '1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1] '
"""勾选不合格项"""

dangwpz = AppiumBy.XPATH, '//*[@resource-id="com.padmatek.szhigreenmb:id/layout_select_time"]/android.widget' \
                          '.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.GridView[' \
                          '1]/android.widget.RelativeLayout[1] '
"""档位拍照"""

shoujpz = AppiumBy.XPATH, '//*[@resource-id="com.android.camera:id/v9_shutter_button_internal"]'
"""手机拍照"""

quedtp = AppiumBy.XPATH, '//*[@resource-id="com.android.camera:id/inten_done_apply"]'
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

buhgjl = AppiumBy.ID, "com.padmatek.szhigreenmb:id/layout_check_unqualified"
"""不合格记录"""

xuncxm_list = AppiumBy.XPATH, '//*[@text="消防巡查"]'
"""巡查项目列表"""
