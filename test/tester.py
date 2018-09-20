# -*- coding: utf-8 -*-
'''
Created on 2018. 9. 20.
@author: Hyechurn Jang, <hyjang@cisco.com>
'''

import sys
from jzlib import *

print('Result like as...')
print('''
Hyechurn Jang jzlib
('windows', '10', '10.0.17134')
imported by sample_file.py
imported by sample_package
single tone StWrap
('Layer1', 'Layer2A')
('Layer1', 'Layer2B')
('Layer1', ('Layer1', 'Layer2A'), 'Layer3A')
('Layer1', ('Layer1', 'Layer2A'), 'Layer3B')
Test
A
A_B
{'0': 0}
{'0': 0, '1': 1}
{'0': 0, '1': 1, '2': 2}
{'1': 1, '2': 2, '3': 3}
{'2': 2, '3': 3, '4': 4}
''')
print('Test Start ###################')
print()

setGlobals(my_name='Hyechurn Jang', this_is='jzlib')
print(my_name, this_is)

print(getPlatform())

loadModule('./tester_resource/sample_file.py')
import sample_file
sample_file.sample()
loadModule('./tester_resource/sample_package')
import sample_package
sample_package.sample()

class StTest(Singleton):
    def __init__(self, name):
        Singleton.__init__(self)
        self.name = name
    def printName(self):
        print('single tone', self.name)
class StWrap(StTest):
    def __init__(self):
        StTest.__init__(self, 'StWrap')
StWrap()
STWRAP.printName()

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

class Env(Environment):
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
Env()
print(ENV.get)
print(ENV.A.get)
print('%s_%s' % (ENV.A, ENV.A.B))

c = Cache(3)
for i in range(0, 5):
    c[str(i)] = i
    print(c)
