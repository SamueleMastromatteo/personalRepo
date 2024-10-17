from operator import itemgetter


def leggi_partecipanti(nome_file):
    record_partecipanti = {}
    with open(nome_file, "r", encoding="utf-8") as f:
        for riga in f:
            campi = riga.rstrip("\n").split(":")
            record_partecipanti[campi[0]] = campi[1]

    return record_partecipanti


def leggi_penalita(nome_file):
    record_penalita = {}
    with open(nome_file, "r", encoding="utf-8") as f:
        for riga in f:
            campi = riga.rstrip("\n").split(":")
            record_penalita[campi[0]] = [int(n) for n in campi[1:]]

    return record_penalita


def organizza_dati(partecipanti, record_penalita):
    dati_partecipanti = []
    for pettorale in partecipanti:
        dati_partecipanti.append({
            "nome": partecipanti[pettorale],
            "penalita": record_penalita[pettorale],
            "tot_penalita": sum(record_penalita[pettorale])
        })

    dati_partecipanti.sort(key=itemgetter("tot_penalita"))

    return dati_partecipanti


def conta_sequenze(dati_partecipante):
    sequenze_zero = []
    sequenza = 0

    for penalita in dati_partecipante["penalita"]:

        if penalita == 0:
            sequenza += 1

        else:
            sequenze_zero.append(sequenza)

            sequenza = 0
    
    dati_partecipante["sequenza"] = max(sequenze_zero)


def main():

    partecipanti = leggi_partecipanti("partecipanti.txt")
    record_penalita = leggi_penalita("penalita.txt")
    dati_partecipanti = organizza_dati(partecipanti, record_penalita)

    print("\nClassifica:\n")
    for dato in dati_partecipanti:
        conta_sequenze(dato)
        print(f"{dato['nome']:<15s} {dato['tot_penalita']:>3d} {'penalità':>}")

    partecipante_migliore = max(dati_partecipanti, key=itemgetter("sequenza"))
    
    print(f"\nHa realizzato la più lunga sequenza {partecipante_migliore['nome']} con {partecipante_migliore['sequenza']} prove consecutive superate senza errori\n")


main()        