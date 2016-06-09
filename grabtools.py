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

def anchors(name, url):
    dom = domof(url)
    class_ = {'class': 'headerlink'}
    As = (a.attrs['href'].split('#')[1] for a in dom.findAll('a', class_))
    return [a for a in As if a.startswith(name)]

def index_modules():
    "Loads all shortcuts from cache or downloads from docs.python.org"

    cache = './.modules'

    if os.path.exists(cache):
        with open(cache, 'rb') as fp:
            return load(fp)

    else:
        master = {}

        for m3 in modsof('3'):
            mod_url = py3b+'/library/{}.html'.format(m3)
            master[m3] = { '3': { 'M': mod_url } }
            print('Anchors/{} for {}..'.format('3', m3))
            for anchor in anchors(m3, master[m3]['3']['M']):
                master[m3]['3'] = dict(
                    master[m3]['3'],
                    **{ anchor:
                        '{}/library/{}.html#{}'.format(py3b, m3, anchor) })

        for m2 in modsof('2'):
            mod_url = py2b+'/library/{}.html'.format(m2)
            if m2 in master:
                master[m2]['2'] = { 'M': mod_url }
            else:
                master[m2] = {'2': {'M': mod_url}}
            print('Anchors/{} for {}..'.format('2', m2))
            for anchor in anchors(m2, master[m2]['2']['M']):
                master[m2]['2'] = dict(
                    master[m2]['2'],
                    **{ anchor: '{}/library/{}.html#{}'.format(py2b, m2, anchor) })
        with open(cache, 'wb') as fp:
            dump(master, fp)
            return master
