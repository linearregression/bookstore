#!/usr/bin/env python

# -*- coding: utf-8 -*-

import os
import sys

import re
from itertools import ifilter

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_version():
    '''
    Version slurping without importing bookstore, since dependencies may not be
    met until setup is run.
    '''
    version_regex = re.compile(r"__version__\s+=\s+"
                               r"['\"](\d+.\d+.\d+\w*)['\"]$")
    versions = filter(version_regex.match, open("bookstore/__init__.py"))

    if(len(versions) == 0):
        raise Exception("Bookstore version not set")

    return version_regex.match(versions[-1]).group(1)

version = get_version()

# Utility for publishing the bookstore, courtesy kennethreitz/requests
if sys.argv[-1] == 'publish':
    print("Publishing bookstore {version}".format(version=version))
    os.system('python setup.py sdist upload')
    sys.exit()

packages = ['bookstore']
requires = []

with open('requirements.txt') as reqs:
    requires = reqs.read().splitlines()

setup(name='bookstore',
      # setup.py can't pull from bookstore.__version__ as the dependencies
      # won't be installed yet
      version=version,
      description='IPython notebook storage on OpenStack Swift + Rackspace.',
      long_description=open('README.rst').read(),
      author='Kyle Kelley',
      author_email='rgbkrk@gmail.com',
      url='http://github.com/rgbkrk/bookstore',
      packages=packages,
      package_data={'': ['LICENSE']},
      include_package_data=False,
      install_requires=requires,
      dependency_links=[
          'https://1f2133dc3aab4203faba-815b705eb00655bf9ca363d7dfb3b606.ssl.cf2.rackcdn.com/ipython-1.0.0-rc1.tar.gz',
          #'http://archive.ipython.org/testing/1.0.0/ipython-1.0.0-rc1.tar.gz#egg=ipython-1.0.0-rc1',
          #'http://archive.ipython.org/testing/1.0.0/ipython-1.0.0-rc1.zip#egg=ipython-1.0.0-rc1',
          #'http://pub.fict.io/ipython-1.0.0a1.tar.gz#egg=ipython-1.0.0-rc1',
          #'http://pub.fict.io/ipython-1.0.0a1.zip#egg=ipython-1.0.0-rc1',
      ],
      license=open('LICENSE').read(),
      zip_safe=False,
      classifiers=(
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'Environment :: OpenStack',
          'License :: OSI Approved :: Apache Software License',
          'Natural Language :: English',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: System :: Distributed Computing',
      ),
)
