import sys

from pymod import index
from pymod.index import modules
from pymod.mappings import url

dom = index.domof('https://docs.python.org/3/library/functions.html')
for el in (el for el in dom.findAll('a', {'class': 'headerlink'})
           if '-' not in el.attrs['href']):
    sys.stdout.write("'{}', ".format(el.attrs['href'].split('#')[1]))
