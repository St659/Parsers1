#-*- coding: utf-8 -*-
from AdvancedHTMLParser import AdvancedHTMLParser
import re
import sys
import unicodedata
import codecs

class myClass:
    data = []
    def __init__(self, data):
        self.data = data

def normaliseData(my_list):
    newlist = list()
    for i in my_list:
        newlist.append(unicodedata.normalize('NFKC', i))
    return newlist


print (sys.stdout.encoding)

parser = AdvancedHTMLParser()

parser.parseFile('cazyhtml1.txt')
protein_list = list()
tax_list = list()
truncated_row = list()

new_file = open('ParsedResults.txt', 'w')

#print(parser.getHTML())

linktag_list = parser.getElementsByTagName('a')

row_list = parser.getElementsByTagName('tr')




proteinID = re.compile(r"\w{3}\d{5}.\d{1}")

regex = re.compile(r'\>(.*?)\<')



for row in row_list:
    if re.search("separateur2", row.innerHTML.strip()):

        current_row = re.findall(regex,row.innerHTML.strip())

        tax_list.append(normaliseData(current_row))





        #print(tax_list)

print(tax_list)

#for item in tax_list:
    #new_file.write("%s\n" % item)

