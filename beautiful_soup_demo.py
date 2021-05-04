import requests
from bs4 import BeautifulSoup
import pandas as pd

# get the data
url = 'https://en.wikipedia.org/wiki/List_of_Formula_One_Grand_Prix_winners'
data = requests.get(url)

# load data into bs4

soup = BeautifulSoup(data.text, 'html.parser')

table = soup.find('table', {'class':'sortable plainrowheaders wikitable'}).tbody
rows = table.find_all('tr')
columns = [v.text.replace('\n', '') for v in rows[0].find_all('th')]

df = pd.DataFrame(columns = columns)

for i in range(1, len(rows)):
    tds = rows[i].find_all(['td','th'])
    values = [tds[0].text.replace('\n', '').replace('\xa0', ''), tds[1].text.replace('\n', '').replace('\xa0', ''), tds[2].text.replace('\n', '').replace('\xa0', ''), tds[3].text.replace('\n', ''.replace('\xa0', '')), tds[4].text.replace('\n', ''.replace('\xa0', '')), tds[5].text.replace('\n', ''.replace('\xa0', '')), tds[6].text.replace('\n', ''.replace('\xa0', ''))]

    df = df.append(pd.Series(values, index=columns), ignore_index=True)

df.to_csv('test.csv')