import xlrd
from higreen.base.comm.config import file


def excel_to_list(sheet, data_file=file.test_data):
    """
    获取测试数据--列表嵌套字典格式
    获取工作簿中所有数据
    :param sheet: 工作簿
    :param data_file: .xlsx文件路径
    :return:
    """
    data_list = []
    wb = xlrd.open_workbook(data_file)
    """
    实例--要打开的.xlsx文件
    """
    sh = wb.sheet_by_name(sheet)
    """
    获取工作簿
    """
    header = sh.row_values(0)  # 获取标题行数据
    for i in range(1, sh.nrows):  # 跳过标题行，从第二行开始读取数据
        d = dict(zip(header, sh.row_values(i)))  # 将标题和每行数据组装成字典
        data_list.append(d)
    return data_list  # 列表嵌套字典格式，每个元素都是一个字典


def get_test_data(data_list, case_name):
    """
    获取某一条用例数据
    :param data_list: 工作簿中所有数据
    :param case_name: 测试用例名称
    :return:
    """

    for case_data in data_list:
        try:
            if case_name == case_data['title']:  # 注意：字典数据中case_name与参数一致
                return case_data
        except Exception as ree:
            print(">>>>>>>>>>>>>>>>:请检查测试数据用例名称标题是否与if中的《键》一致")
            return ree


if __name__ == "__main__":
    data_list = excel_to_list("TestLogin")  # 读取excel，TestUserLogin工作簿的所有数据
    print(data_list)
    data = get_test_data(data_list, '用户为空')
    print(data)
