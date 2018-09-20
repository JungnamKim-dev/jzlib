# -*- coding: utf-8 -*-
'''
Created on 2018. 9. 20.
@author: Hyechurn Jang, <hyjang@cisco.com>
'''

from inspect import isclass, getmro

class Mortal(object):
    
    def __dead__(self):
        ### distruction logic here ###
        pass
    
    #===========================================================================
    # internal logic
    #===========================================================================
    def __jzlib_mortal_dead__(self):
        if not hasattr(self, '_jzlib_mortal_dead'):
            self._jzlib_mortal_dead = True
            self.__dead__()
    
    def __del__(self): self.__jzlib_mortal_dead__()

class Singleton(object):
    
    def __init__(self):
        __builtins__[self.__class__.__name__.upper()] = self

class Inventory(object):
    
    def __init__(self, root=None, parent=None):
        if root != None: self._jzlib_inv_root = root
        else: self._jzlib_inv_root = self
        if parent != None: self._jzlib_inv_parent = parent
        else: self._jzlib_inv_parent = self
        self._jzlib_inv_children = {}
        for mro in reversed(getmro(self.__class__)):
            if mro == object or mro == Inventory: continue
            elems = mro.__dict__
            for name, cls in elems.items():
                if isclass(cls) and issubclass(cls, Inventory):
                    inst = cls()
                    Inventory.__init__(inst, self._jzlib_inv_root, self)
                    self.__setattr__(name, inst)
                    self._jzlib_inv_children[name] = inst
    
    def __invert__(self): return self._jzlib_inv_root
    def __neg__(self): return self._jzlib_inv_parent
    def __pos__(self): return self._jzlib_inv_children

class Environment(Singleton, Inventory):
    
    def __init__(self):
        Singleton.__init__(self)
        Inventory.__init__(self)

class Cache(dict):
    
    def __init__(self, max=100):
        dict.__init__(self)
        self._jzlib_cache_max = max
        self._jzlib_cache_hit = []
        
    def __setitem__(self, key, val):
        if len(self._jzlib_cache_hit) < self._jzlib_cache_max:
            if key not in self._jzlib_cache_hit:
                self._jzlib_cache_hit.append(key)
            else:
                self._jzlib_cache_hit.remove(key)
                self._jzlib_cache_hit.append(key)
        else:
            cache = self._jzlib_cache_hit.pop(0)
            dict.pop(self, cache)
            self._jzlib_cache_hit.append(key)
        return dict.__setitem__(self, key, val)
    
    def __getitem__(self, key):
        if key in self._jzlib_cache_hit:
            self._jzlib_cache_hit.remove(key)
            self._jzlib_cache_hit.append(key)
            return dict.__getitem__(self, key)
        else:
            return None
    
    def pop(self, key):
        if key in self._jzlib_cache_hit:
            self._jzlib_cache_hit.remove(key)
            return dict.pop(self, key)
        else: return None
    
    def remove(self, key): return self.pop(key)
