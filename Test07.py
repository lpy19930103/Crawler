import requests
from bs4 import BeautifulSoup

start_url = 'https://github.com/search?l=Java&o=desc&q=%s&s=stars&type=Repositories&utf8='

base_url = 'https://github.com'
key = "";


def query():
    html = requests.get(start_url % key).content
    soup = BeautifulSoup(html)
    title = soup.find('title').getText()
    info = soup.find('div', {'class': "col-8 pr-3"}).find('a')
    link = base_url + info['href']
    name = info.getText()
    content = soup.find('p', {'class': 'col-9 d-inline-block text-gray mb-2 pr-4'}).getText()
    print(title)
    print(name)
    print(content)
    print(link)


def main():
    global key
    key = input()
    query()


if __name__ == '__main__':
    main()
