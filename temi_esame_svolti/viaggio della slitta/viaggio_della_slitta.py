import csv
import math
from operator import itemgetter


def rad(dato_in_gradi):

    return dato_in_gradi * math.pi/180


def calcola_h(lat_a, lat_b, long_a, long_b):
    lat_a = rad(lat_a)
    lat_b = rad(lat_b)
    long_a = rad(long_a)
    long_b = rad(long_b)

    return math.sin(abs(lat_a - lat_b)/2)**2 + math.cos(lat_a) * math.cos(lat_b) * math.sin(abs(long_a - long_b)/2)**2


def calcola_distanza(h, R = 6731):
    # R di default è il raggio della terra in km
    return (2 * R * math.asin(math.sqrt(h)))


def leggi_provincie(nome_file):
    record_provincie = []
    with open(nome_file, "r", encoding="utf-8") as f:
        f.readline()
        for riga in f:
            campi = riga.rstrip("\n").split(",")
            record_provincie.append({

                "provincia": campi[4],
                "lat": float(campi[5]),
                "long": float(campi[6])
            })

    return record_provincie


def leggi_bambini(nome_file):
    with open(nome_file, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        bambini = [record for record in reader]

    return(bambini)


def aggiorna_dati(bambini, province):
    for bambino in bambini:
        for provincia in province:
            if bambino["provincia"] == provincia["provincia"]:
                bambino["lat"] = provincia["lat"]
                bambino["long"] = provincia["long"]

    bambini.sort(key=itemgetter("lat"), reverse = True)


def prossimo_bambino(vicino, bambini):
    
    distanze = []
    for bambino in bambini:
        distanze.append(calcola_distanza(calcola_h(vicino["lat"], bambino["lat"], vicino["long"], bambino["long"])))

    vicino = bambini[distanze.index(min(distanze))]
    distanza_vicino = min(distanze)
    return vicino, distanza_vicino
         

def main():

    province = leggi_provincie("province.csv")
    bambini = leggi_bambini("bambini.csv")
    aggiorna_dati(bambini, province)

    vicino = bambini[0] # bambino piu a nord
    
    print(f"\nConsegnato {vicino['regalo']} a {vicino['nome']} {vicino['cognome']} ({vicino['provincia']})")

    bambini.remove(vicino)

    while len(bambini) > 0:
        
        vicino, distanza_vicino = prossimo_bambino(vicino, bambini)
        print(f"    Viaggio di {distanza_vicino} Km")
        print(f"Consegnato {vicino['regalo']} a {vicino['nome']} {vicino['cognome']} ({vicino['provincia']})")
        bambini.remove(vicino)

    print()

main()