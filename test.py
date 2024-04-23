import xml.etree.ElementTree as ET

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
        'vegetable': ['carotte', 'tomate', 'brocoli', 'épinard', 'concombre', 'poivron', 'courgette','pomme de terre',
                       'courge', 'aubergine', 'asperge', 'radis', 'chou-fleur', 'haricot vert' ],
        'nuts': ['amande', 'noisette', 'noix', 'pistache', ],
        'dairy': ['lait', 'fromage', 'yaourt', 'beurre', 'crème', 'kéfir', 'féta'],
        'egg': ['œuf', 'omelette', 'frittata', 'soufflé', 'meringue', 'oeuf'],
        'seafood': ['crevette', 'saumon', 'thon', 'huître', 'moule', 'crabe', 'homard', 'calamar', 'palourde', 'langouste',
                    'saint-Jacques', 'anguille', 'éperlan'],
        'cereal': ['blé', 'riz', 'maïs', 'avoine', 'quinoa', 'millet', 'épeautre', 'sarrasin', 'seigle', 'orge', 'boulgour',
                    'pâtes'],
        'boisson': ['eau', 'jus', 'café', 'thé']
    }

    # Liste des préfixes à ignorer
    prefixes_a_ignorer = ['au ', 'à']

    # Liste des lettres à ignorer en fin de mot
    pluriel = ['s', 'x']

    # Convertir le nom de l'aliment en minuscules pour la correspondance insensible à la casse
    nom_aliment_lower = nom_aliment.lower()

    elements_present = set()

    for element in types.values():
        for item in element:
            #print(item)
            # Vérifie si l'élément est dans le nom de l'aliment et si son préfixe n'est pas à ignorer
            if item in nom_aliment_lower and not any(prefix in nom_aliment_lower for prefix in prefixes_a_ignorer):
                if f' {item} ' in f' {nom_aliment_lower} ': 
                    elements_present.add(item)
    print(elements_present)
          
      # Vérifiez si un élément contient un autre
    for element1 in elements_present:
        for element2 in elements_present:
            if element1 != element2 and element1 in element2:
               for key, values in types.items():
                    if element2 in values:
                        #print(f"Type de l'élément : {key}")
                        return key

    # Si aucun élément ne contient un autre, retourner simplement un élément présent dans le nom
    if elements_present:
        #print(elements_present)
        return elements_present.pop()

    return 'autre'



# Charger le XML
tree = ET.parse('main.xml')
root = tree.getroot()

# Parcourir chaque élément 'aliment' dans le XML
for aliment in root.findall('aliment'):
    nom_aliment = aliment.find('nom').text.strip()
    type_aliment = determiner_type_aliment(nom_aliment)
    #print(type_aliment)
