#!/usr/bin/python
# -*- coding: latin-1 -*-
import requests
import json
import os
from bs4 import BeautifulSoup

# pip install virtualenv
# source venv/bin/activate
# pip3 install -r requirements.txt

url = 'http://www.dsp-mostaganem.dz/index.php/en/using-joomla/extensions/components/content-component/article-categories/153-liste-medecins-sepcialistes'

BASE_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
CSV_FILE = os.path.join(BASE_DIRECTORY, 'data_csv.csv')
JSON_FILE = os.path.join(BASE_DIRECTORY, 'data_json.json')


data_json = []
data_csv = "Specialite, Nom, Prenom, Adresse, Commune, Telephone\n"

req2 = requests.get(url)
soup2 = BeautifulSoup(req2.text, 'html.parser')


table = soup2.find("table", {"class": "tabelle separate"})
# print(table)
field = table.findAll("td", {"class": "zelle"})
doctors = len(field)//10
print("doctors\n", doctors)

data = {}


count = 0
for doctor in range(doctors):
    count += 1

    print(count)
    # print(field[doctor].text)

    if count == 1:
        # print('specialte = ', field[doctor].text)
        data["Specialite"] = field[doctor].text
    elif count == 2:
        # print('nome = ', field[doctor].text)
        data["Nom"] = field[doctor].text
    elif count == 3:
        # print('Prenom = ', field[doctor].text)
        data["Prenom"] = field[doctor].text
    elif count == 4:
        # print('Adresse = ', field[doctor].text)
        data["Adresse"] = field[doctor].text
    elif count == 5:
        # print('Commune = ', field[doctor].text)
        data["Commune"] = field[doctor].text
    elif count == 6:
        # print('Telephone = ', field[doctor].text)
        data["Telephone"] = field[doctor].text

        count = 0
        print('data = \n', data)
        # data_json.append(data)

        data_json += [{"Specialite": data["Specialite"],
                       "Nom": data["Nom"],
                       "Prenom": data["Prenom"],
                       "Adresse": data["Adresse"],
                       "Commune": data["Commune"],
                       "Telephne": data["Telephone"]
                       }]
        data.clear()

print("data_json = \n", data_json)

with open(JSON_FILE, 'w') as json_f:
    json_f.write(json.dumps(data_json, indent=4)+'\n')
