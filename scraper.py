import os
import time
import json
import urllib.request as libreq
import feedparser
import re
from datetime import date

import utils

config = json.load(open('./config.json', 'r'))
date_dir = utils.checkYesterdaysDir()

# the query filters according to id_list, so in order to query all categories it must be made n queries
for category in config['categories']:
    ## get page
    query = f"http://export.arxiv.org/api/query?search_query=cat:{category}&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending"
    response = libreq.urlopen(query).read()
    feed = feedparser.parse(response)

    # make dir for the category
    category_dir = date_dir + '/' + category
    if len(feed.entries) > 0:
        try:
            os.mkdir(category_dir)
        except:
            pass

    counter = 0
    for entry in feed.entries:
        #print(json.dumps(entry, indent=5))         # useful print to understand entry structure

        # end if there's no more papers for yesterday
        if not utils.isPaperFromYesterday(entry.date):
            break

        # check if there's a pdf for the paper, go to next if otherwise
        pdf_url = None
        for link in entry.links:
            if 'title' in link and link['title'] == 'pdf':
                pdf_url = link['href']
        if pdf_url == None:
            continue

        # fetch pdf and save it
        pdf_title = re.sub('[\*\\\:\<\>\?\/\|]', '-', entry['title']).replace('\n', '') + '.pdf'
        pdf_path = category_dir + '/' + pdf_title
        if os.path.exists(pdf_path):
            continue
        pdf_content = libreq.urlopen(pdf_url).read()
        file = open(pdf_path, 'wb')
        file.write(pdf_content)
        file.close()

        counter = counter + 1
        if counter >= config['maxPapers']:
            break
        #print(f'{category} - {counter}')

utils.activateFinished()