# -*- coding: utf-8 -*-
'''
Created on 2017. 9. 27.
@author: HyechurnJang
'''

import jzlib

class Layer1(jzlib.Inventory):
    
    def __init__(self): jzlib.Inventory.__init__(self)
    
    @property
    def get(self): return 'Layer1'
    
    class Layer2A(jzlib.Inventory):
        
        class Layer3A(jzlib.Inventory):
            
            @property
            def get(self): return (~self).get, (-self).get, 'Layer3A'
            
        class Layer3B(jzlib.Inventory):
            
            @property
            def get(self): return (--self).get, (-self).get, 'Layer3B'
        
        @property
        def get(self): return (~self).get, 'Layer2A'
    
    class Layer2B(jzlib.Inventory):
        
        @property
        def get(self): return (-self).get, 'Layer2B'

l1 = Layer1()

print l1.Layer2A.get
print l1.Layer2B.get
print l1.Layer2A.Layer3A.get
print l1.Layer2A.Layer3B.get