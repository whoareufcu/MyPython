# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 11:29:56 2019
@author: 朱小五
微信公众号: 凹凸玩数据
"""

'''
#生成全部的六位数字密码
f = open('passdict.txt','w')
for id in range(1000000):
    password = str(id).zfill(6)+'\n'
    f.write(password)
f.close()
'''
from unrar import rarfile

def extractFile(rf, password):
    try:
        rf.extractall(pwd=bytes(password, "utf8"))
        print("李大伟的压缩包密码是" + password)  # 破解成功
    except:
        pass  # 失败，就跳过


def main():
    rf = rarfile.RarFile(r'C:\Users\whoareu\Desktop\UT12\课件和源码.rar')
    PwdLists = open(r'C:\Users\whoareu\Desktop\UT12\mydict.txt')  # 读入所有密码
    for line in PwdLists.readlines():  # 挨个挨个的写入密码
        Pwd = line.strip('\n')
        guess = extractFile(rf, Pwd)


if __name__ == '__main__':
    main()
