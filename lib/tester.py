# -*- coding: utf-8 -*-

# This program is just a simple interface. The main program should use the
# libs in this directory.

import DXFDefinitions as DXFdefs
from sys import argv as sys_argv

if len(sys_argv) != 2:
    raise Exception
else:
    print "Opening file",sys_argv[1]
    f = open(sys_argv[1])


# Constructing a table:
MyTab = DXFdefs.TABLES(f)

# Trying to print its values:
for i in MyTab.TEXTS:
    print i.textSymbols,"\n"

