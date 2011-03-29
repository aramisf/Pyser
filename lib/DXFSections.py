# -*- coding: utf-8 -*-

# One class for each Section on DXF files

import DXFSubSections as DXFsubs

#class TEMPLATE(object):
#    ''' Sections Template '''

class ENTITIES(object):
    '''Extracts subsections from ENTITIES section subsection'''

    def __init__(self,filePointer):
        self.subSections = {}
        self.sectionFound = False
        # Be sure to include your other tags of interest inside this dict:
        self.subSections = dict.fromkeys(['TEXT'],[])
        line = filePointer.readline().strip()

        while line != 'EOF':

            if line == 'ENTITIES':
                self.sectionFound = True

            while not line in self.subSections and self.sectionFound:
                line = filePointer.readline().strip()
                if line == 'ENDSEC':
                    self.sectionFound = False
                if line == 'EOF': break

            if line == 'TEXT' and self.sectionFound:
                self.subSections['TEXT'].append(DXFsubs.TEXT(filePointer))

            line = filePointer.readline().strip()


