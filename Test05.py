import requests
from bs4 import BeautifulSoup
import re

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# 获取页面所有内链的列表
def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    for link in bsObj.findAll('a', href=re.compile("^(/|.*" + includeUrl + ")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks


# 获取页面所有外链的列表
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    for link in bsObj.findAll('a', href=re.compile("^(http|www)((?!" + excludeUrl + ").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


def splitAddress(address):
    addressParts = address.replace('https://', '').split('/')
    return addressParts


allExtLinks = set()
allIntLinks = set()


def getAllExternalLinks(siteUrl):
    try:
        html = requests.get(siteUrl).content
        soup = BeautifulSoup(html)
        internalLinks = getInternalLinks(soup, splitAddress(siteUrl)[0])
        externalLinks = getExternalLinks(soup, splitAddress(siteUrl)[0])

        for link in externalLinks:
            if link is not None:
                if link not in allExtLinks:
                    allExtLinks.add(link)
                    print(link)

        for link in internalLinks:
            if link is not None:
                if link not in allIntLinks:
                    allIntLinks.add(link)
                    print(link)
                    getAllExternalLinks(link)
    except Exception as e:
        pass


getAllExternalLinks("https://www.baidu.com")
