import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

major_dictionary = {}

for i in range(100, 200):
    source = urllib.request.urlopen(f'https://major-system.info/en/?n={i}').read()
    soup = BeautifulSoup(source,'lxml')
    body = soup.body

    for paragraph in body.find_all('div', {'id': 'response'}):
        list_of_words = paragraph.text.split()
        print(i)
        major_dictionary[i] = list_of_words


df = pd.DataFrame.from_dict(major_dictionary, orient='index')
df.to_csv('major_dictionary.csv')

df = pd.read_csv('major_dictionary.csv', index_col=0)

d = df.to_dict('split')
d = dict(zip(d['index'], d['data']))