# -*- coding: utf-8 -*-
'''
Created on 2018. 9. 20.
@author: Hyechurn Jang, <hyjang@cisco.com>
'''

import os
import sys
import json
import platform
from .struct import Mortal

def setGlobals(**kargs):
    for k, v in kargs.items(): __builtins__[k] = v

def getPlatform():
    os, ver, _ = platform.dist()
    if os: return ('linux', os.lower(), ver)
    os, ver, _, _ = platform.win32_ver()
    if os: return ('windows', os.lower(), ver)
    return ('unknown', 'unknown', 'unknown')

def kill(obj):
    if isinstance(obj, Mortal): obj.__jzlib_mortal_dead__()
    del obj

def loadModule(path):
    directory, name = os.path.split(path)
    name, _ = os.path.splitext(name)
    if directory not in ['', '.'] and directory not in sys.path: sys.path.insert(0, directory)
    __import__(name)

def unloadModule(name):
    if name in sys.modules:
        mod = sys.modules.pop(name)
        for _, obj in mod.__dict__.items(): kill(obj)
        del mod

def dumpJson(obj, indent=None, sort_keys=False):
    def json_default(val): return str(val)
    return json.dumps(obj, default=json_default, indent=indent, sort_keys=sort_keys)