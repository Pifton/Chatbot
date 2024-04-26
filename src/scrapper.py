import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import pickle

def get_links_from_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        links = set()  # Utiliser un ensemble pour éviter les doublons
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extraire tous les liens de la page
            for link in soup.find_all('a', href=True):
                absolute_link = urljoin(url, link['href'])
                parsed_link = urlparse(absolute_link)
                # Ignorer les liens qui ne commencent pas par le préfixe spécifié
                if absolute_link.startswith("https://www.lanutrition.fr/") and len(parsed_link.path.split('/')) <= 2 and not parsed_link.fragment:
                    links.add(absolute_link)
        return links
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {url}. {e}")
        return set()


def scraper(url):
    # Faire la requête GET vers l'URL
     response = requests.get(url)
    
    # Vérifier si la requête a réussi
     if response.status_code == 200:
        # Analyser le contenu HTML de la page
          soup = BeautifulSoup(response.text, 'html.parser')
          details = soup.find('div', class_='details-valeurs')
          if details:
               # Scraping du titre
               title = soup.find('h1', id='page-title')
               if title:
                    title = title.text.strip()
                    file.write(f"Aliment: {title}\n")
                    #print("Aliment:", title)
               
               # Scraping des portions
               portions = soup.find('span', class_='portion')
               if portions:
                    portions = portions.text.strip()
                    file.write(f"Quantité: {portions}\n")
                    #print("Quantité:", portions)
               
               # Scraping des détails de valeurs
               #print(details)
               for detail in details.find_all('p'):
                    text = detail.get_text(strip=True)
                    if "Protéines" in text:
                         key, value = text.split('s')
                         file.write(f"{key}s: {value}\n")
                         #print(f"{key}s: {value}")
                    elif "Lipides" in text:
                         key, value = text.split('s')
                         file.write(f"{key}s: {value}\n")
                         #print(f"{key}s: {value}")
                    elif "Glucides" in text:
                         key, value = text.split('s')
                         file.write(f"{key}s: {value}\n")
                         #print(f"{key}s: {value}")
                    elif "Fibres" in text:
                         key, value = text.split('s')
                         file.write(f"{key}s: {value}\n")
                         #print(f"{key}s: {value}")
                    elif "kCal)" in text:
                         key, value = text.split(')')
                         file.write(f"{key}): {value}\n")
                         #print(f"{key}): {value}")
                    elif "cool" in text:
                         key, value = text.split('cool')
                         file.write(f"{key}cool: {value}\n")
                         #print(f"{key}cool: {value}")
                    elif "Eau" in text:
                         key, value = text.split('u')
                         file.write(f"{key}u: {value}\n")
                         #print(f"{key}u: {value}")
          else:
               print(f"No details found for: {url}")
          file.write("\n")
          file.write("-------------------\n\n")


# URL de départ
start_url = "https://www.lanutrition.fr/les-aliments-a-la-loupe"

filename = "../data/scrapped.txt"
#with open(filename,"w") as file:
file = open(filename,"w")

# Obtenir les liens de la page de départ
links_from_start_page = get_links_from_page(start_url)
#print(links_from_start_page)
test = 0
#scrappe toutes les données nécéssaires
for liens in links_from_start_page:
     scraper(liens)
     test += 1
     print(test," | ",liens)
print("Toutes les données ont été extraites avec succès dans le fichier texte !")


""" if isinstance(links_from_start_page, str):
     print("yes")
else:
     print("no")
print(type(links_from_start_page))
#print(links_from_start_page)
#url = links_from_start_page.get_text(strip=True)
#scraper(url)

#print(len(links_from_start_page)) """
