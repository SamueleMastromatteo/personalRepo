import csv
def leggi_riviste(nome_file): # nella lista riviste metterò solo dizionari con dati utili gli altri gli ignoro 
    riviste = []
    with open(nome_file, "r", encoding="utf-8") as f:
        f.readline()
        for riga in f:
            campi = riga.rstrip("\n").split(",")
            if campi[5] != "N/A":
                riviste.append({
                    "ISSN": campi[1],
                    "IF": float(campi[5])
                })

    return riviste

def leggi_pubblicazioni():

    esiste = False

    while not esiste:
        try:
            ricercatore = input("inserire exit per chiudere il programma o inserire il nome del ricercatore per continuare: ").capitalize()

            if ricercatore == "Exit":
                return exit("chiusura programma...")
            
            nome_file = ricercatore + ".csv"

            with open(nome_file, "r", encoding="utf-8", newline="") as f:
                reader = csv.DictReader(f, delimiter=",")
                pubblicazioni_autore = list(reader)
                for pubb in pubblicazioni_autore:
                    pubb["Authors"] = pubb["Authors"].strip("'").split(",")

            esiste = True

        except OSError:
            print(f"file non valido trovato per l'autore {ricercatore}")
    
    return ricercatore, pubblicazioni_autore

def calcola_if(ricercatore, riviste, pubblicazioni_autore):
    total_if = 0.0
    first_total_if = 0.0
    last_total_if = 0.0
    first_counter = 0
    last_counter = 0
    for rivista in riviste:

        for pubblicazione in pubblicazioni_autore:
            if rivista["ISSN"] == pubblicazione["ISSN"]:
                total_if += rivista["IF"]
            
                if ricercatore in pubblicazione["Authors"][0]:
                    first_total_if += rivista["IF"]
                    first_counter += 1
                if ricercatore in pubblicazione["Authors"][-1]:
                    last_total_if += rivista["IF"]
                    last_counter += 1

    return total_if, first_total_if, first_counter, last_total_if, last_counter


def main():

    riviste = leggi_riviste("journal_IF.csv")
    ricercatore, pubblicazioni = leggi_pubblicazioni()
    total_if, first_total_if, first_counter, last_total_if, last_counter = calcola_if(ricercatore, riviste, pubblicazioni)

    print(f"Total IF di {ricercatore}: {total_if:.2f}")

    if first_counter > 1:
        print(f"Total IF come primo autore: {first_total_if:.2f} ({first_counter} pubblicazioni)")
    if first_counter == 1:
        print(f"Total IF come primo autore: {first_total_if:.2f} ({first_counter} pubblicazione)")
    if last_counter > 1:
        print(f"Total IF come ultimo autore: {last_total_if:.2f} ({last_counter} pubblicazioni)")
    if last_counter == 1:
            print(f"Total IF come ultimo autore: {last_total_if:.2f} ({last_counter} pubblicazione)")

main()