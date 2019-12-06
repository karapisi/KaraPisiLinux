#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS", "%s -Wno-implicit-function-declaration -Wno-implicit-int -Wno-discarded-qualifiers" % get.CFLAGS())
    pisitools.dosed("Makefile.in", "-o root", "")
    pisitools.dosed("nl80211_control.c", "#ifdef HAVE_CONFIG_H", "#include <stdio.h>\n#ifdef HAVE_CONFIG_H")
    autotools.configure("--enable-static=no --libdir=/usr/lib")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())