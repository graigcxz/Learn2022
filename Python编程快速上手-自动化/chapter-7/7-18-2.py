"""
strip()的正则表达式版本
写一个函数，它接受一个字符串，做的事情和strip()字符串方法一样。
如果只传入了要去除的字符串，没有其他参数，那么就从该字符串首尾去除空白字符。
否则，函数第二个参数指定的字符将从该字符串中去除。
"""

import re

def my_strip(text, strip=''):
    if strip:
        mo1 = re.compile(strip)
        print(mo1.sub('', text))
    else:
        mo2 = re.compile(r'( *)(.*)( *)')
        print(mo2.search(text).group(2))

my_strip('   lskahjdfo ksdhf jsdh  ')
my_strip('sdjf sjdhk  skdh  ', 'sk')
