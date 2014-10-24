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

urlList = ['http://www.duowan.com','http://www.17173.com','http://tieba.baidu.com/']

mailsdb = []
urlDB = []

def crawl(url):
    try:
        req = requests.get(url)
        if req.status_code != 200:
            return 
        file = open('mail.txt', mode='a')
        links = link_re.findall(req.text)
        mails = email_re.findall(req.text)
        if len(mails) > 0:
            mailsdb.extend(mails)
            
        for mail in mailsdb:
            file.write(mail+"\n")
            mailsdb.remove(mail)
        
        for link in links:
            m = re.match(r'^http(.*?)', link)
            if m:
                if link not in urlDB:
                    urlList.append(link)
                    urlDB.append(link)
    except:
        raise ValueError("kao")
    finally:
        file.close()
    return req.content



if __name__ == '__main__':
    countnum = 0
    while len(urlList) >= 1:
       url = urlList.pop()
       crawl(url)
       countnum+=1
       print(url)
       if countnum > 1000:
           break
    
    print(count)
    print(mailsdb)
