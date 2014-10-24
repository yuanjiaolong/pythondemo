'''
Created on 2014年10月23日

@author: dell
'''
# -*- coding: utf-8 -*- 
import requests
import re
from urllib import parse
from itertools import count

email_re = re.compile(r'([\w\.,]+@[\w\.,]+\.\w+)')

link_re = re.compile(r'href="(.*?)"')
http_re = re.compile(r'^http(.*?)')

urlList = ['http://www.sina.com','http://www.sohu.com']

mailsdb = []

def crawl(url):

    req = requests.get(url)
    links = link_re.findall(req.text)
    mails = email_re.findall(req.text)
    if len(mails) > 0:
        mailsdb.extend(mails)
    for link in links:
        m = re.match(r'^http(.*?)', link)
        if m:
            urlList.append(link)
    return req.content



if __name__ == '__main__':
    count = 0
    while len(urlList) >= 1:
       url = urlList.pop()
       content = crawl(url)
       count+=1
       print(url)
       if count > 10:
           break
    
    print(count)
    print(mailsdb)
