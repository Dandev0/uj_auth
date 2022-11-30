import time

import requests
from bs4 import BeautifulSoup


def main():
    session = requests.session()
    url = 'https://api-product.mysmartflat.ru/api/v1/pub/admin/login'
    token = session.get(url)
    soup = BeautifulSoup(token.text, "lxml")
    a = soup.find('input')['value']
    print(a)
    print(token.status_code)
    url_login = 'https://api-product.mysmartflat.ru/api/v1/pub/admin/login'
    data = {
        "_token": a,
        "login": "koksharov@ujin.tech",
        "password": "unemufyfut"
    }
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    auth = session.post(url_login, data=data, headers=headers)
    # print(auth.status_code)
    # print(auth.text)
    search_number_url = 'https://api-product.mysmartflat.ru/api/v1/pub/admin/users/search?search=79824911582'
    number = session.get(search_number_url)
    # print(number.status_code)
    # print(number.text)
    url3 = 'https://api-product.mysmartflat.ru/api/v1/pub/admin/users/generateOTP?user_id=1631635'
    passw = session.get(url3)
    print(passw.text)
    a = soup.find('input', {"class":"form-control", "type": "password"})["required"]
    print(f"Пароль: {a}")




    # print(soup.find_all('input'))

if __name__ == '__main__':
    main()