# -*- coding: utf-8 -*-

# This file is the main interface between the user interface and the parser
# itself. Functions here are called by the main program, through user
# interface.

import DXFTableCreator as tabcreator
import DXFSections as dxfsecs

from sys import argv as sys_argv


if len(sys_argv) != 2:
    # TODO: Treat those exceptions in user interface.
    raise Exception
else:
    try:
        f = open(sys_argv[1],'r')
    except:
        exit(1) # This one must also be treated


# Creating lists of ENTITIES:
EntitiesList = dxfdefs.ENTITIES(f)

# Creating a table from TEXT subsection in ENTITIES list:
MyTab = tabcreator.TextTable(EntitiesList.subSections['TEXT'])

# MyTab should be ready for printing =)
# but I'm not gonna test it today.
