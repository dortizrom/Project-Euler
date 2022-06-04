# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 21:46:32 2020

@author: dorti
"""

from bs4 import BeautifulSoup
import requests

url = 'https://projecteuler.net/problem=13'

r = requests.get(url)

html = r.text

soup = BeautifulSoup(html, features="lxml")

values = soup.find_all('div', attrs={"class":"monospace center"})
    

for desempaque in values:
    num_str = desempaque.text.replace('\n', "")

num_list = [int(num_str[i:i+50]) for i in range(0,5000,50)]

suma = sum(num_list)

ten_first_digits = str(suma)[0:10]

print(ten_first_digits)