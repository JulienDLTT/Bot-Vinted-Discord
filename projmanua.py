import requests
from bs4 import BeautifulSoup

def get_vinted_ads():
    url = 'https://www.vinted.fr/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        ads = soup.find_all(class_='c-box--row c-box--row--item')
        for ad in ads:
            title = ad.find(class_='c-box__title').text.strip()
            price = ad.find(class_='c-box__price').text.strip()
            print(f'Titre: {title}, Prix: {price}')
    else:
        print("Échec de la requête HTTP")

if __name__ == "__main__":
    get_vinted_ads()
