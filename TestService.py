'''
Created on 2014年10月27日

@author: dell
'''

import requests
import re
from urllib import parse

def crawl(url):
    req = requests.get(url)
    if req.status_code != 200:
        return 
    print(req.text)




if __name__ == '__main__':
    crawl("http://localhost:8080/smart-reminder-service/app/query?queryText=提醒我晚上8点吃晚饭")