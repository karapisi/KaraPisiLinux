#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#def setup():
#    shelltools.system("rm %s/mock-3.0.5/mock/tests/testhelpers_py3.py" % get.workDIR())

def build():
    pythonmodules.compile(pyVer="3")
    
    #pythonmodules.run("setup.py build_sphinx", pyVer="3")
    
#def check():
    #pythonmodules.compile("test", pyVer="3")
    #pythonmodules.run("-m unittest discover", pyVer="3")

def install():
    pythonmodules.install(pyVer="3")