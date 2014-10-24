'''
Created on 2014年10月23日

@author: dell
'''


class Student(object):
    '''
    classdocs
    '''


    def __init__(self, name):
        '''
        Constructor
        '''
        self.name=name
    def sayHello(self):
         print("Hello " + self.name)