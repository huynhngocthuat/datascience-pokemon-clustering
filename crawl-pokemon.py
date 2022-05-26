from numpy import spacing
import requests
from bs4 import BeautifulSoup
# link data
link = 'https://pokemondb.net/pokedex/all?fbclid=IwAR1y_ysWgVB58G0D4PSCwnhpcL2KqrKiemPGaPzH82nXnriIGdOTE8h7stw'
# headers tránh các trường hợp k tải được trang
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# open file
f = open("pokemon.csv", "a")
head = "Code,Name,Type 1,Type 2,Total,HP,Attack,Defense,SP Attack,SP Defense,Speed\n"
f.write(head)

# read data from website
response = requests.get(link, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
tr_data = soup.find_all('tr')
for row in tr_data[1:]:
    td_list = row.find_all('td')
    code = td_list[0].find_all('span')[2].text
    name = td_list[1].find_all('a')[0].text.replace("♀", " Male").replace("♂", " Female")    
    if len(td_list[1].find_all('small')) > 0:
        other_name = td_list[1].find_all('small')[0].text
        name = name + "-" + other_name
    if len(td_list[2].find_all('a')) == 2:
        type1 = td_list[2].find_all('a')[0].text
        type2 = td_list[2].find_all('a')[1].text
    elif len(td_list[2].find_all('a')) == 1:
        type1 = td_list[2].find_all('a')[0].text
        type2 = ""
    
    total = td_list[3].text
    hp = td_list[4].text
    attack = td_list[5].text
    defense = td_list[6].text
    sp_attack = td_list[7].text
    sp_defense = td_list[8].text
    speed = td_list[9].text

    # create data save in the file
    data = f"{code},{name},{type1},{type2},{total},{hp},{attack},{defense},{sp_attack},{sp_defense},{speed}\n"
    f.write(data)


f.close()
