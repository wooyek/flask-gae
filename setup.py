#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2014 Janusz Skonieczny

import os
import sys
from setuptools import setup, find_packages
from pip.req import parse_requirements
# import pypandoc

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.join(ROOT_DIR, 'src')

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = parse_requirements(os.path.join(ROOT_DIR, "requirements.txt"))
requirements = [str(r.req) for r in requirements]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='flask-gae',
    version='0.1.0',
    description='Commons for Flask running on Google App Engine',
    long_description=readme + '\n\n' + history,
    author='Janusz Skonieczny',
    author_email='js@bravelabs.pl',
    url='https://github.com/wooyek/flask-gae',
    packages=find_packages("src"),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='flask google app engine',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
