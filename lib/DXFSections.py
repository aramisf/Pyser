# -*- coding: utf-8 -*-

# One class for each Section on DXF files

import DXFSubSections as DXFsubs

#class TEMPLATE(object):
#    ''' Sections Template '''

class ENTITIES(object):
    '''Extracts subsections from ENTITIES section subsection'''

    def __init__(self,filePointer):
        self.subSections = {}

        # Be sure to include your other tags of interest inside this dict:
        self.subSections = dict.fromkeys(['TEXT'],[])
        line = filePointer.readline().strip()

        while line != '' and line != 'EOF':

            while not line in self.subSections and line != 'ENDSEC':
                line = filePointer.readline().strip()
                if line == 'EOF': break

            if line == 'TEXT':
                self.subSections['TEXT'].append(DXFsubs.TEXT(filePointer))

            line = filePointer.readline().strip()


