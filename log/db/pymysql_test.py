import pymysql
from db.poll import POOL


# CREATE TABLE `test` (
#   `id` int(11) NOT NULL AUTO_INCREMENT,,
#   `date` datetime NOT NULL,
#   `ip` varchar(255) NOT NULL,
#   `method` varchar(255) DEFAULT NULL,
#   `request` varchar(255) DEFAULT NULL,
#   `stat_code` varchar(255) DEFAULT NULL,
#   `boy_size` int(11) DEFAULT NULL,
#   `request_body` varchar(255) DEFAULT NULL,
#   `user_agent` varchar(255) DEFAULT NULL,
#   `request_time` datetime DEFAULT NULL,
#   `correct_log` enum('0','1') DEFAULT '0',
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8;


class Mysql:
    def __init__(self):
        # 链接mysql线程池
        self.mysql_client = POOL.connection()
        # 连接mysql返回字典类型的数据
        self.cursor = self.mysql_client.cursor(
            pymysql.cursors.DictCursor
        )

    def create(self, table_name):
        sql = " CREATE TABLE %s (`id` int(11) NOT NULL AUTO_INCREMENT,`date` datetime NOT NULL,`ip` varchar(255) NOT NULL,`method` varchar(255) DEFAULT NULL,`request` varchar(255) DEFAULT NULL,`stat_code` varchar(255) DEFAULT NULL,`boy_size` int(11) DEFAULT NULL,`request_body` varchar(255) DEFAULT NULL,`user_agent` varchar(255) DEFAULT NULL,`request_time` datetime DEFAULT NULL,`correct_log` enum('0','1') DEFAULT '0',PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;" % (
            self.table_name)
        self.cursor.execute(sql)

    # def inset(self, info_list):
    #     sql = " INSERT INTO %s( `date`, `ip`, `method`, `request`, `stat_code`, `boy_size`, `request_body`, `user_agent`, `request_time`, `correct_log`) VALUES (%s, %s, %s, %s,%s,%s, %s, %s, %s, %s, %s)"
    #     rows = self.cursor.execute(sql, (info_list[0],
    #                                      info_list[1],
    #                                      info_list[2],
    #                                      info_list[3],
    #                                      info_list[4],
    #                                      info_list[5],
    #                                      info_list[6],
    #                                      info_list[7],
    #                                      info_list[8],
    #                                      info_list[9],))
    #     return rows
    #
    # def close(self):
    #     # 先关闭游标
    #     self.cursor.close()
    #     # 再关闭数据库连接
    #     self.mysql_client.close()


mysql = Mysql()
mysql.create(test1)
