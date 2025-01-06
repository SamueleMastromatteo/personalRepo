# La mappa dei posti a teatro è rappresentata da una tabella con i prezzi dei biglietti
# per ciascun posto, come questa.
# 10, 10, 10, 10, 10, 10, 10, 10, 10, 10
# 10, 10, 10, 10, 10, 10, 10, 10, 10, 10
# 10, 10, 10, 10, 10, 10, 10, 10, 10, 10
# 10, 10, 20, 20, 20, 20, 20, 20, 10, 10
# 10, 10, 20, 20, 20, 20, 20, 20, 10, 10
# 10, 10, 20, 20, 20, 20, 20, 20, 10, 10
# 20, 20, 30, 30, 40, 40, 30, 30, 20, 20
# 20, 30, 30, 40, 50, 50, 40, 30, 30, 20
# 30, 40, 50, 50, 50, 50, 50, 50, 40, 30

# Scrivere un programma che chieda all’utente di scegliere o un posto (fornendo riga e colonna),
# o un prezzo o l’uscita dal programma. Quando l’utente specifica un posto, accertarsi che sia 
# libero e che le coordinate siano all’interno della tabella. Quando, invece, specifica un 
# prezzo, assegnare un posto qualsiasi tra quelli disponibili a quel prezzo (se ve ne sono). 
# Contrassegnare con un prezzo uguale a 0 i posti già venduti.

import sys

biglietti = [
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
    [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
    [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
    [20, 20, 30, 30, 40, 40, 30, 30, 20, 20],
    [20, 30, 30, 40, 50, 50, 40, 30, 30, 20],
    [30, 40, 50, 50, 50, 50, 50, 50, 40, 30]
]

while True:
    selezione = int(input("""1 -> seleziona posto \n2 -> seleziona prezzo \n3 -> uscita dal programma\n"""))

    if selezione == 1:
        while True:
            try:
                posto = input("seleziona posto (Enter per uscire): ")
                if posto == "":
                    break

                riga = int(posto.split(",")[0])
                colonna = int(posto.split(",")[1])

                if biglietti[riga][colonna]>0:
                    print("costo biglietto: ", biglietti[riga][colonna])
                else:
                        print("biglietto non disponibile")
            except Exception as e:
                print("inserire delle coordinate valide")
                print("errore: ",e)

            biglietti[riga][colonna] = 0
        print(biglietti)
        
    elif selezione == 2:
        prezzo = input("selezionare prezzo (Enter per uscire): ")
        if prezzo == "":
            break
        prezzo = int(prezzo)
        posto_trovato = False
        for r in range(len(biglietti)):
            for c in range(len(biglietti)):
                if biglietti[r][c] == prezzo:
                    print(f"posto assegnato: {r},{c}")
                    biglietti[r][c] = 0
                    posto_trovato = True
                    break
            if posto_trovato:
                break
        if not posto_trovato:
            print("nessun biglietto trovato a quel prezzo")

    else:
        sys.exit("uscita dal programma")

