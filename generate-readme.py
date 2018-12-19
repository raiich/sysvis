#!/usr/bin/env python

import os


def func():
    with open('README.ja.template.md') as f:
        md = f.read()
    filling = {fn.split('.')[0]: content('./docs/' + fn) for fn in os.listdir('docs')}
    with open('README.ja.md', 'w') as f:
        f.write(md.format(**filling))


class Sysvis:
    def __init__(self, content):
        self.sysvis = content


def content(filename):
    with open(filename) as f:
        return Sysvis(f.read())


func()
