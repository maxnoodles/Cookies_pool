from cookies_pool.db import RedisClient

conn = RedisClient('accounts', 'weibo')

def set(accout, sep='----'):
    username, password = accout.split(sep)
    result = conn.set(username, password)
    print('账号', username, '密码', password)
    print('录入成功' if result else '录入失败')

def scan():
    print('请输入账号密码组，输入exit退出')
    while True:
        accout = input()
        if accout == 'exit':
            break
        set(accout)

if __name__=='__main__':
    scan()