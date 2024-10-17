import math
from operator import itemgetter

def leggi_traiettorie(nome_file):
    traiettorie = []
    with open(nome_file, "r", encoding="utf-8") as f:
        for riga in f:
            campi = riga.rstrip("\n").split(":")
            traiettorie.append({
                "drone": campi[0],
                "fermate": campi[1].split(","),
                "n_fermate": len(campi[1].split(",")) - 1
            })

    return traiettorie


def leggi_fermate(nome_file):
    fermate = {}
    with open(nome_file, "r", encoding="utf-8") as f:
        for riga in f:
            campi = riga.rstrip("\n").split(":")
            fermate[campi[0]] = tuple([int(valore) for valore in campi[1].split(",")])

    return fermate


def calcola_distanza(cord_partenza, cord_arrivo):
    x1, y1 = cord_partenza
    x2, y2 = cord_arrivo
    distanza = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return distanza


def calcola_tragitto(traiettorie, cord_fermate):
    for drone in traiettorie:
        distanza_percorsa = 0.0
        for i, fermata in enumerate(drone["fermate"]):
            if i < len(drone["fermate"]) - 1:
                distanza_percorsa += calcola_distanza(cord_fermate[fermata], cord_fermate[drone["fermate"][i + 1]])

        drone["distanza_percorsa"] = distanza_percorsa

    # ordino la lista dei dizionari in modo che il primo dizionario sia quello con il drone con la distanza percorsa maggiore
    traiettorie.sort(key=itemgetter("distanza_percorsa"), reverse=True) 


def main():

    traiettorie = leggi_traiettorie("drones.txt")
    cord_fermate = leggi_fermate("stops.txt")
    calcola_tragitto(traiettorie, cord_fermate)
    print(f"\nhighest battery capacity for {traiettorie[0]['drone']}\ntotal distance = {traiettorie[0]['distanza_percorsa']:.1f}\nnumber of stops = {traiettorie[0]['n_fermate']}\n")

main()