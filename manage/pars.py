import requests
from bs4 import BeautifulSoup

classes = [
    'warrior', 
    'paladin', 
    'hunter', 
    'rogue', 
    'priest', 
    'shaman', 
    'mage', 
    'warlock', 
    'druid', 
    'death-knight'
]


def get_page(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, "html.parser")


def get_pers_data(url):
    pers_data = dict()
    soup = get_page(url)
    pers_data['name'] = soup.find('div', class_='font-semp-xxxLarge-white').text

    pers_data_soup = soup.findAll('div', class_='Grid-full')
    pers_data['desc'] = pers_data_soup[1].findAll('div', class_='gutter-vertical')[1].text

    pers_info = pers_data_soup[1].find('div', class_='gutter-normal').findAll('div', class_='List-item')
    for i in pers_info:
        key = i.find('div').text
        value = i.text[len(key):].lower().split(', ')

        pers_data[key] = value

    pers_data['talant'] = dict()
    talant_info = soup.findAll('div', class_='Talent--gutter')
    for talant in talant_info:
        talant_name = talant.find('div', class_='Talent-name').text
        pers_data['talant'][talant_name] = talant.find('div', class_='Talent-desc').text.replace('\r\n', '')

    return pers_data


def get_info_by_classes():
    return [get_pers_data(f'https://worldofwarcraft.com/ru-ru/game/classes/{i}') for i in classes]
