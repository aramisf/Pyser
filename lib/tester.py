# -*- coding: utf-8 -*-

# This program is just a simple interface. The main program should use the
# libs in this directory.

import DXFDefinitions as DXFdefs
from sys import argv as sys_argv

if len(sys_argv) != 2:
    raise Exception
else:
    print "Abrindo arquivo",sys_argv[1]
    f = open(sys_argv[1])


DXFdefs.TABLES(f)
