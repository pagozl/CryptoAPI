from urllib import request
import json

response = request.urlopen('https://financialmodelingprep.com/api/v3/cryptocurrencies')

obj = json.load(response)
crname = input("Podaj nazwe kryptowaluty (np. Bitcoin, Maker, Dogecoin): ")
found=0

for x in obj['cryptocurrenciesList']:
    if x['name'] == crname:
        print("Cena", crname, "to", x['price'], "USD")
        found=1

if found==0:
    print("Niepoprawna nazwa kryptowaluty. Lista dostępnych kryptowalut:")
    for x in obj['cryptocurrenciesList']:
        print(x['name'])