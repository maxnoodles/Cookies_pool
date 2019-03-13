# redis数据库地址
REDIS_HOST = 'localhost'

# redis端口
REDIS_PORT = 6379

# API地址和端口
API_HOST = 'localhost'
API_PORT = 5001

# 产生器类，如扩展其他站点，请在此配置
GENERATOR_MAP = {
    'weibo':'WeiboCookiesGenerator'
}


# 测试类，如扩展其他站点，请在此配置
TESTER_MAP = {
    'weibo': 'WeiboValidTester'
}

# 测试类，如扩展其他站点，请在此配置
TEST_URL_MAP = {
    'weibo': 'https://m.weibo.cn/'
}

# 产生器和验证器循环周期
CYCLE = 120

# 产生器开关，模拟登录添加Cookies
GENERATOR_PROCESS = True
# 验证器开关，循环检测数据库中Cookies是否可用，不可用删除
VALID_PROCESS = False
# API接口服务
API_PROCESS = False
