import requests
from bs4 import BeautifulSoup
import csv
# change to whatever your url is
url = "https://www.w3schools.com/html/html_tables.asp"

outfile = open("table_data.csv", "w", newline='')
writer = csv.writer(outfile)

page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

# tables = soup.findAll("table", {"id": "customers"})

# print(tables)

tree = BeautifulSoup(page.text, "lxml")
table_tag = tree.select("table")[0]
tab_data = [[item.text for item in row_data.select("th,td")]
            for row_data in table_tag.select("tr")]

for data in tab_data:
    writer.writerow(data)
    print(' '.join(data))
