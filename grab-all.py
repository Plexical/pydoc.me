import os
from grabtools import domof, modsof, anchors, py3b, py2b

from pickle import load, dump

cache = './.master'

if os.path.exists(cache):
    with open(cache, 'rb') as fp:
        master = load(fp)
else:
    master = {}

    for m3 in modsof('3'):
        mod_url = py3b+'/library/{}.html'.format(m3)
        master[m3] = {
            '3': {
                'M': mod_url
            }
        }
        print('Anchors/{} for {}..'.format('3', m3))
        for anchor in anchors(m3, master[m3]['3']['M']):
            master[m3]['3'] = dict(
                master[m3]['3'],
                **{ anchor: '{}/library/{}.html#{}'.format(py3b, m3, anchor) })

    for m2 in modsof('2'):
        mod_url = py2b+'/library/{}.html'.format(m2)
        if m2 in master:
            master[m2]['2'] = {
                'M': mod_url
            }
        else:
            master[m2] = {'2': {'M': mod_url}}
        print('Anchors/{} for {}..'.format('2', m2))
        for anchor in anchors(m2, master[m2]['2']['M']):
            master[m2]['2'] = dict(
                master[m2]['2'],
                **{ anchor: '{}/library/{}.html#{}'.format(py2b, m2, anchor) })

    with open(cache, 'wb') as fp:
         dump(master, fp)
