import higreen
import os

PATH = lambda p: os.path.abspath(p)
path = PATH(os.getcwd()).split('higreen')[0]
"""
登录测试数据文件路径
"""


jietbc = path + r'higreen\Outputs\screenshot\error_img'
"""
异常截图保存路径
"""

test_cases = path + 'higreen\script'
"""
获取测试用例路径--用例执行代码
"""

reports = path + r'higreen\Outputs\reports'
"""
报告保存路径
"""

xlsx_test_data = path + r"higreen\test_data\test_user_data.xlsx"
"""
测试数据
"""

shib_file_im = path + r"higreen\run\TestResult\123.png"
"""
文字——识别图片路径
"""

Original_file_path = path + r'higreen\run\TestResult'
"""
复制文件——复制文件路径
"""

new_file_path = path + r'higreen\Outputs\screenshot'
"""
复制文件——指定路径
"""

startAppiumServer = r'start {}higreen\base\comm\config\startAppiumServer.bat'.format(path)
"""
appium启动文件路径
"""

stopAppiumServer = r'start {}higreen\base\comm\config\stopAppiumServer.bat'.format(path)
"""
appium停止文件路径
"""

login_test_data = path + r"higreen\test_data\data_login.json"
"""
登录测试数据路径
"""

jiaojb_test_data = path + r'higreen\test_data\data_jiaojb.json'
"""交接班测试数据"""

chouccj_test_data = path + r"higreen\test_data\data_chouccj.json"
"""抽查抽检测试数据"""

shicxc_test_data = path + r"higreen\test_data\data_shicxc.json"
"""市场巡查测试数据"""
