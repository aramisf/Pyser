# -*- coding: utf-8 -*-

class TABLES(object):
    '''Extracts a table from TABLES section;
        text fields from TEXT section;
        other (probably) relevant information from VPORT section.'''

    self.table = []
    self.fields = dict.fromkeys(['TABLES','TEXT','VPORT'],0)

    def __init__(self,filePoiter):
        line = filePointer.next()

class TABLE(object):

    ''' TODO: Add description'''

    def __init__(self,filePointer):
        # TODO: Check specs
        #self.tableSymbols = dict.fromkeys(['10','20','1'],'')
        line = filePointer.next()

        while line != '  0\r\n':
            if line.strip() in self.tableSymbols:
                self.tableSymbols[line.strip()] = filePointer.next().strip()
                print self.tableSymbols

            try:
                line = filePointer.next()

            except StopIteration:


class TEXT(object):

    ''' This class receives finds the following data:
    Column: 10
    Line: 20
    Value: 10
    inside a TEXT section of a DXF file. This class should be created only
    when a TEXT section is found in DXF file.'''

    def __init__(self,filePointer):
        self.textSymbols = dict.fromkeys(['10','20','1'],'')
        line = filePointer.next()

        while line != '  0\r\n':
            if line.strip() in self.textSymbols:
                self.textSymbols[line.strip()] = filePointer.next().strip()
                print self.textSymbols

            try:
                line = filePointer.next()

            except StopIteration:


  

class VPORT(object):

    ''' TODO: Add description'''

    def __init__(self,filePointer):
        # TODO: Check specs
        #self.vportSymbols = dict.fromkeys(['10','20','1'],'')
        line = filePointer.next()

        while line != '  0\r\n':
            if line.strip() in self.vportSymbols:
                self.vportSymbols[line.strip()] = filePointer.next().strip()
                print self.vportSymbols

            try:
                line = filePointer.next()

            except StopIteration:


