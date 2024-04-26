**Readme - Scrapper**

J'ai conçu un script récupérant les liens sur la page "https://www.lanutrition.fr/les-aliments-a-la-loupe" pour scrapper les valeurs nutritionelles de chaque aliment
### Prérequis

- Python 3.x
- Les bibliothèques Python suivantes :
  - requests
  - BeautifulSoup4
  - urllib.parse
  - pickle
  - re
  - xml.sax.saxutils


### Informations
- scrapper.py: Ce script extrait les valeurs nutritionnelles des différents aliments à partir de la page "https://www.lanutrition.fr/les-aliments-a-la-loupe" et les enregistre dans un fichier texte.
- sarser.py: Ce script prend les informations extraites du fichier texte et les formate dans une structure XML.
- to_scv.py: Ce script convertit les données extraites et formatées en XML en un format de fichier CSV plus standardisé, facilitant leur manipulation et leur analyse ultérieures.
- analyse.py: Ce script prend les données du fichier XML et les présente dans un format convivial pour l'humain, regroupant les aliments par type et fournissant des informations nutritionnelles agrégées.
- kmeans.py: Ce module contient l'implémentation de l'algorithme de clustering K-Means, qui est utilisé pour partitionner les aliments en clusters en fonction de leurs caractéristiques nutritionnelles similaires.
- kmoyen.py: Ce programme est le point d'entrée de l'analyse de clustering. Il utilise les données prétraitées de "to_csv" pour appliquer l'algorithme K-Means et générer des clusters d'aliments en fonction de leurs valeurs nutritionnelles.

### Éxécution

Je conseil d'utiliser ``python3 scrapper.py && python3 parser.py && python3 to_csv.py && python3 analyse.py `` pour éxécuter tous les programmes liés au traitement de donnés de manière à ne pas les éxécuter individuellement.

``python3 kmoyen.py`` permet d'éxécuter le programme contenant l'analyse de clustering


### Avertissement

Ce script est fourni à titre informatif et éducatif uniquement. L'utilisation abusive de ce script peut violer les conditions d'utilisation de lanutrition.fr ou causer 
une charge inutile sur leurs serveurs.
