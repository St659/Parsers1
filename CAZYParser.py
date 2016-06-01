#-*- coding: utf-8 -*-
from AdvancedHTMLParser import AdvancedHTMLParser
import re
import sys
import unicodedata
from collections import Counter

import codecs



def normaliseData(my_list):
    newlist = list()
    for i in my_list:

        normalised_string =unicodedata.normalize('NFKC', i)
        if len(normalised_string) > 2 and re.search('[a-zA-Z]', normalised_string):
            newlist.append(normalised_string)
    return newlist

def get_highest_strain(data_list, species):
    strain_list = []
    for strain in data_list:
        if species in strain[1]:
            strain_list.append(strain)

    counter = Counter()

    for strain in strain_list:
        counter[strain[1]] +=1

    if len(counter.most_common(1)) > 0:
        most = counter.most_common(1)[0]
    else:
        print("ERROR HERE")
        print(strain_list)

        print("ERROR HERE")
        print(counter)

    highest_strain_enz = []

    for strain in strain_list:
        if re.match(most[0],strain[1]):
            highest_strain_enz.append(strain)


    #print(most[0])
    #print(strain_list)
    #print(highest_strain_enz)
    return highest_strain_enz



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


species_list = list()
for item in tax_list:


    split_string = item[1].split(' ',2)

    if len(split_string) > 1:
        species_string = split_string[0] + " " + split_string[1]
    else:
        species_string = split_string

    if species_string not in species_list:
        species_string = species_string.replace("[", " ")
        species_string = species_string.replace("]", " ")
        species_list.append(species_string)
        #print(species_string)
    #new_file.write("%s\n" % item)



strain_sorted_list = list()
highest_strains =[]

for species in species_list:
    highest_strains.append(get_highest_strain(tax_list, species))

print(len(tax_list))
print(highest_strains)


