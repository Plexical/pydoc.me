import os

py3b = 'https://docs.python.org/3'
py2b = 'https://docs.python.org/2'
from os.path import join

make = lambda v, *segs: v == 3 and join(py3b, *segs) or join(py2b, *segs)

lib3 = lambda page: make(3, 'library', page)
expanded = {
    '2': {},
    '3': {
        'itertools': lib3('itertools.html'),
        'accumulate': lib3('itertools.html#itertools.accumulate'),
        'chain': lib3('itertools.html#itertools.chain'),
        'chain.from_iterable': lib3('itertools.html#itertools.chain.from_iterable'),
        'combinations': lib3('itertools.html#itertools.combinations'),
    }
}

def url(v, term):
    return v in expanded and term in expanded[v] and expanded[v][term] or None
