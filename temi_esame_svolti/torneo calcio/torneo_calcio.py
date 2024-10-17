from operator import itemgetter


def leggi_partite(nome_file):
    record_partite = []
    squadre_registrate = []
    with open(nome_file, "r", encoding="utf-8") as f:

        for riga in f:
            campi = riga.rstrip("\n").split(":")
            squadre = campi[:2]
            for squadra in squadre:
                if squadra not in squadre_registrate:
                    squadre_registrate.append(squadra)
            record_partite.append([campi[0], campi[1], int(campi[2]), int(campi[3])])
    
    return squadre_registrate, record_partite

def calcola_partite(squadra, partite):

    record_squadra = { "squadra":squadra, "gol_segnati": 0, "gol_ricevuti": 0, "punti": 0}

    for partita in partite:

        if squadra in partita:

            i = partita.index(squadra)

            if i == 0:

                record_squadra["gol_segnati"] += partita[2]
                record_squadra["gol_ricevuti"] += partita[3]

                if partita[2] > partita[3]:
                    record_squadra["punti"] += 3 # vittoria

                if partita[2] == partita[3]:
                    record_squadra["punti"] += 1 # pareggio



            elif i == 1:
                record_squadra["gol_segnati"] += partita[3]
                record_squadra["gol_ricevuti"] += partita[2]

                if partita[3] > partita[2]:
                    record_squadra["punti"] += 3 # vittoria

                if partita[3] == partita[2]:
                    record_squadra["punti"] += 1 # pareggio


            else:
                exit("c'è un problema")
        
    return record_squadra


def main():

    squadre, partite = leggi_partite("torneo.txt")

    dati_squadre = []

    for squadra in squadre:
        dati_squadra = calcola_partite(squadra, partite)
        dati_squadre.append(dati_squadra)
    
    dati_squadre.sort(key=itemgetter("punti"), reverse=True)

    print("\nClassifica:\n")

    for i, dato in enumerate(dati_squadre):
        print(f"{i+1}. {dato['squadra']} - Punti: {dato['punti']}, Gol fatti: {dato['gol_segnati']}, Gol subiti: {dato['gol_ricevuti']}")
    
    miglior_attacco = max(dati_squadre, key=itemgetter("gol_segnati"))
    miglior_difesa = min(dati_squadre, key=itemgetter("gol_ricevuti"))

    print(f"\nMiglior attacco: {miglior_attacco['squadra']} - Gol fatti: {miglior_attacco['gol_segnati']}")

    print(f"Miglior difesa: {miglior_difesa['squadra']} - Gol subiti: {miglior_difesa['gol_ricevuti']}\n")

main()

            