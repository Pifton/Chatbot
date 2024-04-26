import xml.etree.ElementTree as ET
import csv

# Fonction pour extraire les informations d'un élément aliment
def extract_aliment_info(aliment):
    nom = aliment.find('nom').text
    portion = aliment.find('portion').text.replace('g', '')
    calories = aliment.find('calories').text.replace(' kCal', '') if aliment.find('calories').text is not None else '0'
    proteins = aliment.find('proteins').text.replace(' g', '') if aliment.find('proteins').text is not None else '0'
    lipides = aliment.find('lipides').text.replace(' g', '') if aliment.find('lipides').text is not None else '0'
    glucides = aliment.find('glucides').text.replace(' g', '') if aliment.find('glucides').text is not None else '0'
    fibres = aliment.find('fibres').text.replace(' g', '') if aliment.find('fibres').text is not None else '0'
    aliment_type = aliment.attrib.get('type', 'autre')  # Type d'aliment
    return nom, aliment_type, portion, calories, proteins, lipides, glucides, fibres

# Charger le fichier XML
tree = ET.parse('aliments.xml')
root = tree.getroot()

# Ouvrir un fichier CSV en mode écriture
with open('../data/aliments.csv', 'w', newline='', encoding='utf-8') as csvfile:
    # Créer un objet writer CSV
    csvwriter = csv.writer(csvfile)
    
    # Écrire l'en-tête du CSV
    csvwriter.writerow(['nom', 'type', 'portion', 'calories', 'proteins', 'lipides', 'glucides', 'fibres'])
    
    # Parcourir tous les éléments 'aliment' dans le fichier XML
    for aliment in root.findall('aliment'):
        # Extraire les informations de l'aliment
        nom, portion, calories, proteins, lipides, glucides, fibres, aliment_type = extract_aliment_info(aliment)
        
        # Écrire les informations dans le fichier CSV
        csvwriter.writerow([nom, portion, calories, proteins, lipides, glucides, fibres, aliment_type])

print("Conversion XML vers CSV terminée.")
