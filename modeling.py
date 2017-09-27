# -*- coding: utf-8 -*-
'''
Created on 2017. 9. 27.
@author: HyechurnJang
'''

import types

class Inventory(object):
    
    def __init__(self, root=None, parent=None):
        if root: self._inventory_root = root
        else: self._inventory_root = self
        if parent: self._inventory_parent = parent
        else: self._inventory_parent = self
        self._inventory_children = {}
        elems = self.__class__.__dict__
        for name, cls in elems.items():
            if type(cls) in [types.TypeType, types.ClassType] and issubclass(cls, Inventory):
                inst = cls()
                Inventory.__init__(inst, self._inventory_root, self)
                self.__setattr__(name, inst)
                self._inventory_children[name] = inst
    
    def __invert__(self): return self._inventory_root
    def __neg__(self): return self._inventory_parent
    def __pos__(self): return self._inventory_children
