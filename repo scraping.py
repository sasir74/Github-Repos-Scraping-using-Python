import requests
import csv
from bs4 import BeautifulSoup
 
url = input('Enter the url  :  ')
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

li = soup.findAll('div', class_="d-inline-block mb-1")

with open('output.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Repo Name', 'Repo Link', 'Name']) 
    for i in li:
        for a in i.findAll('a'):
            repo_name = i.text.strip()
            repo_link = url + a["href"]
            name = repo_name[0:6]
 
        print( repo_name , repo_link , name )
        writer.writerow([repo_name , repo_link , name])
 
f.close()
