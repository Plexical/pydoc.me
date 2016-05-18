import requests
from bs4 import BeautifulSoup

domof = lambda url: BeautifulSoup(requests.get(url).text, 'html.parser')

py3b = 'https://docs.python.org/3'
py2b = 'https://docs.python.org/2'
