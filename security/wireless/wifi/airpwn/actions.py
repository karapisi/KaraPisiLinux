#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.system("sed -i 's/python2.4/python2.7/g' conf.h")
    shelltools.system("sed -i 's/python2.4/python2.7/g' configure.ac")
    autotools.autoreconf("-ivf")
    autotools.configure("CFLAGS=-Wno-unused-result CPPFLAGS=-Ilorcon/usr/include LDFLAGS=-Llorcon/usr/lib LIBS=-lcrypto --libdir=/usr/lib")
    pisitools.dosed("Makefile", "LDFLAGS =", "LDFLAGS = -Wl,-O1,--as-needed ")
    
def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dosbin("airpwn")
    pisitools.dosbin("wep_keygen")
    pisitools.dosbin("ma*.sh")
    shelltools.copytree("conf/", "%s/usr/share/airpwn/conf/" % get.installDIR())
    shelltools.copytree("content/", "%s/usr/share/airpwn/" % get.installDIR())
    shelltools.copytree("pyscripts/", "%s/usr/share/airpwn/" % get.installDIR())
