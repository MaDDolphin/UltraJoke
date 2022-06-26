from typing import Dict, Any
import json
import requests
from bs4 import BeautifulSoup
import os
import re


def read_file(filename):
    with open(filename, encoding='utf-8') as input_file:
        text = input_file.read()
    return text


def html_req():
    for page_nmb in range(1, 68):
        print(page_nmb)
        url = 'https://baneks.site/best/?p=%d#' % page_nmb
        r = requests.get(url)
        with open('./pages/' + str(page_nmb) + '.html', 'w', encoding="utf-8") as output_file:
            output_file.write(r.text)


def joke_links_parse(filename, links):
    text = read_file(filename)
    soup = BeautifulSoup(text)
    jokes_list = soup.find('div', {'class': 'page-content mdl-cell mdl-cell--6-col'})
    jokes = jokes_list.find_all('div', {'class': 'joke mdl-shadow--6dp block mdl-card mdl-card--border'})
    for joke in jokes:
        link = joke.find('div', {'class': 'actions-container'}).find('a').get('href')
        links.append(link)


def joke_parse(links):
    print('Start joke download!')

    for link in links:
        print(id, ' joke ')
        url = 'https://baneks.site' + link
        r = requests.get(url)
        with open('./jokes_pages/' + str(id) + '.html', 'w', encoding="utf-8") as output_file:
            output_file.write(r.text)
        id = id + 1
    print('Jokes were loaded')


def joke_text_parse(filename, joke_dic, id):
    text = read_file(filename)
    soup = BeautifulSoup(text)
    jokes_list = soup.find('div', {'class': 'joke mdl-shadow--6dp block mdl-card mdl-card--border'})
    jokes = jokes_list.find_all('div', {
        'class': 'block-content mdl-card__supporting-text mdl-color--grey-300 mdl-color-text--grey-900'})
    for joke in jokes:
        joke_str = str(joke.find('section', {'itemprop': 'description'}).find('p'))
        joke_str = joke_str.replace('</p>', '')
        joke_str = joke_str.replace('<p>', '')
        joke_str = joke_str.replace('<br/>', '\n')
    joke_dic[id] = joke_str
    print('Joke number ', id)


def main():
    html_req()
    links = []
    id = 0
    joke_dic = {}
    for root, dirs, files in os.walk('./pages'):
        for file in files:
            joke_links_parse('./pages/' + file, links)
    joke_parse(links)
    for root, dirs, files in os.walk('./jokes_pages'):
        for file in files:
            joke_text_parse('./jokes_pages/' + file, joke_dic, id)
            id = id + 1
    with open('jokes.json', 'w') as fp:
        json.dump(joke_dic, fp)


if __name__ == "__main__":
    main()
