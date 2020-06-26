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
    
#df = pd.DataFrame(links)

d = {}

l = 0

df = []

def insert(d):
    d_copy = d.copy()
    df.append(d_copy)
    d = {}

for link in links:
    r = requests.get(link)
    soup = BeautifulSoup(r.content)
    data = soup.find("div" , {"class" : "_2GNeiG _2t27J6"})
    if data is None:
        data = soup.find("div" , {"class" : "_2GNeiG"})
        
    rows = data.find_all("div" , {"class" : "row"})
    for i in rows:
        n = i.find("div" , {"class" : "col col-3-12 _1kyh2f"})
        v = i.find("div" , {"class" : "col col-9-12 _1BMpvA"})
        d[n.text] = v.text
    insert(d)   

print(data)

import json
with open('details.json', 'w') as fout:
    json.dump(df , fout)