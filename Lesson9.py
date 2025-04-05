import requests
# responce = requests.get('https://uaserials.pro/films/')
# print(responce.content)
# print(type(responce.content))

# responce = requests.post('https://httpbin.org/get', data='Test data')
# headers = {'h1':'Test title'}
# print(responce.text)


responce = requests.get('https://coinmarketcap.com/')
responce_text = responce.text
responce_parse = responce_text.split("<span>")



for parse_element_1 in responce_parse:
    if parse_element_1.startswith('$'):
        for parse_element_2 in parse_element_1.split('</span>'):
            if parse_element_2.startswith('$') and parse_element_2[1].isdigit():
                print(parse_element_2)







