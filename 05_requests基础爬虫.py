import random

import requests


def get_headers():
    '''
    随机获取一个headers
    '''
    user_agents = ['Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
                   'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
                   'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11']
    headers = {'User-Agent': random.choice(user_agents)}
    return headers


def get_proxies(ip_list):
    '''随机获取一个proxies'''
    proxies = {"http": random.choice(ip_list)}
    print(proxies)
    return proxies


def readFileLine(path):
    ip_list = []
    with open(path, 'r')as f:
        for l in f.readlines():
            ip_list.append(l.strip())
        return ip_list


# print(get_proxies(readFileLine('D:\mypy1\IO\ip.txt')))
{'https': 'https://223.199.16.42:9999'}


def my_requests():
    cookies = dict(uuid='b18f0e70-8705-470d-bc4b-09a8da617e15',
                   UM_distinctid='15d188be71d50-013c49b12ec14a-3f73035d-100200-15d188be71ffd')
    url = 'https://www.sdzxkj.cn/index.php/Index/xwzx/mid/10/p/1.html'
    rtsp = requests.get(url, headers=get_headers(), proxies=get_proxies(readFileLine('D:\mypy1\IO\ip.txt')))
    rtsp.text
    print(rtsp.status_code)
    # print(rtsp.text)


while True:
    my_requests()
