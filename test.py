import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

def get_links_from_page(url):
    response = requests.get(url)
    links = set()  # Utiliser un ensemble pour éviter les doublons
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extraire tous les liens de la page
        for link in soup.find_all('a', href=True):
            absolute_link = urljoin(url, link['href'])
            # Ignorer les liens avec un schéma invalide
            if absolute_link.startswith("http://") or absolute_link.startswith("https://"):
                links.add(absolute_link)
    return links

def find_pages_with_path(start_url, path_prefix):
    visited = set()  # Pour éviter les boucles infinies
    to_visit = {start_url}
    relevant_pages = set()
    test = 0

    while to_visit:
        current_url = to_visit.pop()
        visited.add(current_url)

        # Vérifier si l'URL contient le chemin souhaité
        if path_prefix in current_url:
            relevant_pages.add(current_url)

        # Obtenir les liens de la page actuelle
        links = get_links_from_page(current_url)
        
        test = test+1
        print(test) 

        # Ajouter les nouveaux liens à visiter
        for link in links:
            if link not in visited and "bien-etre" not in link:
                to_visit.add(link)

        # Pause de 0.5 seconde
        #time.sleep(0.01)
    return relevant_pages and print("reussi")



# URL de départ
start_url = "https://www.lanutrition.fr/les-aliments-a-la-loupe"

# Préfixe de chemin souhaité
path_prefix = "https://www.lanutrition.fr/"

# Trouver toutes les pages contenant le préfixe de chemin spécifié
relevant_pages = find_pages_with_path(start_url, path_prefix)

# Afficher les pages trouvées
print("Pages pertinentes:" ,relevant_pages)

#for page in relevant_pages:
  #  print(page)
