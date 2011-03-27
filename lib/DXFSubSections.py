# -*- coding: utf-8 -*-

# One class for each subsection of a section

class TEXT(object):

    ''' Data of interest:
        Column: 10;
        Line: 20;
        Value: 1;
    '''

    self.textSymbols = {}

    def __init__(self,filePointer):
        self.textSymbols = dict.fromkeys(['10','20','1'],'')
        line = filePointer.readline()

        # Must consider windows and linux
        while line != '  0\r\n' and line != '  0\n':
            line = line.strip()

            if line in self.textSymbols:
                self.textSymbols[line] = filePointer.readline().strip()
            line = filePointer.readline()



# For the future:
#class TEMPLATE(object):
#
#    ''' Data of interest:
#        <up to you> 
#    '''
#
#    self.<tag>Symbols = dict.fromkeys([<your tags>],'')
#
#    def __init__(self,filePointer):
#        line = filePointer.readline()
#
#        # Must consider windows and linux, and what tells your interest
#        # subsection ending mark
#        while line != '  0\r\n' and line != '  0\n':
#            line = line.strip()
#
#            if line in self.textSymbols:
#                self.textSymbols[line] = filePointer.readline().strip()
#            line = filePointer.readline()

