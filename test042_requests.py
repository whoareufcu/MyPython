# 我们已经讲解了Python内置的urllib模块，用于访问网络资源。但是，它用起来比较麻烦，而且，缺少很多实用的高级功能。
#
# 更好的方案是使用requests。它是一个Python第三方库，处理URL资源特别方便。

# 安装requests
# 如果安装了Anaconda，requests就已经可用了。否则，需要在命令行下通过pip安装：
#
# $ pip install requests

# 使用requests
# 要通过GET访问一个页面，只需要几行代码：
import requests


def request_Baidu():
    r = requests.get('https://www.baidu.com/')
    print(r.status_code, r.reason)
    text = r.text
    print(text)


# request_Baidu()
def sserch_py():
    r = requests.get('http://www.hao6v.com/', params={'q': 'python', 'cat': '1001'})
    print('实际请求的url：', r.url)
    print('编码格式：', r.encoding)
    print('bytes对象：', r.content)
    # print(r.status_code, r.reason)
    # text = r.text
    # print(text)


# sserch_py()
# requests的方便之处还在于，对于特定类型的响应，例如JSON，可以直接获取：
def get_json():
    url1 = 'http://123.131.131.14:81/Platform/NewWeb/ashx/NewWeb.ashx?method=getServerInfoByUser&userId=lsqtest'
    r = requests.get(url1)
    print('json:', r.json())


# get_json()
# 需要传入HTTP Header时，我们传入一个dict作为headers参数：
def request_headers():
    r = requests.get('https://www.douban.com/',
                     headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
    print(r.text)


# request_headers()
# 要发送POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据：
def request_post():
    r = requests.post('https://accounts.douban.com/login',
                      data={'form_email': 'abc@example.com', 'form_password': '123456'})
    print(r.status_code, r.reason)
    print(r.text)


# request_post()


# requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数：
#
# params = {'key': 'value'}
# r = requests.post(url, json=params) # 内部自动序列化为JSON
# 类似的，上传文件需要更复杂的编码格式，但是requests把它简化成files参数：
#
# >>> upload_files = {'file': open('report.xls', 'rb')}
# >>> r = requests.post(url, files=upload_files)
# 在读取文件时，注意务必使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度。
#
# 把post()方法替换为put()，delete()等，就可以以PUT或DELETE方式请求资源。
#
# 除了能轻松获取响应内容外，requests对获取HTTP响应的其他信息也非常简单。例如，获取响应头：
#
# >>> r.headers
# {Content-Type': 'text/html; charset=utf-8', 'Transfer-Encoding': 'chunked', 'Content-Encoding': 'gzip', ...}
# >>> r.headers['Content-Type']
# 'text/html; charset=utf-8'
# requests对Cookie做了特殊处理，使得我们不必解析Cookie就可以轻松获取指定的Cookie：
#
# >>> r.cookies['ts']
# 'example_cookie_12345'
# 要在请求中传入Cookie，只需准备一个dict传入cookies参数：
#
# >>> cs = {'token': '12345', 'status': 'working'}
# >>> r = requests.get(url, cookies=cs)
# 最后，要指定超时，传入以秒为单位的timeout参数：
#
# >>> r = requests.get(url, timeout=2.5) # 2.5秒后超时