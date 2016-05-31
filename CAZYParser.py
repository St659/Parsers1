from AdvancedHTMLParser import AdvancedHTMLParser
import re

parser = AdvancedHTMLParser()

parser.parseFile('Parsers1/cazyhtml1.txt')
protein_list = list()
tax_list = list()

new_file = open('ParsedResults.txt', 'w')

#print(parser.getHTML())

linktag_list = parser.getElementsByTagName('a')

row_list = parser.getElementsByTagName('tr')




proteinID = re.compile(r"\w{3}\d{5}.\d{1}")

regex = re.compile(r'\>(.*?)\<')



for row in row_list:
    if re.search("separateur2", row.innerHTML.strip()):

        current_row = re.findall(regex,row.innerHTML.strip())

        truncated_row = [ i for i in current_row if len(i) > 2]

        tax_list.append(truncated_row)




for item in tax_list:
    for dif_row in new_list:
        if dif_row[0] == item[0] and dif_row[1] == item[1]:

    new_file.write("%s\n" % item)

