import requests
from bs4 import BeautifulSoup
import csv



def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('cmc.csv', 'a') as f:
        writer = csv.writer(f)
        
        writer.writerow([data['name'],
                        data['symbol'],
                        data['price'],
                        data['link']])


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find('table', id='currencies').find('tbody').find_all('tr')
    # print(table)

    for tr in table:
        tds = tr.find_all('td')
        name = tds[1].find('a', class_='currency-name-container').text
        # print(name)
        symbol = tds[1].find('a').text
        # print(symbol)
        price = tds[3].find('a').get('data-usd')
        # print(price)
        link  = 'https://coinmarketcap.com' + tds[1].find('a', class_='currency-name-container').get('href')
        # print(link)


        data = {'name': name,
                'symbol': symbol,
                'price': price,
                'link': link}
        
        write_csv(data)

def main():
    url = 'https://coinmarketcap.com/'
    get_data(get_html(url))


if __name__ == "__main__":
    main()