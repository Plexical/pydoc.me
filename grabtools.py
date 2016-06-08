import os

import requests
from bs4 import BeautifulSoup

from pickle import load, dump

domof = lambda url: BeautifulSoup(requests.get(url).text, 'html.parser')

py3b = 'https://docs.python.org/3'
py2b = 'https://docs.python.org/2'

def modsof(v):
    cache = './.py{}mod'.format(v)
    if os.path.exists(cache):
        return load(open(cache, 'rb'))
    else:
        dom = domof('https://docs.python.org/{}/py-modindex.html'.format(v))
        mods = [m for m in (el.text for el in dom.findAll('code',
                                                          {'class': 'xref'}))]
        with open(cache, 'wb') as fp:
            dump(mods, fp)
        return mods
