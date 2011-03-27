# -*- coding: utf-8 -*-

# One class for each Section on DXF files

import DXFSubsections as DXFsubs

#class TEMPLATE(object):
#    ''' Sections Template '''

class ENTITIES(object):
    '''Extracts subsections from ENTITIES section subsection'''

    self.subSections = {}

    def __init__(self,filePointer):
        # Be sure to include your other tags of interest inside this dict:
        self.subSections = dict.fromkeys(['TEXT'],[])
        line = filePointer.readline().strip()

        while line != '':

            while not line in self.subSections and line != 'ENDSEC':
                line = filePointer.readline().strip()

            if line == 'TEXT':
                self.subSections['TEXT'].append(DXFsubs.TEXT(filePointer))

            line = filePointer.readline().strip()


