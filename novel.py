# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests

target = 'https://read.qidian.com/chapter/r5YwhJIIZtkuTkiRw_sFYA2/TQWhvZa8wJ2aGfXRMrUjdw2'

def write_txt(str):
     with open('test.txt', 'w+', encoding='UTF-8') as file:
         file.write(str)

def get_content():
     req = requests.get(url = target)
     html = req.text
     bf = BeautifulSoup(html, 'html.parser')
     div = bf.find_all('div', class_ = 'read-content j_readContent')
     str = div[0].text
     str = str.replace('\n', '', 3)
     str = str.replace('　　', '\r\n\t')
     return str

def get_title():
     req = requests.get(url = target)
     html = req.text
     bf = BeautifulSoup(html, 'html.parser')
     div = bf.find_all('h3', class_ = 'j_chapterName')
     return div[0].text

if __name__ == "__main__":
     title = get_title()
     content = get_content()
     print(title + '\r\n' + content)
     write_txt(title + '\r\n' + content)
