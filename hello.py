import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import pickle

# Fonction pour obtenir les liens à partir d'une page
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

# Fonction pour enregistrer les URL dans un fichier
def save_visited_urls(urls, filename):
    with open(filename, 'wb') as file:
        pickle.dump(urls, file)

# Fonction pour charger les URL à partir d'un fichier
def load_visited_urls(filename):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except (FileNotFoundError, EOFError):
        return set()

# Fonction pour trouver les pages avec un chemin spécifié
def find_pages_with_path(start_url, path_prefix, visited_urls_filename):
    visited_urls = load_visited_urls(visited_urls_filename)
    to_visit = {start_url}
    relevant_pages = set()
    test = 0

    while to_visit:
        current_url = to_visit.pop()
        visited_urls.add(current_url)

        # Vérifier si l'URL contient le chemin souhaité
        if path_prefix in current_url:
            relevant_pages.add(current_url)

        # Obtenir les liens de la page actuelle
        links = get_links_from_page(current_url)

        # Ajouter les nouveaux liens à visiter
        for link in links:
            if link not in visited_urls and "bien-etre" not in link:
                to_visit.add(link)

        # Enregistrer les URL visités en cas de plantage
        save_visited_urls(visited_urls, visited_urls_filename)

        test = test +1
        print(test)

        # Pause de 0.5 seconde

    return relevant_pages

# URL de départ
start_url = "https://www.lanutrition.fr/les-aliments-a-la-loupe"

# Préfixe de chemin souhaité
path_prefix = "https://www.lanutrition.fr/"

# Nom du fichier pour enregistrer les URL visités
visited_urls_filename = "visited_urls.txt"

# Trouver toutes les pages contenant le préfixe de chemin spécifié
relevant_pages = find_pages_with_path(start_url, path_prefix, visited_urls_filename)

# Afficher les pages trouvées
print("Pages pertinentes:", relevant_pages)

# Supprimer le fichier des URL visités une fois que le programme a terminé avec succès
if len(relevant_pages) > 0:
    try:
        os.remove(visited_urls_filename)
    except FileNotFoundError:
        pass
