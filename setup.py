#!/usr/bin/env python

from setuptools import setup


setup(
    setup_requires=['pbr'],
    package_dir={'': '.'},
    py_modules=['mistral_awx_actions'],
    pbr=True,
)
