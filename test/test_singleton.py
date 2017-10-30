# -*- coding: utf-8 -*-
'''
Created on 2017. 10. 30.
@author: HyechurnJang
'''

from jzlib import Singleton

class StTest(Singleton):
    
    def __init__(self, name):
        Singleton.__init__(self)
        self.name = name
    
    def printName(self):
        print self.name

class StWrap(StTest):
    
    def __init__(self):
        StTest.__init__(self, 'test')

StWrap()

_StWrap.printName()

