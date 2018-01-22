import requests
from bs4 import BeautifulSoup
import time

start_url = 'https://github.com/search?l=Java&o=desc&p=%d&q=%s&s=stars&type=Repositories&utf8='

base_url = 'https://github.com'
key = ""
page = 1


def query():
    html = requests.get(start_url % (page, key)).content
    soup = BeautifulSoup(html)
    title = soup.find('title').getText()
    print(title)

    datas = soup.findAll('div', {'class': "repo-list-item d-flex flex-justify-start py-4 public source"})
    for data in datas:
        info = data.find('div', {'class': "col-8 pr-3"}).find('a')
        link = base_url + info['href']
        name = info.getText()
        content = data.find('p', {'class': 'col-9 d-inline-block text-gray mb-2 pr-4'}).getText()
        print(name.strip())
        print(content.strip())
        print(link)
        print('-----------------------------------------------------------------------------------')


def main():
    global page
    global key
    key = input()
    while page < 6:
        try:
            page += 1
            query()
            time.sleep(5)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
