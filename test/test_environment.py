# -*- coding: utf-8 -*-
'''
Created on 2018. 9. 19.
@author: Hyechurn Jang, <hyjang@cisco.com>
'''

from jzlib import Environment, Inventory

class Test(Environment):
    
    @property
    def get(self): return 'Test'
    def __repr__(self): return 'Test'
    
    class A(Inventory):
        
        @property
        def get(self): return 'A'
        def __repr__(self): return 'A'
        
        class B(Inventory):
            @property
            def get(self): return 'B'
            def __repr__(self): return 'B'

Test()

print(_Test.get)
print(_Test.A.get)
print('%s_%s' % (_Test.A, _Test.A.B))
