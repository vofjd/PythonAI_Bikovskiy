# from bs4 import BeautifulSoup
# import requests
# response = requests.get("https://coinmarketcap.com/")
# if response.status_code == 200:
#     soup = BeautifulSoup(response.text,features="html.parser")
#     soup_list = soup.find_all("a", {"href": "/currencies/bitcoin/#markets"})
#     res = soup_list[0]
#     print(res.text)

print("------------------Фільми які зараз Доступні для перегляду------------------")
from bs4 import BeautifulSoup
import requests

url = "https://uaserials.pro/films/"

r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")
soup_list_name = soup.find_all('div',{"class":"th-title truncate"})
name_list = []
for i in soup_list_name:
    name_list.append(i.text)
    print(i.text)


f = open('film.txt', 'w', encoding='utf-8' )
for film in name_list:
    f.write(f"{film}\n")
f.close()