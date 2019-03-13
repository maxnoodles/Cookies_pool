import json
import requests
from requests.exceptions import ConnectionError
from cookies_pool.db import RedisClient
from cookies_pool.config import *

class ValidTester(object):
    def __init__(self, website='default'):
        self.website = website
        self.cookiers_db = RedisClient('cookies', self.website)
        self.accounts_db = RedisClient('accounts', self.website)

    def test(self, username, cookies):
        raise NotImplementedError

    def run(self):
        cookies_groups = self.cookiers_db.all()
        for username, cookies in cookies_groups.items():
            self.test(username, cookies)

class WeiboValidTester(ValidTester):
    def __init__(self, website='weibo'):
        ValidTester.__init__(self, website)

    def test(self, username, cookies):
        print('正在测试Cookies','用户名',username)
        try:
            cookies = json.loads(cookies)
        except:
            self.cookiers_db.delete(username)
            print('Cookies不合法,已删除',username)
        try:
            test_url = TEST_URL_MAP[self.website]
            response = requests.get(url=test_url, cookies=cookies, timeout=5, allow_redirects=False)
            if response.status_code == 200:
                print('Cookies有效', username)
            else:
                print(response.status_code, response.headers)
                self.cookiers_db.delete(username)
                print('Cookies失效, 已删除', username)
        except ConnectionError as e:
            print('发生异常', e.args)


if __name__=='__main__':
    WeiboValidTester().run()
