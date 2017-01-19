!/usr/bin/env python
#-*- coding: utf-8 -*-
# Supporting Python 2.7.16
 
import sys, os, re
 
try:    bibtexdb = open(sys.argv[1]).read()
except: print("Error: specify the file to be processed!")

 # mirror from Jabref
 # https://raw.githubusercontent.com/JabRef/jabref/master/src/main/resources/journals/journalList.txt
if not os.path.isfile('journalList.txt'):
    import urllib
    urllib.urlretrieve("https://raw.githubusercontent.com/dlnguyen/Abbreviate-Journal-Names-in-Bibtex/master/journalList.txt", 
            filename="journalList.txt")
rulesfile = open('journalList.txt')
 
for rule in rulesfile.readlines()[::-1]:           ## reversed alphabetical order matches extended journal names first
    pattern1, pattern2 = rule.strip().split(" = ")
    if pattern1 != pattern1.upper() and (' ' in pattern1):        ## avoid mere abbreviations
        print("Replacing '%s' FOR '%s'" % (pattern1, pattern2))
    #bibtexdb = bibtexdb.replace(pattern1.strip(), pattern2.strip())    ## problem - this is case sensitive
        repl = re.compile(re.escape(pattern1), re.IGNORECASE)               ## this is more robust, although ca. 10x slower
        bibtexdb = repl.sub(pattern2, bibtexdb)
with open('abbreviated.bib', 'w') as outfile:
    outfile.write(bibtexdb)
    print "Bibtex database with abbreviated files saved into 'abbreviated.bib'"
