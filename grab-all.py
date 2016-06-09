import os
import sys
import pprint
from grabtools import index_modules

if __name__ == '__main__':
    mods = index_modules()
    if '--pprint' in sys.argv:
        pprint.pprint(mods)
