'''
Created on 2014年10月28日

@author: dell
'''

import re

mail_re = re.compile(r'([\w\.,]+@(gmail\.com|qq\.com))')



if __name__ == '__main__':
    mails = re.findall(mail_re, "sss yuanjialong@gmail.com,fdafefasgcvz,fefasdf,sdf@msn.com.asf 234had@qq.com")
    print(mails)