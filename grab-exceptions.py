import sys

from pymod import index
from pymod.index import modules
from pymod.mappings import url

out = lambda s: sys.stdout.write(s)

out('{ ')

dom = index.domof('https://docs.python.org/2/library/exceptions.html')
for el in (el for el in dom.findAll('a', {'class': 'headerlink'})
           if '-' not in el.attrs['href']):
    out("'{}', ".format(el.attrs['href'].split('#exceptions.')[1]))
out('}\n')
