#-*- coding: utf-8 -*-
from AdvancedHTMLParser import AdvancedHTMLParser
from Bio import Entrez,SeqIO
import re
import sys
import unicodedata
from collections import Counter
import urllib.request
import unittest
import itertools

import codecs


class ParserTests(unittest.TestCase):

    def test_url_split(self):
        url_string = "http://www.cazy.org/GH33_bacteria.html,http://www.cazy.org/GH33_bacteria.html?debut_PRINC=1000#pagination_PRINC"
        self.assertEqual(len(split_url(url_string)), 2)

    def test_search_name(self):
        test_tax_list = [[' neuraminidase', 'Acidobacteria bacterium DSM 100886', 'AMY11745.1'], [' neuraminidase', 'Acidobacteria bacterium DSM 100886', 'AMY11757.1'], [' ABSDF1049 (fragment)', 'Acinetobacter baumannii', 'CAP00401.1'], [' ABSDF0702 (fragment)', 'Acinetobacter baumannii', 'CAP00078.1'], [' BJAB0715_02370', 'Acinetobacter baumannii BJAB0715', 'AGQ07016.1'], [' IOMTU433_1027', 'Acinetobacter baumannii IOMTU 433', 'BAP65815.1'], [' ABZJ_02864', 'Acinetobacter baumannii MDR-ZJ06', 'AEP07324.1'], [' ABTW07_1207', 'Acinetobacter baumannii TCDC-AB0715', 'ADX91636.1', 'ADX92148.1'], [' ABTW07_3055', 'Acinetobacter baumannii TCDC-AB0715', 'ADX93478.1'], [' AZE33_12470', 'Acinetobacter baumannii XH858', 'AMN01984.1'], [' Asuc_1960', 'Actinobacillus succinogenes 130Z', 'ABR75307.1', 'A6VQR0']]
        self.assertEqual(len(search_name(test_tax_list,'Acidobacteria bacterium')), 2)


def search_name(tax_list, name):
    search_result_list = []
    for tax in tax_list:
        for string in tax:
            if re.match(name, str(string)):
                search_result_list.append(tax)
    return search_result_list

def split_url(urlString):
    return urlString.split(",")


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
        print(strain_list)

    highest_strain_enz = []

    for strain in strain_list:
        if re.match(most[0],strain[1]):
            highest_strain_enz.append(strain)

    return highest_strain_enz


def get_fasta(urlInput, resultsFile, search_string, reduce):
    parser = AdvancedHTMLParser()

    urls = split_url(urlInput)
    print(urls)
    nested_species_list = []
    nested_tax_list = []
    for url in urls:
        with urllib.request.urlopen(url) as response:
            html = response.read()

        parser.parseStr(html)
        row_list = parser.getElementsByTagName('tr')

        tax= get_tax_list(row_list)

        nested_species_list.append(get_species_list(tax))
        nested_tax_list.append(tax)


    species_list = list(itertools.chain.from_iterable(nested_species_list))
    tax_list = list(itertools.chain.from_iterable(nested_tax_list))
    highest_strains = []

    if search_string:
        highest_strains.append(search_name(tax_list, search_string))
    elif reduce == 1:
        for species in species_list:
            highest_strains.append(get_highest_strain(tax_list, species))
    else:
        highest_strains = tax_list

    accessions = []
    for strain in highest_strains:
        print(strain)
        if len(strain) >0:
            for enzyme in strain:
                accessions.append(enzyme[2])
    print(len(accessions))
    #entrez_get_fasta(accessions, resultsFile)
    del accessions[:]
    del tax_list[:]
    del species_list [:]
    del highest_strains[:]
    del nested_species_list[:]
    del nested_tax_list[:]


def get_tax_list(html_row_list):

    tax_list = list()

    regex = re.compile(r'\>(.*?)\<')

    for row in html_row_list:
        if re.search("separateur2", row.innerHTML.strip()):
            current_row = re.findall(regex, row.innerHTML.strip())
            tax_list.append(normaliseData(current_row))
    return tax_list

def get_species_list(tax_list):
    species_list = list()
    for item in tax_list:

        split_string = item[1].split(' ', 2)

        if len(split_string) > 1:
            species_string = split_string[0] + " " + split_string[1]
        else:
            species_string = split_string

        if species_string not in species_list:
            species_string = species_string.replace("[", " ")
            species_string = species_string.replace("]", " ")
            species_list.append(species_string)
    return species_list


def entrez_get_fasta(accessions, resultsFile):
    accession = " ".join(accessions)
    Entrez.email = "st659@york.ac.uk"
    print(accession)
    handle = Entrez.esearch(db="protein", term=accession, retmode="xml", usehistory='y')
    results = Entrez.read(handle)
    idList = results["IdList"]

    webEnv = results["WebEnv"]
    queryKey = results["QueryKey"]

    batch_size = 100
    resultsList = []
    for start in range(0, len(accessions), batch_size):
        resultsList.append(
            Entrez.efetch(db="protein", rettype="fasta", retstart=start, retmax=batch_size, webenv=webEnv,
                          query_key=queryKey))

    fasta = 0
    resultsFile = open(resultsFile, 'w')
    for result in resultsList:
        resultsFile.write(result.read())
        fasta += 1

    print('Fasta files received: ' + str(fasta))



if __name__ == '__main__':
    unittest.main()
