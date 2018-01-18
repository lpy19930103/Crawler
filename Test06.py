# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import json
import codecs
import time

BASE_URL = 'https://www.jianshu.com'
TOP_30_URL = BASE_URL + '/trending/monthly?&page=%d'
num = 1


class Top30Item(object):
    def __init__(self, title, link):
        self.title = title
        self.link = link


def get_top_30(url):
    print(url)
    html = requests.get(url).content
    soup = BeautifulSoup(html)
    note_list = soup.find('ul', {'class': 'note-list'}).findAll('li')
    list = []
    for note in note_list:
        content_link = note.find('div', {'class', 'content'}).find('a', {'class': 'title'})['href']
        content_title = note.find('div', {'class', 'content'}).find('a', {'class': 'title'}).getText()
        list.append(json.dumps(Top30Item(content_title, BASE_URL + content_link).__dict__, ensure_ascii=False))
        print(json.dumps(Top30Item(content_title, BASE_URL + content_link).__dict__, ensure_ascii=False))
    return list


def main():
    global num
    all = []
    top30List = get_top_30(TOP_30_URL % num)
    all.append(top30List)
    while top30List:
        try:
            time.sleep(10)
            num += 1
            top30List = get_top_30(TOP_30_URL % num)
            all.append(top30List)
        except Exception as e:
            print(e)
            break

    with codecs.open("TOP30.txt", "wb", encoding='utf-8') as f:
        for Top30Item in all:
            f.write(u'{Top30Item}\n'.format(Top30Item='\n'.join(Top30Item)))
            # f.write(Top30Item + '\n')


if __name__ == '__main__':
    main()
