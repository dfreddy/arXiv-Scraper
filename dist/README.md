# arXiv Scraper

Scrapes arXiv for yesterday's papers from selected lists

## Steps

- personalise config.json
- run the .exe

## Configs

- categories
	- follow format presented in example
	- category ID is found in the url: eg. General Topology -> math.GN (https://arxiv.org/list/math.GN/recent)
- maxPapers
	- max number of papers to download for each category
	- if the number of published papers for the day < maxPapers, then only that number of papers will be downloaded
- directory
	- path to the base folder where the papers will be stored
	- does not need to end in "arXiv Papers"

## Install exe from python

- pyinstaller --onefile -w scraper.py
