import random
import redis
from cookies_pool.config import *

class RedisClient:

    def __init__(self, type, website, host=REDIS_HOST, port=REDIS_PORT):
        """
        初始化数据库
        :param type: 账号 or cookies
        :param website: 爬取网站
        :param host: 地址
        :param port: 端口
        """
        self.db = redis.StrictRedis(host=host, port=port, decode_responses=True)
        self.type = type
        self.website = website

    def name(self):
        """
        获取hash名称
        :return:
        """
        return "{type}:{website}".format(type=self.type, website=self.website)

    def set(self, username, value):
        """
        设置键值队
        :param name:
        :param value:
        :return:
        """
        return self.db.hset(self.name(), username, value)

    def get(self, username):
        """
        根据键名获得键值
        :param username:
        :return:
        """
        return self.db.hget(self.name(), username)

    def delete(self, username):
        """
        根据键名删除键值队对
        :param username:
        :return:
        """
        return self.db.hdel(self.name(), username)

    def count(self):
        """
        获取数目
        :return:
        """
        return self.db.hlen(self.name())

    def random(self):
        """
        随机获得键值，用于cookies获取
        :return:
        """
        return random.choice(self.db.hvals(self.name()))

    def usernames(self):
        """
        获得所有账户信息
        :return:
        """
        return self.db.hkeys(self.name())

    def all(self):
        """
        获得所有键值对
        :return:
        """
        return self.db.hgetall(self.name())

if __name__ == '__main__':
    conn = RedisClient('cookies', 'weibo')
    # result1 = conn.set('test', 'testtest')
    # result2 = conn.name()
    # result3 = conn.get('test')
    # result33 = conn.set('test', 'testtest111')
    # result4 = conn.count()
    # result5 = conn.random()
    # result6 = conn.usernames()
    result7 = conn.all()

    # result8 = conn.delete('test')

    #
    # print(result1)
    # print(result2)
    # print(result3)
    # print(result4)
    # print(result5)
    # print(result6)
    print(result7)
    # print(result8)

