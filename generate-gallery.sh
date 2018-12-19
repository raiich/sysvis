#!/usr/bin/env bash

mkdir -p build/docs build/examples

rm -r build/docs/ build/examples/ \
&& mkdir -p build/docs build/examples \
&& find . -name \*.sysvis | xargs -IX bash -c 'echo X ; sysvis -i X -o build/X'

find . -name \*.r.svg | xargs rm \
&& find build/ -name \*.svg | xargs -IX bash -c 'echo X ; rougher X > X.r.svg'
