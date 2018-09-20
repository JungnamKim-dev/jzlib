# -*- coding: utf-8 -*-
'''
Created on 2018. 9. 19.
@author: Hyechurn Jang, <hyjang@cisco.com>
'''

from setuptools import setup

with open("README.md", "r") as fd: long_description = fd.read()
setup(
    name='jzlib',
    version='0.2.1',
    license='Apache 2.0',
    author='Hyechurn Jang',
    author_email='hyjang@cisco.com',
    url='https://github.com/HyechurnJang/jzlib',
    description='Jz code architect library',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['jzlib'],
#     install_requires=[],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)

# python sdist bdist_wheel
# twine upload dist/*