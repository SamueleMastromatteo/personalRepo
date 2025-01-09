# Scrivere un programma che legga i dati dal file di testo
# rawdata_2004.txt e li inserisca in un dizionario le cui chiavi sono nomi di nazioni e i cui valori
# sono redditi annui pro capite. Si noti che nel file i campi sono separati da un carattere di tabulazione
# '\t'. Poi, il programma deve chiedere all’utente di fornire in input nomi di nazioni, per visualizzare i
# valori corrispondenti di reddito annuo pro capite. Il programma deve terminare quando l’utente
# inserisce in input la stringa 'quit'. È possibile leggere dati analoghi, aggiornati al 2021, in formato
# .csv, dal file rawdata_2021.csv. Provare a risolvere lo stesso esercizio lavorando su questo file
# .csv.

def leggi_dati_2004(input_file):
    reddito = {}
    with open(input_file, "r", encoding="utf-8") as f:
        for riga in f:
            campi = riga.strip().split("\t")
            if len(campi) >= 3:
                nazione = campi[1].strip()
                reddito_annuo = campi[2].strip().replace(",", "")
                reddito[nazione] = reddito_annuo
    return reddito

def leggi_dati_2021(input_file):
    reddito = {}
    with open(input_file, "r", encoding="utf-8") as f:
        colonne = f.readline()
        colonne = colonne.split(",")
        for riga in f:
            campi = riga.strip().split('","')
            nazione = campi[0].replace('"', '')
            continente = campi[-1].replace('"', '')
            reddito[nazione] = campi[2]
    return reddito
            
def main():
    #reddito = leggi_dati_2004("rawdata_2004.txt")
    reddito = leggi_dati_2021("rawdata_2021.csv")
    while True:
        nome = input("inserisci nome di una nazione: ")
        if nome.lower() == 'quit':
            break
        if nome in reddito:
            print(f"Il reddito annuo pro capite di {nome} è {reddito[nome]}")
        else:
            print(f"Nazione {nome} non trovata nei dati.")

    
if __name__ == "__main__":
    main()