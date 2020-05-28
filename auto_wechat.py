####此函数用于测试图灵的机器人是否注册成功，是否可以使用。
import requests
import itchat
import wxpy
import json
import time

# 这个key也是你注册获得的。
from wxpy import Bot

KEY = 'f8fa985f40824103abc6e171ba75633e'


def robot(input):
    apiUrl = 'http://openapi.tuling123.com/openapi/api/v2'
    datas = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": input
            },
            "inputImage": {
                "url": "imageUrl"
            },
            "selfInfo": {
                "location": {
                    "city": "xxx",
                }
            }
        },
        "userInfo": {
            "apiKey": "" + KEY,
            "userId": "1111"  # 这个是你申请到的userid

        }
    }
    datas = json.dumps(datas)
    result = requests.post(apiUrl, data=datas).json()
    result = result.get('results')[0].get('values').get('text')
    return result


# while True:  ####用于测试
#     inputs = input('A:')
#     info = robot(inputs)
#     print(info)


#  一个Bot 对象可被理解为一个 Web 微信客户端。
#  cache_path 提供了缓存的选项,用于将登录信息保存下来，就不用每次都扫二维码
# bot = Bot(cache_path=True)
# 从好友中查找名字叫:林 的人,模糊匹配,可能查出多个人,取出第0个
# father = bot.search('None')[0]


# @bot.register()  # 用于注册消息配置
# def recv_send_msg(recv_msg):
#     print('收到的消息：', recv_msg.text)  # recv_msg.text取得文本
#     # recv_msg.sender 就是谁给我发的消息这个人
#     if recv_msg.sender == father:
#         recv_msg.forward(bot.file_helper, prefix='老爸留言: ')  # 在文件传输助手里留一份，方便自己忙完了回头查看
#         ms = '祝早日康复！'
#         return ms  # 回复
