#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules

WorkDir="distorm-%s" % get.srcVERSION()

def setup():
    pisitools.dosed("setup.py", "'-Wall'", "'-Wno-strict-prototypes', '-Wno-missing-braces'")
    shelltools.system("sed -r 's|(CFLAGS	)=|\1+=|g' -i make/linux/Makefile")
    shelltools.system("sed -e '1i#!/usr/bin/env python' -i python/distorm3/sample.py")
    pisitools.dosed("make/linux/Makefile", "usr/local/lib", "%s/usr/lib" % get.installDIR())

def build():
    autotools.make("-C make/linux")
    pythonmodules.compile()

def install():
    pisitools.dodir("/usr/lib")
    autotools.rawInstall("-C make/linux DESTDIR=%s" % get.installDIR())
    pythonmodules.install()
    pisitools.insinto("/usr/share/distorm/", "python/distorm3/sample.py")
    shelltools.chmod(get.installDIR() + "/usr/share/distorm/sample.py", mode=0755)
    pisitools.dosym("/usr/share/distorm/sample.py", "/usr/bin/disasm")
    pisitools.insinto("/usr/include/", "include/*.h")
    pisitools.dodoc("COPYING", "MANIFEST", "README*")
