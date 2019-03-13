from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


option = webdriver.ChromeOptions()
option.add_argument('headless')

class WeiboCookies():
    def __init__(self, username, password):
        self.url = 'https://passport.weibo.cn/signin/login?entry=mweibo&r=https://m.weibo.cn/'
        self.driver = webdriver.Chrome(
            executable_path = 'D:\pycharm-work\spider-test\cookies_pool\chromedriver.exe',
            chrome_options = option
        )
        self.username = username
        self.password = password
        self.timeout = 10

    def open(self):
        """
        打开网页输入用户名和密码，并点击
        :return:
        """
        self.driver.get(url=self.url)
        self.driver.set_window_size(1920, 1080)

        username = WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.find_element_by_xpath('//*[@id="loginName"]')
        )
        password = WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.find_element_by_xpath('//*[@id="loginPassword"]')
        )
        sumbit = WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.find_element_by_xpath('//*[@id="loginAction"]')
        )

        username.send_keys(self.username)
        password.send_keys(self.password)
        time.sleep(1)
        sumbit.click()

        # validate = WebDriverWait(self.driver, self.timeout).until(
        #     lambda d:d.find_element_by_xpath('//span[@class="geetest_radar_tip_content"]')
        # )
        # time.sleep(1)
        # self.yanzheng.click()
    def password_error(self):
        """
        判断是否密码错误
        :return:
        """
        try:
            return WebDriverWait(self.driver, 5).until(
                EC.text_to_be_present_in_element((By.ID, 'errorMsg'), '用户名或密码错误'))
        except TimeoutException:
            return False

    def login_successfully(self):
        """
        判断是否登录成功
        :return:
        """
        try:
            return bool(
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'lite-iconf-profile'))))
        except TimeoutException:
                return False

    def get_cookies(self):
        """
        获取Cookies
        :return:
        """
        return self.driver.get_cookies()

    def get_valid(self):
        if self.driver.title == '请先验证身份':
            return True
        else:
            return False

    def main(self):
        self.open()
        if self.password_error():
            return{
                'status': 2,
                'content': '用户名或密码错误'
            }
            # 如果不需要验证码直接登录成功
        if self.get_valid():
            # print('进入验证页面', self.driver.current_url)
            time.sleep(5)
            print({
                'status': 4,
                'content': '验证失败'
            })
        if self.login_successfully():
            cookies = self.get_cookies()
            print(cookies)
            return {
                'status': 1,
                'content': cookies
            }
        else:
            return {
                'status': 3,
                'content': '登录失败'
            }

if __name__ == '__main__':
    result = WeiboCookies('13751678541', 'cjx8852077.').main()
    print(result)






