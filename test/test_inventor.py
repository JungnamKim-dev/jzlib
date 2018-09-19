# -*- coding: utf-8 -*-
'''
Created on 2018. 9. 19.
@author: Hyechurn Jang, <hyjang@cisco.com>
'''

from jzlib import Inventory

class Layer1(Inventory):
    
    def __init__(self): Inventory.__init__(self)
    
    @property
    def get(self): return 'Layer1'
    
    class Layer2A(Inventory):
        
        class Layer3A(Inventory):
            
            @property
            def get(self): return (~self).get, (-self).get, 'Layer3A'
            
        class Layer3B(Inventory):
            
            @property
            def get(self): return (--self).get, (-self).get, 'Layer3B'
        
        @property
        def get(self): return (~self).get, 'Layer2A'
    
    class Layer2B(Inventory):
        
        @property
        def get(self): return (-self).get, 'Layer2B'
        
class LayerWrap(Layer1):
    
    def __init__(self):
        Layer1.__init__(self)

l1 = LayerWrap()

print(l1.Layer2A.get)
print(l1.Layer2B.get)
print(l1.Layer2A.Layer3A.get)
print(l1.Layer2A.Layer3B.get)