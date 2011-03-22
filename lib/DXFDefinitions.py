# -*- coding: utf-8 -*-

class TABLES(object):
    '''Extracts:
       a table from TABLES section;
       text fields from TEXT section;
       other (probably) relevant information from VPORT section.'''

    def __init__(self,filePointer):
        self.tables = []
        self.texts = []
        self.vports = []
        self.fields = dict.fromkeys(['TABLES','TEXT','VPORT'],[])
        line = filePointer.next()

        while line != 'EOF':
            line = line.strip()

            while not line in self.fields:
                try:
                    line = filePointer.next()
     
                except StopIteration:
                    filePointer.close()

            if line.strip() == 'TEXT':
                self.texts.append(TEXT(filePointer))
        
#            elif line.strip() == 'TABLE':
#                self.tables.append(TABLE(filePointer))
# 
#            elif line.strip() == 'VPORT':
#                self.vports.append(VPORT(filePointer))

            # At the end of processing, append the list to the dict.
            self.fields[line] = filePointer.next().strip()

            line = filePointer.next()



#class TABLE(object):
# 
#    ''' TODO: Add description'''
# 
#    def __init__(self,filePointer):
#        # TODO: Check specs
#        #self.tableSymbols = dict.fromkeys(['10','20','1'],'')
#        line = filePointer.next()
#        print "line: '",line,"'"
# 
#        #if line == '  0\r\n':
# 
#        while line != '  0\r\n':
#            if line.strip() in self.tableSymbols:
#                self.tableSymbols[line.strip()] = filePointer.next().strip()
#                print "table symbols",self.tableSymbols
# 
#            try:
#                line = filePointer.next()
#                print "line2: '",line,"'"
# 
#            except StopIteration:
#                filePointer.close()
# 
#        line = filePointer.next()


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
        print "line: '",line,"'"

        while line != '  0\r\n':
            line = line.strip()

            if line in self.textSymbols:
                self.textSymbols[line] = filePointer.next().strip()
                print "table symbols",self.tableSymbols

            try:
                line = filePointer.next()
                print "line2: '",line,"'"

            except StopIteration:
                filePointer.close()

        line = filePointer.next()

  

#class VPORT(object):
#
#    ''' TODO: Add description'''
#
#    def __init__(self,filePointer):
#        # TODO: Check specs
#        #self.vportSymbols = dict.fromkeys(['10','20','1'],'')
#        line = filePointer.next()
#
#        while line != '  0\r\n':
#            if line.strip() in self.vportSymbols:
#                self.vportSymbols[line.strip()] = filePointer.next().strip()
#                print self.vportSymbols
#
#            try:
#                line = filePointer.next()
#
#            except StopIteration:
#                filePointer.close()
#
#        line = filePointer.next()

