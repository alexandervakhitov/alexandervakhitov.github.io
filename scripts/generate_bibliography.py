#!/usr/bin/env python
import numpy as np
import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

# the bib file is generated automatically by Zotero
with open('publications/mypubs.bib') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)
#sort by date
years = []
for bib_item in bib_database.entries:
    years.append(-int(bib_item['year']))

bib_inds = np.argsort(years)

previous_year = -1
writer = BibTexWriter()
with open('publication_list.md', 'w') as md_file:
    #for bib_item in bib_database.entries:
    for bib_ind in bib_inds:
        if years[bib_ind] != previous_year:
            md_file.write("\n#### {}\n".format(-years[bib_ind]))
            previous_year = years[bib_ind]
        bib_item = bib_database.entries[bib_ind]
        if 'booktitle' in bib_item:
            venue = u' {},'.format(bib_item['booktitle']).replace('{', '').replace('}', '')
        elif bib_item['journal']:
            venue = u' {},'.format(bib_item['journal'])
        else:
            venue = u''

        if 'pages' in bib_item:
            pages = u' pp. {}'.format(bib_item['pages'])
        else:
            pages = u''

        if 'file' in bib_item:
            pdf_link = u' [pdf]({{{{site.url}}}}{})'.format(bib_item['file'])
        else:
            pdf_link = u''

        # create bibtex file
        db = BibDatabase()
        db.entries = [bib_item]
        bib_file = 'bib/{0}.bib'.format(bib_item['ID'])
        bib_link = u' [bib]({{{{site.url}}}}{})'.format('/scripts/publications/'+bib_file)
        with open('publications/{0}'.format(bib_file), 'w') as bib:
            bib_str = bibtexparser.dumps(db)
            bib.write(bib_str)
        year_str = bib_item['year']
        if len(pages)>0:
            year_str += ','
        md_file.write(u"- {0} **{1},** {2} {3} {4} {5} {6}\n".format(bib_item['author'],
                                                                  bib_item['title'].replace('{', '').replace('}', ''),
                                                                  venue,
                                                                  year_str,
                                                                  pages,
                                                                  pdf_link,
                                                                  bib_link))