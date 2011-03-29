# -*- coding: utf-8 -*-

# A class to create a table, the one that will be obtained by the DXF file.
# The idea is to get a list containing all objects from a Section, and
# create a table containing all elements inside that section. In our
# specific case, ENTITIES section with lots of TEXT subsections inside of it.

from re import sub as rename
# Creates a table from a TEXT subsection
class TextTable(object):

    def __init__(self,subSecList):
        self.columns = []
        self.lines = []
        self.textTable = {}

        for i in range(subSecList.__len__()):

            if not subSecList[i].textSymbols['10'] in self.columns:
                self.columns.append(subSecList[i].textSymbols['10'])

            if not subSecList[i].textSymbols['20'] in self.lines:
                self.lines.append(subSecList[i].textSymbols['20'])

        self.columns.sort()
        self.lines.sort()
        self.createTable()
        self.fillTable(subSecList)


    def createTable(self):
        self.textTable = dict.fromkeys(self.lines,{})

        for i in self.textTable:
            self.textTable[i] = dict.fromkeys(self.columns,' ')


    def fillTable(self,subSecList):

        for i in range(subSecList.__len__()):
            self.textTable[subSecList[i].textSymbols['20']][subSecList[i].textSymbols['10']]=subSecList[i].textSymbols['1']


    def printto(self,fileName):

        if not fileName:
            raise Error("No DXF file name given!")

        f = open(fileName,'r')
        g = open(rename("\.dxf$",".txt",f.name),'w')

        for i in self.lines:
            for j in self.columns:
                g.write(self.textTable[i][j]+'  ')
            g.write('\n')

        g.close()
        f.close()
