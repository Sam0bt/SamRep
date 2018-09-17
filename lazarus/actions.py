#!/usr/bin/python

# Created For PisiLinux

from pisi.actionsapi import shelltools, get, pisitools

WorkDir = "."

def install():
    shelltools.system("rpm2targz lazarus-1.8.4-0.x86_64.rpm")
    shelltools.system("tar -zxvf lazarus-1.8.4-0.x86_64.tar.gz")
    pisitools.insinto("/", "etc")
    pisitools.insinto("/","usr")
    pisitools.domove("/usr/lib64/lazarus/", "/usr/lib/")
    pisitools.removeDir("/usr/lib64")
    pisitools.remove("/usr/bin/lazarus-ide")
    pisitools.remove("/usr/bin/lazbuild")
    pisitools.remove("/usr/bin/startlazarus")
    pisitools.dosym("/usr/lib/lazarus/lazarus", "/usr/bin/lazarus-ide")
    pisitools.dosym("/usr/lib/lazarus/lazbuild", "/usr/bin/lazbuild")
    pisitools.dosym("/usr/lib/lazarus/startlazarus", "/usr/bin/startlazarus")
    shelltools.export("$THEPREFIX /usr/lib/fpc/3.0.4/samplecfg", "$THEPREFIX/usr/lib/fpc/3.0.4/ $ETCDIR")