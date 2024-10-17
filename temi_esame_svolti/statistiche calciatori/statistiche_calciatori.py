import csv
from operator import itemgetter


def leggi_giocatori(nome_file):

    with open(nome_file, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter=",")
        record_giocatori = list(reader)

    for giocatore in record_giocatori:

        for campo in giocatore.keys():

            if campo not in ["player","position","team"]:
                giocatore[campo] = int(giocatore[campo])

    return record_giocatori


def calcola_stat(record_giocatori):

    attaccanti = []
    centrocampisti = []
    for giocatore in record_giocatori:

        if giocatore["position"] == "FW": # attaccante

            giocatore["efficacy"] = (giocatore["goals"] + giocatore["assists"] - giocatore["offsides"]) / giocatore["minutes"]
            attaccanti.append(giocatore)

        if giocatore["position"] == "MF": # centrocampista

            if giocatore["crosses"] != 0:
                giocatore["efficacy"] = (giocatore["interceptions"] + giocatore["ball_recoveries"] + (giocatore["assists"]/giocatore["crosses"])) / giocatore["minutes"]
                centrocampisti.append(giocatore)
    
    attaccanti.sort(key=itemgetter("efficacy"), reverse=True)
    centrocampisti.sort(key=itemgetter("efficacy"), reverse=True)

    return attaccanti, centrocampisti


def raggruppa_giocatori(record_giocatori):

    record_squadre = {}

    for giocatore in record_giocatori:
        if giocatore["team"] not in record_squadre:
            record_squadre[giocatore["team"]] = [giocatore]
        else:
            record_squadre[giocatore["team"]].append(giocatore)
    
    return record_squadre


def calcola_eta(record_squadre, anno_riferimento = 2023):
    eta_medie = []

    for squadra in record_squadre:
        eta_squadra = []

        for giocatore in record_squadre[squadra]:
            eta_squadra.append(anno_riferimento - giocatore["birth_year"])

        eta_medie.append((squadra,(sum(eta_squadra)/len(eta_squadra))))

    eta_medie.sort(key=itemgetter(1))
    
    return eta_medie


def calcola_attacco_squadra(record_squadre):
    attacco_squadre = []

    for squadra in record_squadre:
        attacco_squadra = []
        
        for giocatore in record_squadre[squadra]:

            if giocatore["position"] == "FW":
                attacco_squadra.append(giocatore["efficacy"])
        
        attacco_squadre.append((squadra, sum(sorted(attacco_squadra, reverse=True)[:3])))

    squadra_migliore = max(attacco_squadre, key=itemgetter(1))[0]

    return squadra_migliore


def cerca_attaccanti(dati_squadra):

    attaccanti_squadra = [giocatore for giocatore in dati_squadra if giocatore["position"] == "FW"]

    attaccanti_squadra.sort(key=itemgetter("efficacy"), reverse=True)

    return attaccanti_squadra[:3]


def main():

    record_giocatori = leggi_giocatori("player_stats.csv")
    
    attaccanti, centrocampisti = calcola_stat(record_giocatori)

    record_squadre = raggruppa_giocatori(record_giocatori)

    eta_medie_squadre = calcola_eta(record_squadre)

    squadra_att_migliore = calcola_attacco_squadra(record_squadre) 

    top_3_att_squadra = cerca_attaccanti(record_squadre[squadra_att_migliore])

    print(f"\nI tre attaccanti più efficaci sono:\n\n{'Nome':<20s} {'Squadra':<12s} {'Efficacia':<9s}\n")

    for i in range(3):
        print(f"{attaccanti[i]['player']:<20s} {attaccanti[i]['team']:<12s}      {attaccanti[i]['efficacy']:>.3f}")

    print(f"\nI tre centrocampisti più efficaci sono:\n\n{'Nome':<20s} {'Squadra':<12s} {'Efficacia':<9s}\n")
    
    for i in range(3):
        print(f"{centrocampisti[i]['player']:<20s} {centrocampisti[i]['team']:<12s}      {centrocampisti[i]['efficacy']:>.3f}")

    print("\nLe tre nazionali più giovani sono:\n")

    for i in range(3):
        print(f"{eta_medie_squadre[i][0]} con {eta_medie_squadre[i][1]:2.2f} anni")
    
    print(f"\nLa nazionale con l'attacco più efficace è {squadra_att_migliore}:\n")

    for i in range(3):
        print(f"{top_3_att_squadra[i]['player']} con efficacia {top_3_att_squadra[i]['efficacy']:>.3f}")

    print()


if __name__ == "__main__":
    main()