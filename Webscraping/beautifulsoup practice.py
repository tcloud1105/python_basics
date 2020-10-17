import requests
from bs4 import BeautifulSoup

r=requests.get("http://pythonhow.com/example.com")
c=r.content

soup = BeautifulSoup(c,'html.parser')
print(soup.prettify())

all=soup.find_all("div", {"class":"cities"})
names=[]
for tag in all:
    names.append(tag.find("h1").text)
