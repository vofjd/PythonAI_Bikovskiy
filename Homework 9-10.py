from bs4 import BeautifulSoup
import requests

print("----------Exchange Rate in the National Bank Of Ukraine----------")

url = "https://bank.gov.ua/en/markets/exchangerates"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")


soup_list_letter_code = soup.find_all('td', {"data-label": "Letter code"})
soup_list_currency_name = soup.find_all('td', {"data-label": "Currency name"})
soup_list_value = soup.find_all('span', {"class": "value"})
soup_list_uah = soup.find_all('td', {"data-label": "UAH"})

print("Letter code      Currency name       Official exchange rate (UAH)")


for letter_code, currency_name, rate in zip(soup_list_letter_code, soup_list_currency_name, soup_list_uah):
    print(f"{letter_code.text.strip():<13} {currency_name.text.strip():<35} {rate.text.strip()}")


