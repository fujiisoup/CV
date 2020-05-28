"""
Find details of papers and export as necessary formats
Need to install crossref library,
>>> pip install crossref
"""
from crossref.restful import Works
import numpy as np


def download_details(doi_list):
    works = Works()
    details = []
    for j, doi in enumerate(doi_list):
        doi = doi.strip()
        work = works.doi(doi)
        details.append(work)
    return details


def get_firstauthor(details):
    firstauthors = []
    for detail in details:
        if detail['author'][0].get('family', None).lower() == 'fujii':
            firstauthors.append(detail)
    return firstauthors


def sort_by_date(details, newest_first=True):
    dates = []
    for detail in details:
        y = detail['journal-issue']['published-print']['date-parts'][0][0]
        m = detail['journal-issue']['published-print']['date-parts'][0][1]
        dates.append(int('{0:d}{1:02d}'.format(y, m)))
    idx = np.argsort(dates)
    if newest_first:
        idx = idx[::-1]
    return [details[i] for i in idx]


def save_markdown(details, outname):
    """
    Save as a markdown format
    """
    details = sort_by_date(details)
    saved_contents = [
        'title', 'publisher', 
        'author', 'journal-issue', 'article-number',
        'short-container-title', 'container-title', 'volume',
    ]
    lines = [
        "# List of published papers",
    ]
    for detail in details:
        lines.append('#### {}\n'.format(detail['title'][0]))
        authors = ''
        for author in detail['author']:
            if author['family'].lower() == 'fujii':
                authors += '**{} {}**, '.format(author['given'], author['family'])
            else:
                authors += '{} {}, '.format(author['given'], author['family'])
        lines.append(' {}\n'.format(authors[:-2]))  # remove the last comma
        # journal
        articlenumber = detail.get('article-number', detail.get('page'))
        lines.append(' *{}* **{},** {} ({})\n'.format(
            detail['container-title'][0], 
            detail['journal-issue']['issue'],
            articlenumber, 
            detail['journal-issue']['published-print']['date-parts'][0][0]
        ))

    with open(outname, 'w') as f:
        for line in lines:
            f.write(line + '\n')


if __name__ == '__main__':
    with open('_papers.csv', 'r') as f:
        doi_list = f.readlines()
    details = download_details(doi_list)
    with open('dois.txt', 'w') as f:
        for detail in details:
            f.write('{}\n'.format(detail))
    save_markdown(details, 'papers.md')