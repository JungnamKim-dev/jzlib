# -*- coding: utf-8 -*-
'''
Created on 2018. 9. 19.
@author: Hyechurn Jang, <hyjang@cisco.com>
'''

from jzlib import Cache

c = Cache(3)
for i in range(0, 5):
    c[str(i)] = i
    print(c)
