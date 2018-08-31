#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
 
from __future__ import with_statement
 
import sys
if sys.version_info < (2, 5):
    sys.exit('Python 2.5 or greater is required.')
 
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
 
import pypidemo
 
 
with open('README.rst') as fp:
    readme = fp.read()
 
with open('LICENSE') as fp:
    license = fp.read()
 
setup(name='pypidemo',
      version=pypidemo.__version__,
      description='这是一个测试库',
      long_description=readme,
      author='Hongtianjun',
      author_email='htj0414@163.com',
      maintainer='Tianjun Hong',
      maintainer_email='htj0414@163.com',
      url='https://github.com/hongtianjun/pypidemo.git',
      packages=['pypidemo'],
      license=license,
      platforms=['any'],
      classifiers=[]
      )