from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.head.title
    except AttributeError as e:
        return None
    return title


title = getTitle("http://open.uc.cn/")

if title:
    print(title)
else:
    print('title is none')
