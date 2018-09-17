#!/usr/bin/python

# Created For PisiLinux

from pisi.actionsapi import shelltools, get, pisitools

WorkDir = "."

def install():
    shelltools.system("rpm2targz fpc-3.0.4-1.x86_64.rpm")
    shelltools.system("tar -zxvf fpc-3.0.4-1.x86_64.tar.gz")
    pisitools.insinto("/", "usr/")
    pisitools.remove("/usr/bin/ppcx64")
    pisitools.dosym("/usr/lib/fpc/3.0.4/ppcx64", "/usr/bin/ppcx64")
    pisitools.domove("/usr/lib64/fpc/", "/usr/lib/")
    pisitools.removeDir("/usr/lib64")
    