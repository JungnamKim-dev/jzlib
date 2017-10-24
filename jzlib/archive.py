# -*- coding: utf-8 -*-
'''
Created on 2017. 9. 27.
@author: HyechurnJang
'''

import types

class Inventory(object):
    
    def __init__(self, root=None, parent=None):
        if root != None: self._inventory_root = root
        else: self._inventory_root = self
        if parent != None: self._inventory_parent = parent
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

class Cache(dict):
    
    def __init__(self, max=100):
        dict.__init__(self)
        self.max = max
        self.hit = []
        
    def __setitem__(self, key, val):
        if len(self.hit) < self.max:
            if key not in self.hit:
                self.hit.append(key)
            else:
                self.hit.remove(key)
                self.hit.append(key)
        else:
            cache = self.hit.pop(0)
            dict.pop(self, cache)
            self.hit.append(key)
        return dict.__setitem__(self, key, val)
    
    def __getitem__(self, key):
        if key in self.hit:
            self.hit.remove(key)
            self.hit.append(key)
            return dict.__getitem__(self, key)
        else:
            return None
    
    def pop(self, key):
        if key in self.hit:
            self.hit.remove(key)
            return dict.pop(self, key)
        else: return None
    
    def remove(self, key): return self.pop(key)