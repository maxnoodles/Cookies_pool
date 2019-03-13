from cookies_pool.db import RedisClient
from cookies_pool.cookies import WeiboCookies
from cookies_pool import config
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import json

class CookiesGenerator(object):
    def __init__(self, website='default'):
        """
        父类，初始化对象
        :param website:
        """
        self.website = website
        self.cookies_db = RedisClient('cookies', self.website)
        self.accounts_db = RedisClient('accounts', self.website)
        self.browser = webdriver.Chrome()

    def __del__(self):
        self.close()

    def new_cookies(self, username, password):
        """
        新生成子类，子类需要重写（方便扩展）
        :param user: 用户名
        :param password: 密码
        :return:
        """
        raise NotImplementedError

    def process_cookies(self, cookies):
        """
        处理cookies
        :param cookies:
        :return:
        """
        dict={}
        for cookie in cookies:
            dict[cookie['name']] = cookie['value']
        return dict

    def run(self):
        """
        运行，得到所有账户，然后顺次模拟登陆
        :return:
        """
        accounts_usernames = self.accounts_db.usernames()
        # print(self.accounts_db.usernames())
        cookies_usernames = self.cookies_db.usernames()

        for username in accounts_usernames:
            if not username in cookies_usernames:
                password = self.accounts_db.get(username)
                print('正在生成cookies','账号',username,'密码',password)
                result = self.new_cookies(username, password)
                if result.get('status') == 1:
                    cookies = self.process_cookies(result.get('content'))
                    print('成功获取cookies')
                    if self.cookies_db.set(username, json.dumps(cookies)):
                        print('成功保存cookies')

                elif result.get('status') == 2:
                    print(result.get('content'))
                    if self.accounts_db.delete(username):
                        print('成功删除账号')

                else:
                    print(result.get('content'))

    def close(self):
        """
        关闭
        :return:
        """
        try:
            print('关闭浏览器')
            self.browser.close()
            del self.browser
        except TypeError:
            print('Browser not opened')


class WeiboCookiesGenerator(CookiesGenerator):

    def __init__(self, website='weibo'):
        """
        初始化子类
        :param website:
        """
        CookiesGenerator.__init__(self, website)
        self.website = website

    def new_cookies(self, username, password):
        """
        生成cookies
        :param user:
        :param password:
        :return:
        """
        return WeiboCookies(username, password).main()

if __name__ == '__main__':
    generator = WeiboCookiesGenerator()
    generator.run()




