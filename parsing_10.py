import requests
from bs4 import BeautifulSoup
import csv

 

def get_html(url):
    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/71.0.3578.98 Chrome/71.0.3578.98 Safari/537.36'}
    r = requests.get(url, headers=headers)
    return r.text


def write_csv(data):
    with open('testimonials.csv', 'a') as f:
        order = ['author', 'since']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)


def get_articles(html):
    soup = BeautifulSoup(html, 'lxml')
    ts = soup.find('div', class_='testimonial-container').find_all('article')
    return ts


def get_page_data(ts):
    for t in ts:
        try:
            since = t.find('p', class_='traxer-since').text.strip()
        except:
            since = ''
        try:
            author = t.find('p', class_='testimonial-author').text.strip()
        except:
            author = ''

        data = {'author': author, 'since': since}
        write_csv(data)


def main():
    page = 1
    while True:
        url = 'https://catertrax.com/why-catertrax/traxers/page/{}/'.format(str(page)) 
        print(url)
        
        articles = get_articles(get_html(url))
  

        # if articles list is empty, we get 'false'
        if articles:
            get_page_data(articles)
            page = page + 1
        else:
            break
    
    

if __name__ == "__main__":
    main()