import re
from xml.sax.saxutils import escape 

# Fonction pour lire les données à partir du fichier texte
def lire_donnees(fichier_texte):
     with open(fichier_texte, 'r', encoding='utf-8') as f:
          donnees = f.read()
     return donnees

# Fonction pour attribuer un type à l'aliment en fonction de son nom
def determiner_type_aliment(nom_aliment):
    types = {
        'fruit': ['pêche', 'fraise', 'banane', 'pomme', 'orange', 'raisin', 'cerise', 'poire', 'grenade', 'mangue',
                  'ananas', 'kiwi', 'melon', 'papaye', 'framboise', 'myrtille', 'groseille'],
        'spice': ['paprika', 'curry', 'cumin', 'cannelle', 'muscade', 'gingembre', 'safran', 'poivre', 'cardamone',
                  'coriandre', 'curcuma', 'anis'],
        'sauce': ['mornay', 'béarnaise', 'hollandaise', 'tomate', 'barbecue', 'vinaigrette', 'mayonnaise', 'soja',
                  'pesto', 'sriracha', 'hoisin'],
        'meat': ['bison', 'boeuf', 'poulet', 'agneau', 'porc', 'canard', 'cheval', 'lapin', 'bœuf', 'veau', 'dinde',
                 'gibier'],
        'vegetables': ['carotte', 'tomate', 'brocoli', 'épinard', 'concombre', 'poivron', 'courgette','pomme de terre',
                       'courge', 'aubergine', 'asperge', 'radis', 'chou-fleur', 'haricot vert' ],
        'nuts': ['amande', 'noisette', 'noix', 'pistache', ],
        'dairys': ['lait', 'fromage', 'yaourt', 'beurre', 'crème', 'kéfir'],
        'eggs': ['œuf', 'omelette', 'frittata', 'soufflé', 'meringue'],
        'seafood': ['crevette', 'saumon', 'thon', 'huître', 'moule', 'crabe', 'homard', 'calamar', 'palourde', 'langouste',
                    'saint-Jacques', 'anguille'],
        'cereals': ['blé', 'riz', 'maïs', 'avoine', 'quinoa', 'millet', 'épeautre', 'sarrasin', 'seigle', 'orge', 'boulgour',
                    'pâtes'],
        'boisson': ['eau', 'jus', 'café', 'thé']
    }

     # Liste des préfixes à ignorer
    prefixes_a_ignorer = ['au ', 'à ', 'aux']

    # Convertir le nom de l'aliment en minuscules pour la correspondance insensible à la casse
    nom_aliment_lower = nom_aliment.lower()

    elements_present = set()

    for element in types.values():
        #print(types.values())
        #print(element)
        for item in element:
            #print(item)
            if item in nom_aliment_lower:
                elements_present.add(item)
                #print(elements_present)
          
      # Vérifiez si un élément contient un autre
    for element1 in elements_present:
        #print(element1)
        for element2 in elements_present:
            #print(element2)
            if element1 != element2 and element1 in element2:
               print(element2)
               for key, values in types.items():
                    if element2 in values:
                        print(f"Type de l'élément : {key}")
                        return key

    # Si aucun élément ne contient un autre, retourner simplement un élément présent dans le nom
    if elements_present:
        return elements_present.pop()

    return 'autre'

# Fonction pour créer le fichier XML
def creer_fichier_xml(donnees, fichier_xml):
     with open(fichier_xml, 'w', encoding='utf-8') as f:
          f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
          f.write('<Aliments>\n\n')
          aliments = re.split(r'\n-{5,}\n', donnees)
          for aliment in aliments:
               if aliment.strip():
                    
                    # Recherche et écriture des données
                    nom_aliment = re.search(r'Aliment: (.+)', aliment).group(1)
                    type_aliment = determiner_type_aliment(nom_aliment)
                    nom_aliment = escape(nom_aliment)  # Remplacer l'apostrophe par &apos;
                    f.write('    <aliment type="{}">\n'.format(type_aliment))
                    f.write('        <nom>{}</nom>\n'.format(nom_aliment))

                    """ portion_aliment = re.search(r'Quantité: (.+)', aliment)
                    f.write('        <portion>{}</portion>\n'.format(portion_aliment.group(1)))

                    calories_aliment = re.search(r'Energie \(kCal\): (.+)', aliment)
                    if calories_aliment:
                         f.write('        <calories>{}</calories>\n'.format(calories_aliment.group(1)))

                    glucides_aliment = re.search(r'Glucides: (.+)', aliment)
                    if glucides_aliment:
                         f.write('        <glucides>{}</glucides>\n'.format(glucides_aliment.group(1)))

                    protein_aliment = re.search(r'Protéines: (.+)', aliment)
                    if protein_aliment:
                         f.write('        <proteins>{}</proteins>\n'.format(protein_aliment.group(1)))

                    lipides_aliment = re.search(r'Lipides: (.+)', aliment)
                    if lipides_aliment:
                         f.write('        <lipides>{}</lipides>\n'.format(lipides_aliment.group(1)))

                    fibres_aliment = re.search(r'Fibres: (.+)', aliment)
                    if fibres_aliment:
                         f.write('        <fibres>{}</fibres>\n'.format(fibres_aliment.group(1))) """


                    portion_aliment_match = re.search(r'Quantité: (.+)', aliment)
                    portion_aliment = portion_aliment_match.group(1) if portion_aliment_match else ''
                    f.write('        <portion>{}</portion>\n'.format(portion_aliment))

                    calories_aliment_match = re.search(r'Quantité: (.+)', aliment)
                    calories_aliment = calories_aliment_match.group(1) if calories_aliment_match else ''
                    f.write('        <calories>{}</calories>\n'.format(calories_aliment))

                    protein_aliment_match = re.search(r'Protéines: (.+)', aliment)
                    protein_aliment = protein_aliment_match.group(1) if protein_aliment_match else ''
                    f.write('        <proteins>{}</proteins>\n'.format(protein_aliment))

                    lipides_aliment_match = re.search(r'Lipides: (.+)', aliment)
                    lipides_aliment = lipides_aliment_match.group(1) if lipides_aliment_match else ''
                    f.write('        <lipides>{}</lipides>\n'.format(lipides_aliment))

                    glucides_aliment_match = re.search(r'Glucides: (.+)', aliment)
                    glucides_aliment = glucides_aliment_match.group(1) if glucides_aliment_match else ''
                    f.write('        <glucides>{}</glucides>\n'.format(glucides_aliment))

                    fibres_aliment_match = re.search(r'Fibres: (.+)', aliment)
                    fibres_aliment = fibres_aliment_match.group(1) if fibres_aliment_match else ''
                    f.write('        <fibres>{}</fibres>\n'.format(fibres_aliment))


                    f.write('    </aliment>\n\n')
          f.write('</Aliments>')

# Nom des fichiers
fichier_texte = 'main.txt'
fichier_xml = 'main.xml'

# Lecture des données du fichier texte
donnees = lire_donnees(fichier_texte)

# Création du fichier XML
creer_fichier_xml(donnees, fichier_xml)

print("Le fichier XML a été créé avec succès !")
