import json
import requests
from bs4 import BeautifulSoup
url = "http://localhost/web/newlead.html"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
nametag = soup.find("font", class_="font16")
name = nametag.find("strong", class_="")
Name = name.text
anc = soup.find_all("a", class_="")
anchortags = []
for a in anc:
    tags = a.text
    anchortags.append(tags)
#Our required tags are : anchortags[3], anchortags[4], anchortags[7],
Phone = anchortags[3]
Email = anchortags[4]
Address = anchortags[7]
output = {
    'Name': Name,
    'Phone' : Phone ,
    'Email' : Email,
    'Address' : Address

}
j = json.dumps(output)
with open('output.json', 'w') as f:
    f.write(j)
    f.close()

#Printing the information
print(output)

