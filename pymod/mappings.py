import os

py3b = 'https://docs.python.org/3'
py2b = 'https://docs.python.org/2'
from os.path import join

make = lambda v, *segs: v == 3 and join(py3b, *segs) or join(py2b, *segs)

lib3 = lambda page: make(3, 'library', page)
lib2 = lambda page: make(2, 'library', page)
expanded = {
    '2': {
        'abc': lib2('abc.html'),
        'itertools': lib2('itertools.html'),
        'ifilterfalse': lib2('itertools.html#itertools.ifilterfalse'),
        'izip_longest': lib2('itertools.html#itertools.izip_longest'),

    },
    '3': {
        'abc': lib3('abc.html'),
        'ABC': lib3('abc.html#abc.ABC'),
        'abc.ABC': lib3('abc.html#abc.ABC'),
        'itertools': lib3('itertools.html'),
        'accumulate': lib3('itertools.html#itertools.accumulate'),
        'zip_longest': lib3('itertools.html#itertools.zip_longest'),
    }
}
def abc_same(name):
    expanded['2'][name] = lib2('abc.html#abc.'+name)
    expanded['3'][name] = lib3('abc.html#abc.'+name)

for name in ('ABCMeta', 'ABCMeta.register', 'ABCMeta.__subclasshook__',
             'abstractmethod', 'abstractstaticmethod', 'abstractclassmethod',
             'abstractproperty', 'get_cache_token'):
    abc_same(name)

def itertools_same(name):
    expanded['2'][name] = lib2('itertools.html#itertools.'+name)
    expanded['3'][name] = lib3('itertools.html#itertools.'+name)

for name in ('chain', 'chain.from_iterable', 'combinations',
             'combinations_with_replacement', 'groupby', 'islice',
             'compress', 'count', 'cycle', 'dropwhile', 'filterfalse',
             'permutations', 'product', 'repeat', 'starmap', 'takewhile',
             'tee'):
    itertools_same(name)

def url(v, term):
    return v in expanded and term in expanded[v] and expanded[v][term] or None
