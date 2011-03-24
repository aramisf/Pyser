# -*- coding: utf-8 -*-

class TABLES(object):
    '''Extracts:
       a table from TABLES section;
       text fields from TEXT section;
       other (probably) relevant information from VPORT section.'''

    def __init__(self,filePointer):
        self.TABLES = []
        self.TEXTS = []
        self.VPORTS = []
        self.fields = dict.fromkeys(['TABLES','TEXT','VPORT'],[])
        line = filePointer.readline()

        while line != '':
            line = line.strip()

            while not line in self.fields and line != '':
                line = filePointer.readline().strip()

            if line == 'TEXT':
                self.TEXTS.append(TEXT(filePointer))
        
#            elif line.strip() == 'TABLE':
#                self.TABLES.append(TABLE(filePointer))
# 
#            elif line.strip() == 'VPORT':
#                self.VPORTS.append(VPORT(filePointer))
            line = filePointer.readline()
            

        print "Found ",len(self.TEXTS)," TEXT tags"


#class TABLE(object):
# 
#    ''' TODO: Add description'''
# 
#    def __init__(self,filePointer):
#        # TODO: Check specs
#        #self.tableSymbols = dict.fromkeys(['10','20','1'],'')
#        line = filePointer.readline()
#        print "line: '",line,"'"
# 
#        #if line == '  0\r\n':
# 
#        while line != '  0\r\n':
#            if line.strip() in self.tableSymbols:
#                self.tableSymbols[line.strip()] = filePointer.readline().strip()
#                print "table symbols",self.tableSymbols
# 
#            try:
#                line = filePointer.readline()
#                print "line2: '",line,"'"
# 
#            except StopIteration:
#                filePointer.close()
# 
#        line = filePointer.readline()


class TEXT(object):

    ''' This class receives finds the following data:
    Column: 10
    Line: 20
    Value: 1
    inside a TEXT section of a DXF file. This class should be created only
    when a TEXT section is found in DXF file.'''

    def __init__(self,filePointer):
        self.textSymbols = dict.fromkeys(['10','20','1'],'')
        line = filePointer.readline()

        while line != '  0\r\n':
            line = line.strip()

            if line in self.textSymbols:
                self.textSymbols[line] = filePointer.readline().strip()

            line = filePointer.readline()

  

#class VPORT(object):
#
#    ''' TODO: Add description'''
#
#    def __init__(self,filePointer):
#        # TODO: Check specs
#        #self.vportSymbols = dict.fromkeys(['10','20','1'],'')
#        line = filePointer.readline()
#
#        while line != '  0\r\n':
#            if line.strip() in self.vportSymbols:
#                self.vportSymbols[line.strip()] = filePointer.readline().strip()
#                print self.vportSymbols
#
#            try:
#                line = filePointer.readline()
#
#            except StopIteration:
#                filePointer.close()
#
#        line = filePointer.readline()

