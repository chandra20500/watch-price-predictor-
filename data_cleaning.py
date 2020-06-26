import json
with open('details.json') as f:
    json_data = json.load(f)

#extracting price

import requests
url = 'https://www.flipkart.com/amp/watches/fastrack~brand/pr?otracker=nmenu_sub_Men_0_Fastrack&sid=r18&start=300'
import pandas as pd
from bs4 import BeautifulSoup

links = []

r = requests.get(url)
soup = BeautifulSoup(r.content)
data = soup.find_all("div", {"class":"_1jJGh"})
for i in data:
    link = i.find_all('a')
    for j in link:
        links.append(j.get('href'))
        
cost = []

for link in links:
    r = requests.get(link)
    soup = BeautifulSoup(r.content) 
    price = soup.find("div", {"class":"_1vC4OE _3qQ9m1"})
    cost.append(price.text)

#backup storage    
real = []
real = cost

#extracting variables

water_resistant = []
Display_type = []
strap_material = []
box_material = []
Diameter = []
occasion = []
series = []
strap_type = []
thickness = []
weight = []
width = []

for i in json_data:
    water_resistant.append(i['Water Resistance Depth'])
    
for i in json_data:
    Display_type.append(i['Display Type'])
    
for i in json_data:
    strap_material.append(i['Strap Material'])

for i in json_data:
    box_material.append(i['Box Material'])
    
for i in json_data:
    Diameter.append(i['Diameter'])
    
for i in json_data:
    occasion.append(i['Occasion'])
    
for i in json_data:
    series.append(i['Series'])
    
for i in json_data:
    strap_type.append(i['Strap Type'])
    
for i in json_data:
    thickness.append(i['Thickness'])
    
for i in json_data:
    weight.append(i['Weight'])
    
for i in json_data:
    width.append(i['Width'])
    
    
df = pd.DataFrame(columns = ['water_resistant', 'Display_type',
                                  'strap_material', 'box_material', 
                                  'Diameter', 'occasion',
                                  'series', 'strap_type', 'thickness',
                                  'weight','width','price'])
df['water_resistant'] = water_resistant
df['Display_type'] = Display_type
df['strap_material'] = strap_material
df['box_material'] = box_material
df['Diameter'] = Diameter
df['occasion'] = occasion
df['series'] = series
df['strap_type'] = strap_type
df['thickness'] = thickness
df['weight'] = weight
df['width'] = width
df['price'] = cost

df.to_csv("dataset.csv") 
