"""
小米步数接口

Version: 0.1
Author: Taichi
"""
import requests

def html_post(url, phone, password, num):
    data = requests.post(url=url,params={
        'phone': phone,
        'pwd': password,
        'num': num,
    })
    print(data.json())

if __name__ == '__main__':
    # 刷步数 API
    url = 'https://motion.faithxy.com/motion/api/motion/Xiaomi'
    # 账号
    phone = '小米账号'
    # 密码
    password = '小米密码'
    # 步数
    size = '23000'
    # 调用函数
    html_post(url=url, phone=phone, password=password, num=size)
