import xml.etree.ElementTree as ET

# Fonction pour extraire les aliments par type et les enregistrer dans un fichier texte
def extraire_aliments_par_type(fichier_xml, fichier_txt):
    # Analyse du fichier XML
    tree = ET.parse(fichier_xml)
    root = tree.getroot()

    # Dictionnaire pour stocker les aliments par type
    aliments_par_type = {}

    # Parcours de tous les éléments aliment dans le fichier XML
    for aliment in root.findall('.//aliment'):
        nom_aliment = aliment.find('nom').text
        type_aliment = aliment.get('type')

        # Ajout de l'aliment au type correspondant dans le dictionnaire
        if type_aliment in aliments_par_type:
            aliments_par_type[type_aliment].append(nom_aliment)
        else:
            aliments_par_type[type_aliment] = [nom_aliment]

    # Écriture des aliments par type dans le fichier texte
    with open(fichier_txt, 'w', encoding='utf-8') as f:
        for type_aliment, aliments in aliments_par_type.items():
            f.write(f"{type_aliment}:\n")
            f.write("       ")
            count = 0
            for aliment in aliments:
                f.write(f"{aliment}, ")
                count += 1
                if count % 15 == 0:  # Ajoute un saut de ligne toutes les 15 aliments
                    f.write("\n       ")
            f.write("\n")

# Nom des fichiers
fichier_xml = 'aliments.xml'
fichier_txt = 'aliments_par_type.txt'

# Extraction des aliments par type
extraire_aliments_par_type(fichier_xml, fichier_txt)

print("Les aliments par type ont été extraits avec succès dans le fichier texte !")
