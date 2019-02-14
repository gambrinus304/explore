import requests
from bs4 import BeautifulSoup
import csv
import json



def get_html(url):
    r = requests.get(url)
    # return r.text
    # return r.json()
    # return r.headers
    return r


def write_csv(data):
    with open ('youtube.csv', 'a') as f:
        order = ['name', 'url']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)

# ---!!!---
def write_html(data):
    with open ('youtube.html', 'w') as file:
        file.write(data)


def write_json(data):
    with open ('youtube.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)
# ---!!!---


def get_page_data(response):
    if 'html' in response.headers['Content-Type']:
        html = response.text
    else:
        html = response.json()['content_html']

    soup = BeautifulSoup(html, 'lxml')
    
    items = soup.find_all('h3', class_='yt-lockup-title')

    for item in items:
        name = item.text
        url = 'https://youtube.com' + item.find('a').get('href')
        # print (name)
        # print (url)
        
        data = {'name': name, 'url': url}
        write_csv(data)


def get_next(response):

    # if 'html' in response.headers['Content-Type']:
    #     html = response.text
    # else:
    #     # html = response.json()['1']
    #     print('Server posted the json-type response')

    try:
        html = response.text
        print('we get next html')
        # print(html)
        write_html(html)

    except:
        print('Server posted the json-type response')
        
    soup = BeautifulSoup(html, 'lxml')
    try:
        url = 'https://youtube.com' + soup.find('button', class_='yt-uix-load-more').get('data-uix-load-more-href')
    except:
        url = ''


    print(url)
    return url



def main():
    # url = 'https://www.youtube.com/channel/UCBDLWj5X5D9bvBa3JIMMTIQ/videos'    
    # url = 'https://www.youtube.com/browse_ajax?ctoken=4qmFsgJAEhhVQ0JETFdqNVg1RDlidkJhM0pJTU1USVEaJEVnWjJhV1JsYjNNZ0FEZ0JZQUZxQUhvQk03Z0JBQSUzRCUzRA%253D%253D&continuation=4qmFsgJAEhhVQ0JETFdqNVg1RDlidkJhM0pJTU1USVEaJEVnWjJhV1JsYjNNZ0FEZ0JZQUZxQUhvQk03Z0JBQSUzRCUzRA%253D%253D&itct=CBwQybcCIhMI7_eTv4634AIVlbSbCh1j0Q'
    url = 'https://www.youtube.com/browse_ajax?ctoken=4qmFsgJAEhhVQ0JETFdqNVg1RDlidkJhM0pJTU1USVEaJEVnWjJhV1JsYjNNZ0FEZ0JZQUZxQUhvQk03Z0JBQSUzRCUzRA%253D%253D'
           
    # get_page_data(get_html(url))

    while True:
        response = get_html(url)
        get_page_data(response)

        url = get_next(response)
        # get_next(response)

        if url:
            continue
        else:
            print('no more link')
            break

    # write_html(get_html(url))










if __name__ == "__main__":
    main()