from operator import itemgetter

def leggi_listino(nome_file):
    listino = []
    with open(nome_file, "r", encoding="utf-8") as f:
        for riga in f:
            campi = riga.rstrip("\n").split(";")
            listino.append({
                "pagine": [i for i in range(int(campi[0]), int(campi[1])+1)],
                "costo": float(campi[2].rstrip("€"))
            })
    listino.sort(key=itemgetter("pagine"))
    return listino


def leggi_libri():

    esiste = False
    libri = {}

    while not esiste:
        try:
            nome_file = input("Digitare exit per chiudere oppure Inserire il nome del file contenente i libri da stampare: ")

            if nome_file == "exit":
                return exit("chiusura programma...")
            
            with open(nome_file, "r", encoding="utf-8") as f:
                for riga in f:
                    campi = riga.rstrip("\n").split(";")
                    libri[campi[0]] = int(campi[1])

            esiste = True

        except OSError:
            print(f"Il file inserito {nome_file} non esiste, riprovare")

    return dict(sorted(libri.items()))


def calcola_prezzo(n_pagine, prezzi_stampa):
    for prezzo in prezzi_stampa:
        if n_pagine in prezzo["pagine"]:
            return prezzo["costo"] * n_pagine
    
    

def main(): 

    listino_stampa = leggi_listino("costipagine.txt")
    libri = leggi_libri()
    totale = 0.0

    print("\nLISTINO PREZZI")
    for prezzo in listino_stampa:
        print(f"Fino a {max(prezzo['pagine'])} pagine: {prezzo['costo']}€/pagina")
    
    print("\nCOSTI DI STAMPA")
    for libro, n_pagine in libri.items():
        prezzo_libro = calcola_prezzo(n_pagine, listino_stampa)
        totale += prezzo_libro
        print(f"{libro} - Pagine: {n_pagine} - Costo: {prezzo_libro:>4.2f}€")

    print(f"Totale: {totale:>5.2f}€\n")

main()