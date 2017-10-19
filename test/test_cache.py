# -*- coding: utf-8 -*-
'''
Created on 2017. 10. 13.
@author: HyechurnJang
'''

from jzlib import cache

c = cache(3)

for i in range(0, 5):
    c[str(i)] = i
    print c


