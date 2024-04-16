import requests
from bs4 import BeautifulSoup

def scraper(url, output_file):
    # Faire la requête GET vers l'URL
    response = requests.get(url)
    
    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Analyser le contenu HTML de la page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Scraping des balises <span class="portion">
        portions = soup.find_all('span', class_='portion')
        with open(output_file, 'a', encoding='utf-8') as file:
            file.write("Portions:\n")
            for portion in portions:
                file.write(portion.text + "\n")
        
        # Scraping des balises <div class="details-valeurs">
        details = soup.find_all('div', class_='details-valeurs')
        with open(output_file, 'a', encoding='utf-8') as file:
            file.write("\nDétails:\n")
            for detail in details:
                file.write(detail.text + "\n")
                
        print("Données extraites avec succès et enregistrées dans", output_file)
    else:
        print("La requête a échoué.")

# Exemple d'utilisation
url = "https://www.lanutrition.fr/"
output_file = "donnees_extraites.txt"
scraper(url, output_file)
