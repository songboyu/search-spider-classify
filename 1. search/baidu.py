#coding=utf-8
import re
import codecs
import json

import requests
from bs4 import BeautifulSoup

def find_items(html):
    '''通过获得的网页源代码匹配每个条目内容

    @param keyq:        网页源代码
    @type  keyq:        String

    @return:            获取到的条目的集合
    @rtype:             list

    '''
    soup = BeautifulSoup(html)
    tds = soup.select('td.f')
    items = []
    for td in tds:
        item = {
	        'url':   td.select('a')[0]['href'],
	        'title': td.select('a')[0].text,
	        'intro': td.select('font[size=-1]')[-1].text,
	        'time':  re.findall(r'\d+-\d+-\d+', td.select('font[color=#008000]')[0].text)[0]
        }
        items.append(item)

    return items

def baidu_search(wd):
    url = 'http://www.baidu.com/s'
    p = {
        'wd':wd,
        'rn':50,
        'ie':'utf-8',
        'tn':'baidulocal'
    }
    r = requests.get(url, params=p)
    print r.url
    return r.content

if __name__ == '__main__':
    html = baidu_search('速度与激情')
    items = find_items(html)
    f = codecs.open('data/baidu_items.json', 'wb', encoding='utf-8')
    for item in items:
	    line = json.dumps(item) + "\n"
	    f.write(line.decode('unicode_escape'))
    f.close()