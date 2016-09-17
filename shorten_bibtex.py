#!/usr/bin/env python

# Shorten a bibtex file so I can import it into Overleaf (<1mb)
# also get rid of all my annotations and stuff which is useless (and perhaps
# embarrassing) anyway)

import argparse, bibtexparser
parser = argparse.ArgumentParser()
parser.add_argument('--input_file', default='bibtex_raw.txt')
parser.add_argument('--output_file', default='bibtex_short.txt')
args = parser.parse_args()

bibdb = bibtexparser.load(open(args.input_file))
for entry in bibdb.entries:
    for property in ['file', 'mendeley-groups', 'annote', 'abstract', 'keyword']:
        if property in entry:
            del entry[property]
    
    print '@%s{%s,' % (entry['ENTRYTYPE'], entry['ID'].encode('utf8'))
    
    # Should just be able to dump to file, but unicode errors.
    for key, value in entry.items():
        if key in ['ID', 'ENTRYTYPE']:
            continue
        else:
            key = key.encode('utf8')
            value = value.encode('utf8')
            if key == 'title':
                print '%s = {{%s}},' % (key, value)
            else:
                print '%s = {%s},' % (key, value)
        
    print '}'
    print

