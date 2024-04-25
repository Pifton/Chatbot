import csv
import numpy as np
import matplotlib.pyplot as plt
import random as rnd
import kmeans
    


def lire_csv(nom_fichier):
    aliments = []
    with open(nom_fichier, 'r', newline='', encoding='utf-8') as csvfile:
        lecteur = csv.DictReader(csvfile)
        for ligne in lecteur:
            nom_aliment = ligne['nom']
            type_aliment = ligne['type']
            calories = float(ligne['calories']) if ligne['calories'] else 0
            proteins = float(ligne['proteins']) if ligne['proteins'] else 0
            aliments.append((nom_aliment,type_aliment, calories, proteins))
    return aliments

def main():
    nom_fichier = 'aliments.csv'
    aliments = lire_csv(nom_fichier)
    #print("Nom,Type, Calories, Proteins")
    #for aliment in aliments:
    #    print(aliment) 
    #print(aliments)

    sse = []
    center_result = []
    cluster_result = []

    for i in range(1, 10):
        tmp_centre = kmeans.tmp_centre(i, aliments)
        print("tmp_centre",tmp_centre)
        cluster = kmeans.cluster_association(aliments, tmp_centre, i)
        #print("cluster",cluster)
        center = kmeans.definitive_centers(aliments, cluster, i)
        print("center",center)
        sse.append(kmeans.calcul_sse(i, cluster, center, aliments))
        center_result.append(center)
        cluster_result.append(cluster)

    xpoints = np.array([1, 8])
    ypoints = np.array([3, 10])

    plt.plot(xpoints, ypoints)
    plt.show()

main()
