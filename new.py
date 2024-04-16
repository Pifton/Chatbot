import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import pickle

# Fonction pour obtenir les liens à partir d'une page
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

# URL de départ
start_url = "https://www.lanutrition.fr/les-aliments-a-la-loupe"

filename = "links.txt"

# Obtenir les liens de la page de départ
links_from_start_page = get_links_from_page(start_url)

# Enregistrer les liens dans un fichier texte


with open(filename, 'wb') as file:
        pickle.dump(links_from_start_page, file)


# Afficher les liens de la page de départ
for link in links_from_start_page:
    print(link)

value = len(links_from_start_page)
print(value)