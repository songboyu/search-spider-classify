#coding=utf-8
import re
import urllib
import codecs
import json

import requests
from bs4 import BeautifulSoup

# import socks
# import socket
# socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 1080)
# socket.socket = socks.socksocket

def find_items(html):
    '''通过获得的网页源代码匹配每个条目内容

    @param keyq:        网页源代码
    @type  keyq:        String

    @return:            获取到的条目的集合
    @rtype:             list

    '''
    soup = BeautifulSoup(html)
    tds = soup.select('h3.r')
    items = []
    for td in tds:
        item = {
            'url':  urllib.unquote(re.findall(r'q=(.*?)&', td.select('a')[0]['href'])[0]),
            'name': td.select('a')[0].text
        }
        print item
        items.append(item)

    return items

def google_search(wd):
    url = 'http://www.google.com.hk/search'
    p = {
        'q':wd,
        'num':50,
        'ie':'utf-8',
    }
    r = requests.get(url, params=p)
    print r.url
    return r.content

if __name__ == '__main__':
    html = google_search('速度与激情')
    items = find_items(html)
    f = codecs.open('data/google_items.json', 'wb', encoding='utf-8')
    for item in items:
	    line = json.dumps(item) + "\n"
	    f.write(line.decode('unicode_escape'))
    f.close()