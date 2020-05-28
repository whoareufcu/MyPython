import random
import re
from html.parser import HTMLParser

import requests


class MyHTMLParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.__sgin = ''
        self.__ip = ''
        self.__port = ''
        self.mydict = {}

    def handle_starttag(self, tag, attrs):
        # print('<%s>' % tag)
        if tag == 'td':
            self.__sgin = 'mysgin'


    def handle_endtag(self, tag):
        if tag == 'td':
            self.__sgin = ''

    def handle_startendtag(self, tag, attrs):
        # print('<%s/>' % tag)
        if tag == 'td':
            self.__sgin = ''


    def handle_data(self, data):
        # print('data:--', data)
        if self.__sgin == "mysgin":
            if re.match(r'^\d+\.\d+\.\d+\.\d+$', data):
                self.__ip = str(data)
            elif re.match(r'\d{4,5}', data):
                self.__port = str(data)
            self.mydict[self.__ip] = self.__port

    def handle_comment(self, data):
        # print('<!--', data, '-->')
        pass

    def handle_entityref(self, name):
        # print('&%s;' % name)
        pass

    def handle_charref(self, name):
        # print('&#%s;' % name)
        pass


# 从文件获取
def readFile():
    with open(r'D:\mypy1\IO\test.txt', 'r') as f:
        return f.read()


def get_headers():
    '''
    随机获取一个headers
    '''
    user_agents = ['Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
                   'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
                   'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11']
    headers = {'User-Agent': random.choice(user_agents)}
    return headers


def get_fromInternet():
    rtsp = requests.get('https://www.xicidaili.com/nn/', headers=get_headers())
    print(rtsp.text)
    return rtsp.text


def writeFile(content):
    with open(r'D:\mypy1\IO\ip.txt', 'a') as f:
        f.writelines(content + '\r')


def pre_compile(string):
    prec = re.compile(r'^\s*\<td>([0-9\.]+)\</td>$')
    print(prec.match(string).groups())
    if prec.match(string):
        return prec.groups()
    else:
        return '匹配失败！'


paser = MyHTMLParser()
# paser.feed(readFile())
paser.feed(get_fromInternet())
for k, v in paser.mydict.items():
    print('http://%s:%s' % (k, v))
    writeFile('http://%s:%s' % (k, v))
# print(paser.mydict)
