#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='AlexTestInstallation',
    version='1.0',
    packages=[
        'Boreas',
    ],
    #find_packages(where='./lib'),
    package_dir={
        "Boreas": "./lib/Boreas",
    },
    py_modules=["bin/testcommand"],
    entry_points={
        'console_scripts': [
            'testcommand=bin.testcommand:main',
        ]
    }
)
