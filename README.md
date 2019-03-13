# Cookies_pool
一个可扩展的cookies池，已加入微博cookies

python3.6 + selenium + request + Flask + redis

## 先导入账号

运行python3 account-import.py

请输入账号密码组, 输入exit退出读入
xxx----xxx

账号 xxx 密码 xxx
录入成功
exit

## 运行

请先导入一部分账号之后再运行，运行命令：

python3 schedule.py  

schedule.run()多进程同时调用

generator.py中GetterWeiboCookiesGenerator(CookiesGenerator), 作用是调用cookies.py,用selenium模拟登录微博获取cookies

tester.py中的WeiboValidTester(ValidTester)，作用是使用requests携带cookies登录m.weibo.cn测试

api中的app.run()，作用是"http://127.0.0.1:5001/random/cookies"接口随机提供一个有效的cookies



