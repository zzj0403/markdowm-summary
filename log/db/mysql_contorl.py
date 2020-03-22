import pymysql
from db.poll import POOL


class Mysql:
    def __init__(self):
        # 链接mysql线程池
        self.mysql_client = POOL.connection()
        # 连接mysql返回字典类型的数据
        self.cursor = self.mysql_client.cursor(
            pymysql.cursors.DictCursor
        )
