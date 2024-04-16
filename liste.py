# list.py
import pickle

# Fonction pour charger les URL à partir d'un fichier
def load_visited_urls(filename):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except (FileNotFoundError, EOFError):
        return set()

# Chargement des URLs visités depuis le fichier
visited_urls_filename = "test.txt"
visited_urls = load_visited_urls(visited_urls_filename)

# Création d'un ensemble pour stocker les URLs uniques et un autre pour les doublons
unique_urls = set()
duplicate_urls = set()

# Comparaison des URLs pour détecter les doublons
for url in visited_urls:
    if url in unique_urls:
        duplicate_urls.add(url)
    else:
        unique_urls.add(url)

# Affichage des URLs uniques
print("URLs uniques :")
for url in unique_urls:
    print(url)

# Affichage des URLs en double
print("\nURLs en double :")
for url in duplicate_urls:
    print(url)

# Affichage du nombre d'URLs différentes
print("\nNombre d'URLs différentes :", len(unique_urls))
