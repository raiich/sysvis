#!/usr/bin/env python
from setuptools import setup

setup(
    name='sysvis',
    version='0.0.1',
    description='model animation tool',
    license='MIT License',
    packages=[
        'sysvis'
    ],
    install_requires=[
        'docopt',
        'antlr4-python3-runtime'
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': ['sysvis=sysvis.__main__:main']
    },
    setup_requires=['pytest-runner'],
    tests_require=[
        'pytest'
    ],
)
