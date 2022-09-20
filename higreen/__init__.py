import os

PATH = lambda p: os.path.abspath(p)


def os_getcwd():
    """
    获取到当前工作目录
    :return:
    """
    path = PATH(os.getcwd())
    return path


if __name__ == '__main__':
    print(os_getcwd())
