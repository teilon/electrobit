'''
https://pypi.python.org/pypi/pyppeteer
'''


from bs4 import BeautifulSoup


runnable = True
host = 'http://saiman.kz'
host_counters = 'http://saiman.kz/products/schetchiki/'
host_transformators = 'http://saiman.kz/products/transformatory-toka/'
host_boards = 'http://saiman.kz/products/shkafy-ucheta/'

def start_parse():
    print('start parse')

    sheets_urls = get_sheets(host_counters)
    if sheets_urls is None or sheets_urls == []:
        print('sheets is None')
        return None

    output = []
    for sht in sheets_urls:
        data_from_sheet = parse(sht)
        output.extend(data_from_sheet)

    print('end parse')
    return output


def get_sheets(url):
    html = get_sleeply_html(url)
    soup = BeautifulSoup(html, 'lxml')

    paginator = soup.find('div', class_='paginator')
    output_urls = []

    if paginator is None:
        output_urls.append(host_counters)
        print('define sheets count')
        return output_urls

    sheets = paginator.find_all('a')
    for sht in sheets:
        href = sht['href'].strip()
        result = host_counters + '?p={}'.format(href)
        output_urls.append(result)

    print('define sheets count')
    return output_urls


def parse(url):
    print('start parse sheet')

    html = get_sleeply_html(url)
    soup = BeautifulSoup(html, 'lxml')
    products = soup.find('div', class_='products-list').find_all('a', class_='prod-prev')

    n = 0

    output = []
    for prd in products:
        # http://saiman.kz/i/Products/13_pp.png
        img_source = host + '{}'.format(prd.find('img')['src'])
        name_tag = prd.find('h4')
        if name_tag is not None:
            name = name_tag.contents[0]
        else:
            name = 'it is not known'
        description_tag = prd.find('p')
        if description_tag is not None:
            description = description_tag.contents[0]
        else:
            description = 'it is not known'
        cost_tag = prd.find('span', class_='cost')
        if cost_tag is not None:
            cost = cost_tag.contents[0]
        else:
            cost = 'it is not known'

        data = {
            'img_source': img_source,
            'name': name,
            'description': description,
            'cost': cost
        }

        n += 1
        output.append(data)

    print('end of parse sheet')
    return output


import requests
from random import uniform
from time import sleep


def get_html(url, useragent=None, proxy=None):
    r = requests.get(url, headers=useragent, proxies=proxy)
    return r.text


def get_sleeply_html(url):
    sleeptime = uniform(3, 7)
    sleep(sleeptime)

    while True:

        try:
            html = get_html(url)
        except Exception as e:
            continue
        else:
            break

    return html
