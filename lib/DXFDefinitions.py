# -*- coding: utf-8 -*-

class ENTITIES(object):
    '''Extracts a table from ENTITIES section contained in text fields on TEXT
    subsection;'''

    # Check this out and you'll be able to improve the code, if you need to
    # use it for other purposes. At this moment, I'm interested into parse only
    # text fields, contained into tables drawn on AutoCAD.
    def __init__(self,filePointer):
        # You should check http://o.mk/2b4f for DXF specifications, or search
        # for it over the internet. In my case, this structures will do the
        # job.
        self.sections = ['ENTITIES'] # ,'TABLES','BLOCKS']
        self.subSections = ['TEXT']
        self.sectionFound = False
        self.TEXTS = []
        line = filePointer.readline().strip()

        while line != '':

            while not line in self.sections and line != '':
                line = filePointer.readline().strip()
            self.sectionFound = True

            while self.sectionFound and line != '':
                line = filePointer.readline().strip()

                while not line in self.subSections and line != '':
                    line = filePointer.readline().strip()

                if line == 'TEXT':
                    self.TEXTS.append(TEXT(filePointer))

                if line == 'ENDSEC':
                    self.sectionFound = False
            line = filePointer.readline().strip()

    def sortcolumns(self):
        self.columns = []

        for i in range(self.TEXTS.__len__()):

            if not self.TEXTS[i].textSymbols['10'] in self.columns:
                self.columns.append(self.TEXTS[i].textSymbols['10'])

        return self.columns.sort()


    def printto(self):
        currentLine = self.TEXTS[0].textSymbols['20']
        columnsList = self.sortcolumns()

        if i == 0 and self.TEXTS[i].textSymbols['10'] < currentColumn:
            print "\t"

        for i in range(self.TEXTS.__len__()):

            if self.TEXTS[i].textSymbols['20'] == currentLine:
                print "%s  " % (self.TEXTS[i].textSymbols['1']),

            else:
                currentLine = self.TEXTS[i].textSymbols['20']
                print "\n"



class TEXT(object):

    ''' This class finds the following data:
    Column: 10;
    Line: 20;
    Value: 1;
    inside a TEXT subsection of a DXF file. This class should be created only
    when a TEXT subsection is found in a DXF file.'''

    def __init__(self,filePointer):
        self.textSymbols = dict.fromkeys(['10','20','1'],'')
        line = filePointer.readline()

        while line != '  0\r\n':
            line = line.strip()

            if line in self.textSymbols:
                self.textSymbols[line] = filePointer.readline().strip()
            line = filePointer.readline()


#class TABLE(object):
# 
#    '''<description here>'''
# 
#    def __init__(self,filePointer):
#        self.tableSymbols = dict.fromkeys(['key1','key2','key3'],'')
#        line = filePointer.readline()
#        print "line: '",line,"'"
# 
#        while line != '  0\r\n':
# 
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
#        line = filePointer.readline()

