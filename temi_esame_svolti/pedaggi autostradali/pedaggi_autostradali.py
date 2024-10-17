from operator import itemgetter


def leggi_auto(nome_file):
    record_auto = []
    targhe_registrate = []
    with open(nome_file, "r", encoding="utf-8") as f:

        for riga in f:
            campi = riga.rstrip("\n").split(";")

            if campi[0] not in targhe_registrate:
                record_auto.append({

                    "targa": campi[0],
                    "percorsi": [[campi[1], campi[2]]],
                    "ingressi": 1

                })

                targhe_registrate.append(campi[0])

            else:
                for auto in record_auto:
                    if campi[0] == auto["targa"]:
                        auto["ingressi"] += 1
                        auto["percorsi"].append([campi[1], campi[2]])

    return record_auto


def leggi_tratte(nome_file):
    tratte = []
    with open(nome_file, "r", encoding="utf-8") as f:
        for riga in f:
            campi = riga.rstrip("\n").split(";")
            tratte.append([campi[0], campi[1], float(campi[2])])

    return tratte


def calcola_percorso(ingresso, uscita, tratte):

    pos_in = None
    pos_out = None

    for i, tratta in enumerate(tratte):
        if ingresso == tratta[0]:
            pos_in = i
        if uscita == tratta[1]:
            pos_out = i
    
    if pos_in != None and pos_out != None and pos_out >= pos_in:

        pedaggio = 0.0

        for i in range(pos_in, pos_out + 1):

            pedaggio += tratte[i][2]
        
        return pedaggio, pos_out - pos_in + 1
    
    else:

        for i, tratta in enumerate(tratte):
            if ingresso == tratta[1]:
                pos_in = i
            if uscita == tratta[0]:
                pos_out = i

        pedaggio = 0.0

        for i in range(pos_out, pos_in + 1):

            pedaggio += tratte[i][2]

        return pedaggio, pos_in - pos_out + 1


def main():

    record_auto = leggi_auto("auto.txt")
    dati_tratte = leggi_tratte("pedaggi.txt")
    print()
    for auto in record_auto:
        auto["pedaggio_tot"] = 0.0
        n_tratte_tot = 0

        for ingresso, uscita in auto["percorsi"]:
            pedaggio, n_tratte = calcola_percorso(ingresso, uscita, dati_tratte)
            auto["pedaggio_tot"] += pedaggio
            n_tratte_tot += n_tratte

        print(f"{auto['targa']}: {auto['pedaggio_tot']:.2f} pedaggio pagato ({n_tratte_tot} tratte percorse in {auto['ingressi']} ingressi)")
    
    record_auto.sort(key=itemgetter("pedaggio_tot"), reverse=True)

    print(f"\nL'auto che ha pagato il pedaggio maggiore ha targa {record_auto[0]['targa']}.\n")


main()