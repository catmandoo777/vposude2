import requests
from bs4 import BeautifulSoup
import lxml
import json
from time import sleep
from random import randint

def url_pan():
  url1_panding = {'https://vposude.ru/collection/podarochnye-nabory': 3,'https://vposude.ru/collection/posuda-dlya-prigotovleniya': 159, 'https://vposude.ru/collection/kastryuli': 42, 'https://vposude.ru/collection/skovorody': 60, 'https://vposude.ru/collection/zharovni': 2, 'https://vposude.ru/collection/skorovarki': 3, 'https://vposude.ru/collection/chugunnaya-posuda': 1, 'https://vposude.ru/collection/geyzernye-kofevarki': 3, 'https://vposude.ru/collection/kofemolka': 1, 'https://vposude.ru/collection/turki': 1, 'https://vposude.ru/collection/french-pressy': 3, 'https://vposude.ru/collection/kuhonnye-nozhi': 60, 'https://vposude.ru/collection/vidy-nozhey': 29, 'https://vposude.ru/collection/keramicheskie-nozhi': 3,'https://vposude.ru/collection/damasskie-kuhonnye-nozhi': 6, 'https://vposude.ru/collection/nozhi-iz-odnosloyinoy-stali': 9, 'https://vposude.ru/collection/kovanye-kukhonnye-nozhi': 2, 'https://vposude.ru/collection/kuhonnye_prinadlezhnosti': 128,
  'https://vposude.ru/collection/reshetki-dlya-barbekyu':   1, 'https://vposude.ru/collection/nabory-dlya-barbekyu':  1}

  url2 = []

  for i, j in url1_panding.items():
    k = 2
    with open('url_catalog.txt', 'a') as file:
      file.write(f'{i}\n')
    while k <= j:
      with open('url_catalog.txt', 'a') as file:
        file.write(i + f'?page={k}'+ '\n')
      k += 1

    with open('url_catalog.txt',) as file:
      data = file.read().split('\n')


def get_urls_carts(data):
  urls_carts = []
  soup = BeautifulSoup(data, 'lxml')

  data = soup.find('div', class_='products-list row').find_all('div', class_='product-card-wrapper product-card-wrapper-cus cell-3 cell-4-md cell-6-sm cell-12-xs')
  for d in data:
    urls_carts.append('https://vposude.ru/' + d.find('a').get('href'))
  return urls_carts

def get_url(URL):
  HEADERS = {'accept': '*/*', 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}
  req = requests.get(URL, HEADERS)
  sleep(randint(1, 2))
  if req.status_code == 200:
    return req.text
  else:
    return None  

def main():
  '''
  with open('url_catalog.txt',) as file:
    data = file.read().split('\n')
  for g in data:
    print(g)

    req = get_url(g)
    if req != None:

      with open('data.json') as file:
        d = json.load(file)

      for i in get_urls_carts(req):
        d[i] = {'url': i}

      with open('data.json', 'w') as file:
        json.dump(d, file, indent=4, ensure_ascii=False)

      with open('check_list1.txt', 'a') as file:
        file.write(g + '\n')
        '''
  

'''
with open('data.json') as file:
  data = json.load(file)

for i, j in data.items():
  temp = get_url(i)
  if temp != None:
    with open('index2.html', 'w') as file:
      file.write(temp)
  break
'''  
primer = {'url':{'url': 'url', 'articul': 'articul', 'maider': 'maider', 'price': 'price', 'text': 'text', 'cheracters': 'cheracters', }}

with open('index2.html') as file:
  src = file.read()

soup = BeautifulSoup(src, 'lxml')

print(soup.find('div', class_= 'row product-main-wrapper'))