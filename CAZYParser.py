#-*- coding: utf-8 -*-
from AdvancedHTMLParser import AdvancedHTMLParser
import re
import sys
import unicodedata
import codecs



def normaliseData(my_list):
    newlist = list()
    for i in my_list:

        normalised_string =unicodedata.normalize('NFKC', i)
        if len(normalised_string) > 2:
            newlist.append(normalised_string)
    return newlist


print (sys.stdout.encoding)

parser = AdvancedHTMLParser()

parser.parseFile('Parsers1/cazyhtml1.txt')
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


species_list = list()
for item in tax_list:

    split_string = item[1].split(' ',2)
    print(len(split_string))
    if len(split_string) > 1:
        species = str.join(split_string[0], split_string[1])
    else:
        species = split_string
    species_list.append(species)
    new_file.write("%s\n" % item)

print(species_list)