import os
import shutil
import unittest

from unittestreport import TestRunner
from higreen.base.comm.config import file


def run_cases(filename, tester, desc, title, templates=2, pattern="test_*.py", report_dir=file.reports):
    """
    :param title: 报告标题
    :param pattern:  要执行的测试用例----默认全部以test开头的文件
    :param filename: 文件名称
    :param report_dir: 生成报告路径
    :param tester: 测试人员
    :param desc: 项目名称`
    :param templates: 报告模板 1 or 2
    :return:
    """
    try:
        shutil.rmtree(file.new_file_path)
        os.mkdir(file.new_file_path)
        suite = unittest.defaultTestLoader.discover(file.test_cases, pattern)

        runner = TestRunner(suite, filename, report_dir, title, tester, desc, templates)
        runner.rerun_run(count=2, interval=1)
    except AttributeError as ree:
        raise ree


class Test_Run:
    pass


if __name__ == '__main__':
    run_cases("higreen_report", "李天浩", "平湖—海吉星app", "海吉星登录", pattern='test_shicxc.py')


