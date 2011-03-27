# -*- coding: utf-8 -*-

# A class to create a table, the one that will be obtained by the DXF file.
# The idea is to get a list containing all objects from a Section, and
# create a table containing all elements inside that section. In our
# specific case, ENTITIES section with lots of TEXT subsections inside of it.

# Creates a table from a TEXT subsection
class TextTable(object):
    self.columns = []
    self.lines = []
    self.textTable = {}

    def __init__(self,subSecList):

        for i in range(subSecList.__len__()):

            if not subSecList[i].symbols['10'] in self.columns:
                self.columns.append(subSecList[i].symbols['10'])

            if not subSecList[i].symbols['20'] in self.lines:
                self.lines.append(subSecList[i].symbols['20'])

        self.columns.sort()
        self.lines.sort()
        self.createTable()
        self.fillTable(subSecList)


    def createTable(self):
        self.textTable = dict.fromkeys(self.lines,{})

        for i in self.textTable:
            self.textTable[i] = dict.fromkeys(self.columns,' ')


    def fillTable(self,subSectList):

        for i in range(subSecList.__len__()):
            self.textTable[subSecList[i].textSymbols['20']][subSecList[i].textSymbols['10']]=subSecList[i].textSymbols['1']


    #def printto(self):

        # TODO: Print the final table to files and to stdout
