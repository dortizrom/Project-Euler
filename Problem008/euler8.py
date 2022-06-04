from bs4 import BeautifulSoup
import requests

url = 'https://projecteuler.net/problem=8'

request = requests.get(url)
html_text = request.text

soup = BeautifulSoup(html_text,features="html.parser")


number = ''
for line in soup.find_all('br'):
    number = number + line.text.replace("\n","")

#print(number)



num = 13
vals = []
list = [int(a) for a in number]

for pos in range(0, len(number)-num):
    mult=1
    for k in list[pos:pos+num]:
        mult=mult*k
    vals.append(mult)
    
print(max(vals))
