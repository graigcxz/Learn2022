"""
强口令检测
写一个函数，它使用正则表达式，确保传入的口令字符串是强口令。
强口令的 定义是:长度不少于 8 个字符，同时包含大写和小写字符，至少有一位数字。
你可能需要用多个正则表达式来测试该字符串，以保证它的强度。
"""

import re

def check(text):
    '''
    :param text: 待检测的字符串
    :return 输出
    '''
    if len(text) < 8:
        return False
    wordRegex = re.compile(r'[a-zA-z]+')
    if wordRegex.findall(text) == []:
        return False
    numRegex = re.compile(r'\d+')
    if numRegex.findall(text) == []:
        return False
    return True

print(check('jafs23SDf'))