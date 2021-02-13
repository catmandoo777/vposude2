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

def pars1(url, data):

  soup = BeautifulSoup(data, 'lxml')

  name_product = soup.find('div', class_= 'page-header-wrapper').text.replace('\n', '').replace('  ', '')
  articul = soup.find('div', class_= 'product-info-sky product-sky').text.replace('\n', '').replace('  ', '')
  price = soup.find('div', class_='price js-product-price on-page product-info-price__price').text.replace('\n', '').replace('  ', '')
  characteristics = soup.find('div', class_='characteristics-block characteristics-block__sky cell-12').text.replace('\n', '').replace('  ', '')
  picters_url =soup.find('div', class_='gallery-main-wrapper text-center hide-sm').a.get('href')
  other = soup.find('div', id = 'characteristics-block').text.replace('\n', '').replace('  ', '')

  return {url:{'url': url, 'articul': articul, 'price': price, 'characteristics': characteristics, 'other': other, 'picters_url': picters_url }}

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
  with open('finish_data.json') as file:
    data = json.load(file)

  k = 0
  for i, j in data.items():
    print('Get_page: ' + i)
    if len(j) < 2:
      g = get_url(i)
      if g != None:
        try:
          result = pars1(i, g)[i]
          data[i] = result
          with open('finish_data.json', 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        except Exception:
          with open('error_pars_card.txt', 'a') as file:
            file.write(f'Error: {i} \n')
    else:
      print('pass: ' + i)
    k += 1
    if k >= 5500:
      break


  '''
  
  try:
    print(pars1(URL, src))
  except Exception:
    with open('error_pars_card.txt', 'a') as file:
      file.write(f'Error: {URL} \n')
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


if __name__ == '__main__':
  main()
