import cx_Oracle
# 注意：一定要加下面这两行代码，负责会中文乱码；
import os
from higreen.base.comm.config import sql_yj


def oracle_sql_fetchone(sql):
    """
    查询数据库数据
    :param sql: 执行的查询sql语句--字符串格式
    :return: 返回查询结果
    """
    try:
        os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
        db = cx_Oracle.connect("HIGREEN_PH", "HIGREEN_PH", "10.100.100.119:1521/tstdb")
        cursor = db.cursor()
        cursor.execute(sql)
        sql_return = cursor.fetchone()
        if sql_return is not None:
            print('sql查询返回数据：{}'.format(sql_return[0]))
            db.close()
            return sql_return[0]
        else:
            print("当前{}查询数据库数据为空，查询实际结果：{}".format(sql, sql_return))
            db.close()
    except Exception as err:
        raise err


def oracle_sql_fetchall(sql):
    try:
        os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
        db = cx_Oracle.connect("HIGREEN_PH", "HIGREEN_PH", "10.100.100.119:1521/tstdb")
        cursor = db.cursor()
        cursor.execute(sql)
        sql_return = cursor.fetchall()
        if sql_return is not None:
            print('sql查询返回数据：{}'.format(sql_return))
            db.close()
            return sql_return
        else:
            print("当前{}查询数据库数据为空，查询实际结果：{}".format(sql, sql_return))
            db.close()
    except Exception as err:
        raise err


if __name__ == '__main__':
    oracle_sql_fetchone(sql_yj.einspectitemrecord_sql)
    oracle_sql_fetchall(sql_yj.einspectitemrecord_sql)
