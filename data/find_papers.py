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
        if doi[0] == '#':
            continue
        work = works.doi(doi)
        work['doi'] = doi
        details.append(standarize(work))
    return details


def get_firstauthor(details):
    firstauthors = []
    for detail in details:
        if detail['author'][0].get('family', None).lower() == 'fujii':
            firstauthors.append(detail)
    return firstauthors


def standarize(detail):
    if 'journal-issue' not in detail:
        detail['journal-issue'] = {}
    if 'published-print' not in detail['journal-issue']:
        detail['journal-issue']['published-print'] = {}
        detail['journal-issue']['published-print']['date-parts'] = detail['issued']['date-parts']
    if len(detail['journal-issue']['published-print']['date-parts'][0]) < 2:
        if isinstance(detail['journal-issue']['published-print']['date-parts'][0][0], list):
            detail['journal-issue']['published-print']['date-parts'][0] = detail['journal-issue']['published-print']['date-parts'][0][0]
        if len(detail['journal-issue']['published-print']['date-parts'][0]) == 1:
            detail['journal-issue']['published-print']['date-parts'][0].append(0)  # month not available

    if 'container-title' in detail:
        if len(detail['container-title']) == 0:
            print(detail['doi'])
            print(detail)

    for author in detail['author']:
        if 'family' not in author:
            author['family'] = author['name']
        if 'given' not in author:
            author['given'] = ''
    return detail


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
    lines = [
        "# List of published papers",
    ]
    for i, detail in enumerate(details):
        lines.append('{}. **{}**  '.format(i + 1, detail['title'][0]))
        authors = ''
        for author in detail['author']:
            if author['family'].lower() == 'fujii':
                authors += '**<u>{} {}</u>**, '.format(author['given'], author['family'])
            else:
                authors += '{} {}, '.format(author['given'], author['family'])
        lines.append(' {}  '.format(authors[:-2]))  # remove the last comma
        # journal
        articlenumber = detail.get('article-number', detail.get('page'))
        lines.append(' *{}* **{},** {} ({})  '.format(
            detail['container-title'][0], 
            detail['volume'],
            articlenumber, 
            detail['journal-issue']['published-print']['date-parts'][0][0]
        ))
        lines.append('<a href="https://doi.org/{0:s}">{0:s}</a>  \n'.format(detail['doi']))

    with open(outname, 'w') as f:
        for line in lines:
            f.write(line + '\n')


def save_cv1(details, outname):
    """
    者名，論文タイトル，著書名・学会誌・雑誌名等（著書の場合は出版社名も記載），巻号，頁，年月の順に記載してください。
    
    共著の場合は，本人の氏名を含め，著者全員の氏名を論文に記載された順に記入してください。本人の氏名にアンダーラインを付けてください。また本人が当該論文のCorresponding authorである場合は氏名の後に”*”を付けてください。（例．Hiroshima.T*）
    """
    details = sort_by_date(details, newest_first=False)
    lines = [
        "# List of published papers",
    ]
    for i, detail in enumerate(details):
        authors = ''
        for author in detail['author']:
            if author['family'].lower() == 'fujii':
                authors += '__**{} {}**__, '.format(author['given'], author['family'])
            else:
                authors += '{} {}, '.format(author['given'], author['family'])
        lines.append('({})\n{}  '.format(i+1, authors[:-2]))  # remove the last comma
        lines.append('**{}**  '.format(detail['title'][0]))
        # journal
        articlenumber = detail.get('article-number', detail.get('page'))
        lines.append(' *{}* **{},** {} ({}.{})  \n'.format(
            detail['container-title'][0], 
            detail['volume'],
            articlenumber, 
            detail['journal-issue']['published-print']['date-parts'][0][0],
            detail['journal-issue']['published-print']['date-parts'][0][1],
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
    save_cv1(details, 'private_papers.md')