#!/usr/bin/env python

from requests import get
from bs4 import BeautifulSoup
from array import array
from re import compile
from colorama import Fore, Style
from sys import argv

#url = 'https://www.boursorama.com/cours/1rPKORI/'
#url = 'https://www.boursorama.com/cours/1rPVK/'
url = argv[1]

MyArray = []
MyPct = []

response = get(url)
# print(response.text[:1500])

html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)

today_stock_name = html_soup.find('a', class_ ="c-faceplate__company-link")
today_value_container = html_soup.find_all('td', class_ = 'c-table__cell c-table__cell--dotted c-table__cell--tiny')
#today_percentage_container = html_soup.find_all('td', class_ = 'c-table__cell c-table__cell--dotted c-table__cell--positive c-table__cell--tiny')
today_percentage_container = html_soup.find_all('td', class_ = compile('c-table__cell c-table__cell--dotted c-table__cell--.* c-table__cell--tiny'))
#today_percentage_container = html_soup.find_all('td', class_ = 'c-table__cell c-table__cell--head c-table__cell--dotted c-table__title / u-text-uppercase')

stock_name = today_stock_name.text.strip()

for row in today_value_container:          # Print all occurrences
  x = row.get_text()
  y = x.strip()
  MyArray.append(y)


for row in today_percentage_container:
  x = row.get_text()
  y = x.strip()
  MyPct.append(y)

Der = MyArray[4]
Var = MyPct[4]
Ouv = MyArray[9]
Haut = MyArray[13]
Bas = MyArray[18]

if float(Var.strip('%')) < 0:
  print ("%-20s %12s %12s %12s %8s %8s" % (Style.BRIGHT + stock_name, Style.RESET_ALL + Der, Fore.RED + Var, Fore.WHITE + Ouv, Haut, Bas))
else:
  print ("%-20s %12s %12s %12s %8s %8s" % (Style.BRIGHT + stock_name, Style.RESET_ALL + Der, Fore.GREEN + Var, Fore.WHITE + Ouv, Haut, Bas))
