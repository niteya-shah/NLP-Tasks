import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
temp_datastore=list()
url = 'http://hindi.webdunia.com/ram-navmi-special/ramayana-117040100054_1.html'
r=requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

for text in soup.findAll('div'):
    w=text.findAll(text=True)
    if(len(w)>0):
        temp_datastore.append(w)

temp_datastore
