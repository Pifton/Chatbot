import requests
from bs4 import BeautifulSoup

def scraper(url):
    # Faire la requête GET vers l'URL
    response = requests.get(url)
    
    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Analyser le contenu HTML de la page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Scraping du titre
        title = soup.find('h1', id='page-title').text.strip()
        print("Aliment:",title)
        
        # Scraping des portions
        portions = soup.find('span', class_='portion').text.strip()
        print("Quantité:",portions)
        
        # Scraping des détails de valeurs
        details = soup.find('div', class_='details-valeurs')
        #print(details)
        if details:
            for detail in details.find_all('p'):
               text = detail.get_text(strip=True)
               if "s" in text:
                    key, value = text.split('s')
                    print(f"{key}s: {value}")
               elif ")" in text:
                    key, value = text.split(')')
                    print(f"{key}): {value}")
               elif "cool" in text:
                    key, value = text.split('cool')
                    print(f"{key}cool: {value}")
               elif "u" in text:
                    key, value = text.split('u')
                    print(f"{key}u: {value}")
# Exemple d'utilisation
url = "https://www.lanutrition.fr/eperlan"
scraper(url)
