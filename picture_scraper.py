from bs4 import BeautifulSoup
import time
import random
import requests
from urllib.request import urlretrieve

test_url = "https://mvideo.ru/smartfony-i-svyaz-10/smartfony-205/f/category=iphone-914"
agents = [
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko)',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko)'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
]

headers = {"User-Agent":random.choice(agents)}


def get_url(url):
    response = requests.get(url, headers=headers)
    return response.text


def load_image(image_name, url):
    r = requests.get(url, stream=True)
    with open(image_name, 'wb') as f:
        for chunk in r.iter_content():
            f.write(chunk)



def main():
    for i in range (2,3):
        html = get_url(test_url)
        soup = BeautifulSoup(html, "html.parser")
        image_list = soup.find_all(class_="product-grid-card")
        print(image_list)
        for img in image_list:
            img_url = img["src"]
            urlretrieve("https:" + img_url, img_url[-8:])
            print("Изображение скачано")



main()