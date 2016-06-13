# pydoc.me

Quick redirects to Python documentation.

## Overview

`pydoc.me` is a fairly straight-forward Flask app, with routes with
routes declared in [pymod/routes.py](pymod/routes.py) (preliminary
name was `pymod.me`, might change the package dir some day).

The actual work is two-part: 1) [pymod/index.py](pymod/index.py)
handles indexing of the https://docs.python.org site (mostly via the
[requests](http://docs.python-requests.org/) and
[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
libraries). And 2) [pymod/mappings.py](pymod/mappings.py) looks up
names and the URLs to redirect to.

Indexing creates a 'modules cache' file
[pymod/modules.dat](pymod/modules.dat) (generated, so it's not visible
in the repo). The cache file must be generated locally and is included
in the distribution package via standard `setuptools` mechanics, as
can be seen in the [MANIFEST.in](MANIFEST.in) and the
[setup.py](setup.py) files.

When running with a module index cache, names are fetched using the
`url()` function in the [pymod/mappings.py](pymod/mappings.py)
file. The `url()` function first checks a few special embedded
structures representing built-in symbols, then looks for the search
term in the modules cache. Certain modules are considered 'priority'
and functions in them do not need to be prepended by their module name
(e.g. `itertools`, `sys`, `os`, `pdb`). I have simply chosen modules
that I use more often and that I subjectively consider more central.

## Development

I can't yet guarantee complete portability from machine to machine for
contributing to `pydoc.me`. If interest grows, I'll add it. Since it's
not overly complex, you could probably do it, though - you need GNU
Make, Python 3 and a recent version of
[virtualenv](https://virtualenv.pypa.io/). Have a look at the
[Makefile](Makefile).

I'm hosting `pydoc.me` at WebFaction, so obviously I would have to
deploy new versions, though ;-). But you can probably have it running
locally without too much trouble.
