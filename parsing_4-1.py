import requests
from bs4 import BeautifulSoup
import csv
import re





def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    # print(r.status_code)



def write_csv(data):
    with open('habr.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'],
                        data['url'],
                        data['tags']))



def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    post_id = re.compile('post_\d{6}')
    lis = soup.find('div', class_='posts_list').find_all('li', class_='content-list__item', id=post_id )

    for li in lis:
        try:
            name = li.find('article', class_='post_preview').find('h2', class_='post__title').text.strip()
        except:
            pass
        # print (name)
        
        try:
            url = li.find('article', class_='post_preview').find('h2', class_='post__title').find('a').get('href')
        except:
            url = ''
        # print(url)

        try:
            tags_list = []
            tags_hub = li.find('article', class_='post_preview').find('ul', class_='post__hubs').find_all('li')
            
            for tag in tags_hub:
                tag = tag.find('a').text
                tags_list.append(tag)
            tags = ", ".join(tags_list)
            # print(tags)

        except:
            tags_hub = ''
        # print (tags_hub) 


        data = {'name': name,
                'url': url,
                'tags': tags}

        write_csv(data)



def main():
    pattern = 'https://habr.com/ru/page{}/'

    for i in range(1, 4):
        url = pattern.format(str(i))
        get_page_data(get_html(url))



if __name__ == "__main__":
    main()