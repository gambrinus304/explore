import requests
from bs4 import BeautifulSoup
import csv
import re



def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    print(r.status_code)


def write_csv(data):
    with open('cmc_pagination.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'], data['link'], data['price']))
        


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    trs = soup.find('table', class_='table').find('tbody').find_all('tr')

    for tr in trs:
        td = tr.find_all('td')

        name = td[1].get('data-sort')
        # print(name)

        link = 'https://coinmarketcap.com' + td[1].find('a').get('href')
        # print(link)

        price = td[3].get('data-sort')
        # print(price)

        data = {'name': name,
                'link': link,
                'price': price}

        write_csv(data)



def main():
    url = 'https://coinmarketcap.com/'

    while True:
        get_page_data(get_html(url))

        soup = BeautifulSoup(get_html(url), 'lxml')
        
        try:
            pattern = 'Next'
            url = 'https://coinmarketcap.com/' + soup.find('ul', class_='pagination').find('a', text=re.compile(pattern)).get('href')
        except:
            break





if __name__ == "__main__":
    main()