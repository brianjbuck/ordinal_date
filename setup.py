#!/usr/bin/env python
# coding=utf-8

import sys
from setuptools import setup, find_packages

import ordinal_date


requirements = []

python_version = sys.version_info
if python_version.major < 3 or python_version.minor < 4:
    requirements += ["enum34"]


setup(
    name="ordinal_date",
    version=ordinal_date.__version__,
    url="http://github.com/brianjbuck/ordinal_date/",
    license="MIT Software License",
    author="Brian Buck",
    install_requires=requirements,
    author_email="brian@thebuckpasser.com",
    description="Python module to create dates based on the (first, second, third, etc) day of the week in a month",
    packages=find_packages(exclude=["*.tests"]),
    include_package_data=True,
    platforms="any",
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Natural Language :: English",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT Software License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
