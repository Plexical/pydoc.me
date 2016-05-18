import requests
from bs4 import BeautifulSoup
from os.path import join

domof = lambda url: BeautifulSoup(requests.get(url).text, 'html.parser')

py3b = 'https://docs.python.org/3'
py2b = 'https://docs.python.org/2'

dom = domof('https://docs.python.org/3/library/itertools.html')
for link in dom.findAll('a', {'class': 'headerlink'}):
    href = link.attrs['href']
    name = href.split('#itertools.')
    if href.startswith('#itertools.'):
        print('3,{},{}'.format(name[-1],
                               join(py3b, 'library', 'itertools.html'+href)
        ))
        print('2,{},{}'.format(name[-1],
                               join(py2b, 'library', 'itertools.html'+href)
        ))
