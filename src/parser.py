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
                  'ananas', 'kiwi', 'melon', 'papaye', 'framboise', 'myrtille', 'groseille', 'mure', 'citron', 
                  'abricot', 'figue', 'prune', 'cassis', 'litchi', 'nèfle', 'fruit', 'goyave', 'pamplemousse',
                  'canneberge', 'nectarine', 'kaki', 'avocat', 'pomelo', 'coing', 'datte', 'pastèque', 'olive',
                  'mandarine'],
        'spice': ['paprika', 'curry', 'cumin', 'cannelle', 'muscade', 'gingembre', 'safran', 'poivre', 'cardamome',
                  'coriandre', 'curcuma', 'anis', 'aneth', 'sel', 'romarin', 'graine', 'basilic', 'pétoncles', 
                  'persil', 'câpre','piment', 'ail', 'thym', 'estragon','laurier', 'cari'],
        'sauce': ['mornay', 'béarnaise', 'hollandaise', 'tomate', 'barbecue', 'vinaigrette', 'mayonnaise', 'soja',
                  'pesto', 'sriracha', 'hoisin', 'sauce', 'vinaigre', 'tabasco', 'moutarde'],
        'meat': ['bison', 'boeuf', 'poulet', 'agneau', 'porc', 'canard', 'cheval', 'lapin', 'bœuf', 'veau', 'dinde',
                 'gibier', 'beef', 'sanglier','faisan', 'pintade', 'autruche', 'lièvre', 'saucisse', 'merguez', 'saucisson',
                 'jambon', 'grison', 'pastrami', 'pigeonneaux', 'chipolata', 'bacon', 'salami', 'caille', 'mortadelle',
                 'oie', 'viande'],
        'vegetable': ['carotte', 'tomate', 'brocoli', 'épinard', 'concombre', 'poivron', 'courgette','pomme de terre',
                       'courge', 'aubergine', 'asperge', 'radis', 'haricot', 'pommes de terre', 
                       'céleri', 'chou', 'fève', 'pois', 'champignon', 'cornichon', 'scarole', 'oignon',
                        'pissenlit', 'cresson', 'rutabaga', 'échalote', 'laitue', 'rhubarbe', 'roquette', 'shiitaké',
                        'betterave', 'artichaut', 'endive', 'navet', 'poireau', 'patate'],
        'nuts': ['amande', 'noisette', 'noix', 'pistache', 'mâche', 'topinambour', 'pâtisson','châtaigne'],
        'dairy': ['lait', 'fromage', 'yaourt', 'beurre', 'crème', 'kéfir', 'féta', 'coulommiers', 'ricotta', 'parmesan',
                  'mascarpone', 'emmental', 'roquefort', 'comté', 'petit-suisse', 'dairy', 'mozzarella', 'edam', 'cantal',
                  'camembert', 'brie', 'boursin', 'gouda', 'reblochon', 'munster', 'dairy'],
        'egg': ['œuf', 'omelette', 'frittata', 'meringue', 'oeuf'],
        'seafood': ['crevette', 'saumon', 'thon', 'huître', 'moule', 'crabe', 'homard', 'calamar', 'palourde', 
                    'langouste','saint-Jacques', 'anguille', 'éperlan', 'esturgeon', 'truite', 'sardine', 'seiche',
                    'maquereau', 'morbier', 'aiglefin', 'poisson', 'poulpe', 'morue','turbot', 'flétan','espadon', 
                    'merlan', 'ormeau', 'calmar', 'bigorneau', 'caviar', 'colin', 'tourteau', 'mulet', 'bar',
                    'surimi', 'écrevisse', 'coquille st-jacques', 'carpe', 'araignée de mer', 'hareng' ],
        'cereal': ['blé', 'riz', 'maïs', 'avoine', 'quinoa', 'millet', 'épeautre', 'sarrasin', 'seigle', 'orge',
                   'boulgour','pâtes', 'lentille', 'manioc'],
        'drink': ['eau', 'jus', 'café', 'thé', 'cola', 'vin', 'bière', 'perrier', 'boisson', 'vodka', 'whisky', 'rhum', 
                  'champagne', 'cappucino', 'liqueur', 'soda', 'tisane', 'pastis'],
        'autre': ['chouquette', 'sandwich', 'huile', 'pain', 'pizza', 'cubes', 'composés', 'soupe', 'ravioli', 'graisse', 'croquette',
                  'biscuit', 'beignet', 'barre', 'pâté']
    }

     # Liste des préfixes à ignorer
    prefixes_a_ignorer = [' au ', ' à ', ' aux ']

    # Convertir le nom de l'aliment en minuscules pour la correspondance insensible à la casse
    nom_aliment_lower = nom_aliment.lower()

    elements_present = set()

    #print(elements_present)
    for element_type, keywords in types.items():
        for keyword in keywords:
            # Vérifier si le mot est un mot entier dans le nom de l'aliment et on ignore sa terminaison dans le cas d'un mot en pluriel ou autre
            if re.search(r'\b{}\w*\b'.format(keyword), nom_aliment_lower):
                prefix_before_keyword = nom_aliment_lower.partition(keyword)[0]
                if not any(prefix in prefix_before_keyword for prefix in prefixes_a_ignorer):
                         elements_present.add(keyword)
                         #Si un des types d'aliments correspond à autre on clear elements_present et retournons autre car c est le type le plus "fort"
                         if element_type == 'autre':
                              elements_present.clear()
                              return 'autre'


    # Si aucun élément du tableau n'est trouvé, retourner "autre"
    if not elements_present:
        return 'autre'

    most_specific_element = None
    # Comparaison des éléments présents dans l'ensemble
    if len(elements_present) > 1:
          #print(elements_present)     
          for element1 in elements_present:
               for element2 in elements_present:
                    if element1 != element2:  # Pour éviter de comparer un élément avec lui-même
                         #donc l'élément qui contient l'autre l'emporte par exemple vinaigre>vin
                         if element1 in element2:
                              most_specific_element = element2
                         else:
                              most_specific_element = element1
    else:
          #print(elements_present,most_specific_element)
          most_specific_element = elements_present.pop()
          #print(most_specific_element)

    # Retourner le type correspondant à l'élément le plus spécifique
    for element_type, value in types.items():
        #print(element_type,value)
        if most_specific_element in value:
            #print(element_type)
            return element_type

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
                    #print(type_aliment)
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

                    calories_aliment_match = re.search(r'Energie \(kCal\): (.+)', aliment)
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
fichier_texte = '../data/scrapped.txt'
fichier_xml = '../data/aliments.xml'

# Lecture des données du fichier texte
donnees = lire_donnees(fichier_texte)

# Création du fichier XML
creer_fichier_xml(donnees, fichier_xml)

print("Le fichier XML a été créé avec succès !")
