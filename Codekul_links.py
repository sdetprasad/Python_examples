from bs4 import BeautifulSoup
import requests
import sys

url = "http://www.codekul.com/"

response = None

try:
    response = requests.get(url)
except Exception as e:
    print(repr(e))
    sys.exit(1)

if response.status_code != 200:
    print("Non success status code returned "+str(response.status_code))
    sys.exit(1)

soup = BeautifulSoup(response.text,'html.parser')

links = soup.find_all("a",{"class":"menu_items"})

menulist = []
for link in links:
    text = link.text.encode('utf-8')
    menulist.append(text)

for linktext in menulist:
    print(linktext)

