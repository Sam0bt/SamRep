#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import get, pisitools, shelltools

def install():
    pisitools.insinto("/usr/share/rvgl", "./*")
    pisitools.dosym("/usr/share/rvgl/rvgl.64", "/usr/bin/rvgl")
    pisitools.dosym("/usr/lib/libfluidsynth.so", "/usr/lib/libfluidsynth.so.1")

