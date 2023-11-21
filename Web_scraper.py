from bs4 import BeautifulSoup
import requests
import csv

# URL to be scraped
URL = 'https://apewisdom.io/all-crypto/'

# Make a GET request to fetch the raw HTML content and clean it.

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
cripto = soup.find_all('div', class_='company-name')
criptos = str(cripto)
criptos = criptos.replace('<div class="company-name">', '|')
criptos = criptos.replace('</div>,', '')
criptos = criptos.replace('<[', '')
criptos = criptos.replace('</div>]', '')
critptoclean = criptos.split('|')  #We use this line to create a list using the | as a separator
critptoclean.pop(0)  #An extra item got added to the list, so we remove it

#We create a list with the top 10 cryptos
lista = []
for i in range(10):
    lista.append(critptoclean[i])

top_10 = lista
print(lista)

#We sava it to a csv file
with open('reddit.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=",")

    # Write each element as a separate row
    for item in critptoclean:
        writer.writerow([item])
