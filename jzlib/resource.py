# -*- coding: utf-8 -*-
'''
Created on 2017. 10. 13.
@author: HyechurnJang
'''

class cache(dict):
    
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
