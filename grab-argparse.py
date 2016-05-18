from grabtools import domof, py3b, py2b

from os.path import join

dom = domof('https://docs.python.org/3/library/argparse.html')

for link in dom.findAll('a', {'class': 'headerlink'}):
    href = link.attrs['href']
    name = href.split('#argparse.')
    if href.startswith('#argparse.'):
        print('3,{},{}'.format(name[-1],
                               join(py3b, 'library', 'argparse.html'+href)
        ))
        print('2,{},{}'.format(name[-1],
                               join(py2b, 'library', 'argparse.html'+href)
        ))
