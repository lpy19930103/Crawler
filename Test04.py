#下载简书文章中的图片
import requests
from bs4 import BeautifulSoup
import codecs
import os

BASE_URL = 'http://movie.douban.com/top250'


def load_page(url):
    data = requests.get(url).content
    return data


def format_html(html):
    soup = BeautifulSoup(html)
    var = soup.find('ol', {'class': 'grid_view'})
    movie_list = []
    for movie in var.findAll('li'):
        title = movie.find('div', {'class': 'hd'}).find('span', {'class': 'title'}).getText()
        pic = movie.find('div', {'class': 'pic'}).find('a').find('img')['src']
        movie_list.append({'title': title, 'pic': pic})

    if get_next(html):
        return movie_list, BASE_URL + get_next(html)
    return movie_list, None


def download_img(movie):
    print(movie)
    file_path = './pic/'
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    img = requests.get(movie['pic']).content
    with codecs.open(file_path + movie['title'] + '.jpg', 'wb')as f:
        f.write(img)


def get_next(html):
    soup = BeautifulSoup(html)
    try:
        return soup.find('span', {'class': 'next'}).find('a')['href']
    except Exception as e:
        return None


def main():
    next_url = BASE_URL
    with codecs.open('movies.txt', 'wb', encoding='utf-8')as fp:
        while next_url:
            movies, next_url = format_html(load_page(next_url))
            for movie in movies:
                fp.write(u'{movie}\n'.format(movie=''.join(movie['title'])))
                # download_img(movie)


if __name__ == '__main__':
    main()
