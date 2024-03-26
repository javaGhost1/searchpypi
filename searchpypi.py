#!/usr/bin/env python3
# searchpypi.py - Opens several search results.

import requests
import sys
import webbrowser
import bs4


def search(package_search):
       # display text while downloading the search result page
    print('Searching...') 
    
    res = requests.get('https://pypi.org/search/?q=' + package_search)
    res.raise_for_status()
    # Parse HTML content
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # Oselect() method finds elements using css selectors
    linkElems = soup.select('.package-snippet')
    # pick first five elements
    numOpen = min(5, len(linkElems))

    for i in range(numOpen):
        urlToOpen = 'https://pypi.org' + linkElems[i].get('href')

        print('Opening', urlToOpen)
        # open a new web tab for each link
        webbrowser.open(urlToOpen)

if __name__ == "__main__":
    package_search = ' '.join(sys.argv[1:])
    search(package_search)