# -*- coding: utf-8 -*-
'''
Created on 2017. 10. 19.
@author: HyechurnJang
'''

import os
import sys

class LifeCycleImpl(object):
    
    def __jzlib_lifecycle_release__(self):
        if not hasattr(self, '_jzlib_released'):
            self._jzlib_released = True
            self.__release__()
    
    def __del__(self): self.__jzlib_lifecycle_release__()

class LifeCycle(LifeCycleImpl):
    
    def __release__(self): pass

def kill(obj):
    if isinstance(obj, LifeCycle): obj.__jzlib_lifecycle_release__()
    del obj

def modup(path):
    directory, name = os.path.split(path)
    name, _ = os.path.splitext(name)
    if directory != '' and directory not in sys.path: sys.path.insert(0, directory)
    __import__(name)

def moddown(name):
    if name in sys.modules:
        mod = sys.modules.pop(name)
        for _, obj in mod.__dict__.items(): kill(obj)
        del mod