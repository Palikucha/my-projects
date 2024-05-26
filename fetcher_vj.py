#treba napisati funkciju koja će sa web stranice https://coinmarketcap.com/ dohvatiti nazive i iznose prvih 10 kriptovaluta
# potrebno je podatke o pojedinoj kriptovaluti čuvati u objektu klase koja će imati dva atributa (name, price)

import requests
from bs4 import BeautifulSoup




class Cryptocurrency:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'{self.name}: {self.price}'

def fetch_crypto():
    url = "https://coinmarketcap.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    rows = soup.find_all('tr'[:10], class_='cmc-table-row')
    print(rows)

    cryptos = []
    for i in range(10):
        name = soup.find_all('p', class_='sc-1eb5slv-0 iJjGCS')[i].get_text()
        price = soup.find_all('a', class_='cmc-link')[i].get_text()
        cryptos.append(Cryptocurrency(name, price))

    return cryptos

if __name__ == "__main__":
    cryptos = fetch_crypto()
    for crypto in cryptos:
        print(crypto)