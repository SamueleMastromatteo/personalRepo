from operator import itemgetter

def leggi_dati(nome_file):
    record_dati = []
    with open(nome_file, "r", encoding="utf-8") as f:
        f.readline()
        for riga in f:
            campi = riga.rstrip("\n").split(",")
            if campi[4] == "E":
                record_dati.append({
                    "negozio": campi[2],
                    "prodotto": campi[3],
                    "prezzo": float(campi[5])
                })

    return record_dati


def leggi_negozi(nome_file):
    with open(nome_file, "r", encoding="utf-8") as f:
        negozi = [riga.rstrip("\n") for riga in f]

    return sorted(negozi)


def rileva_minimo(record_dati, negozio, prodotto):
    prezzi_prodotto = []
    for dato in record_dati:
        if negozio == dato["negozio"] and prodotto == dato["prodotto"]:
            prezzi_prodotto.append(dato["prezzo"])

    return min(prezzi_prodotto)


def prodotti_essenziali(record):
    prodotti_essenziali = set()
    for dato in record:
        prodotti_essenziali.add(dato["prodotto"])
        
    return sorted(prodotti_essenziali)
        

def cerca_cibo(record_dati):
    corretto = False
    prezzi = []

    while not corretto:
        cibo = input("\nChe cibo vuoi cercare? (q per smettere): ")

        if cibo == "q":
            return exit("chiusura programma...")
        
        else:
            for dato in record_dati:
                if dato["prodotto"] == cibo:
                    prezzi.append(dato)

        if len(prezzi) > 0:
            corretto = True
            prezzi.sort(key=itemgetter("prezzo"))
            minimo = prezzi[0]

            print(f"Prezzo minimo: {minimo['prezzo']} $/kg da {minimo['negozio']}")
        
        else:
            print(f"Cibo {cibo} non trovato")


def main():

    record_dati = leggi_dati("NLFoodPricing.csv")
    negozi = leggi_negozi("shops.txt")
    prodotti_e = prodotti_essenziali(record_dati)
    
    print("\nProdotti:")
    for prodotto in prodotti_e:
        print(f"- {prodotto}")
    
    for negozio in negozi:
        print(f"\n{negozio}")
        for prodotto in prodotti_e:
            prezzo_minimo = rileva_minimo(record_dati, negozio, prodotto)
            print(f"- {prodotto}: {prezzo_minimo} $/kg")

    cerca_cibo(record_dati)


main()