from setuptools import setup

import pymod

requirements = (
    'Flask==0.10.1',
    'requests==2.10.0',
    'beautifulsoup4==4.4.1'
)

setup(
    name=pymod.name,
    packages=('pymod',),
    include_package_data=True,
    zip_safe=False,
    author='Jacob Oscarson',
    author_email='jacob@plexical.com',
    install_requires=requirements,
    version='.'.join(map(str, pymod.version)))
