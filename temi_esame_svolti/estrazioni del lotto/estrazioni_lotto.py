from operator import itemgetter


def leggi_storico(nome_file):
    storico = {}
    with open(nome_file, "r", encoding="utf-8") as f:
        for riga in f:
            campi = riga.rstrip("\n").split()
            if campi[1] not in storico:
                storico[campi[1]] = [(campi[0], [int(n) for n in campi[2:7]])]
            else:
                storico[campi[1]].append((campi[0], [int(n) for n in campi[2:7]]))

    return storico
    

def individua_occorrenze(estrazioni_ruota1, estrazioni_ruota2):
    occorrenze = []
    numeri_calcolati = []
    for estrazione1 in estrazioni_ruota1:
        for estrazione2 in estrazioni_ruota2:
            if estrazione1[0] == estrazione2[0]:
                for n in estrazione1[1]:
                    if n in estrazione2[1]:
                        occorrenze.append((n, estrazione1[0]))
                        numeri_calcolati.append(n)

    return occorrenze, numeri_calcolati


def calcola_frequenza(lista_numeri):
    ins_numeri = set(lista_numeri)
    num_frequenza = []
    for n in ins_numeri:
        num_frequenza.append((n, lista_numeri.count(n)))

    num_frequenza.sort(key=itemgetter(1), reverse=True)
    
    return num_frequenza
    

def main():


    storico = leggi_storico("storico01-oggi.txt")
    print(f"\nRuote disponibili {', '.join(storico.keys())}\n")
    corretto = False

    while not corretto:
        try:
            print("\nInserisci exit all'inserimento della prima o della seconda ruota per chiudere il programma\n")
            prima_ruota = input("Inserisci la prima ruota: ")
            seconda_ruota = input("Inserisci la seconda ruota: ")

            if prima_ruota == "exit" or seconda_ruota == "exit":
                exit("chiusura programma...")

            occorrenze, numeri = individua_occorrenze(storico[prima_ruota], storico[seconda_ruota])
            corretto = True

        except KeyError:
            print(f"c'è stato un problema nell'inserimento delle ruote, riprovare")

    for occorrenza in occorrenze:
        print(f"Numero comune {occorrenza[0]:>2d} in data {occorrenza[1]}")

    num_frequenza = calcola_frequenza(numeri)

    print(f"\nNumero    Frequenza\n{'-' * 8}  {'-' * 9}")

    for n, frequenza in num_frequenza:
        print(f"{n:>8d} {frequenza:>9d}")


main()