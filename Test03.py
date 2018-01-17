from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import ssl
import random

ssl._create_default_https_context = ssl._create_unverified_context


def getBsObj(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        resObj = BeautifulSoup(html.read())
    except ArithmeticError as e:
        return None
    return resObj


def getLinks(url):
    bsObj = getBsObj('https://en.wikipedia.org' + url)

    if bsObj is None:
        print("bsObj is None")
        return None
    else:
        return bsObj.find('div', {'id': 'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))


links = getLinks('/wiki/Kevin_Bacon')
while len(links) > 0:
    newPage = links[random.randint(0, len(links) - 1)].attrs['href']
    print(newPage)
    links = getLinks(newPage)
