# -*- coding: utf-8 -*-
'''
Created on 2018. 9. 19.
@author: Hyechurn Jang, <hyjang@cisco.com>
'''

from jzlib import Singleton

class StTest(Singleton):
    
    def __init__(self, name):
        Singleton.__init__(self)
        self.name = name
    
    def printName(self):
        print(self.name)

class StWrap(StTest):
    
    def __init__(self):
        StTest.__init__(self, 'test')

StWrap()

_StWrap.printName()
