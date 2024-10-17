def leggi_risultati(nome_file):
    risultati = []

    with open(nome_file, "r", encoding="utf-8") as f:

        for riga in f:
            campi = riga.rstrip("\n").split(";")

            calcolo = int(campi[4]) / 10

            minuti = int(calcolo)
            secondi = (calcolo - minuti) * 0.6

            passo = minuti + secondi

            risultati.append({

                "id": campi[5],
                "nome": campi[0] + " " + campi[1],
                "categoria": campi[3],
                "passo": passo

            })

    return risultati


def leggi_database(nome_file):
    
    with open(nome_file, "r", encoding="utf-8") as f:
        database = {}

        for riga in f:
            campi = riga.rstrip("\n").split(";")
            database[campi[0]] = float(campi[1])
    
    return database
            

def record_battuto(risultati_gara, database_record):
    record_battuto = []
    for atleta in risultati_gara:
        if atleta["passo"] < database_record[atleta["id"]]:
            record_battuto.append(atleta["nome"])

    return record_battuto
    

def separa_categorie(risultati_gara):
    cat_m = []
    cat_f = []

    for atleta in risultati_gara:

        if atleta["categoria"] == "M":
            cat_m.append(atleta)

        else:
            cat_f.append(atleta)

    return cat_m, cat_f


def main():

    risultati_gara = leggi_risultati("risultati_gara.txt")
    database = leggi_database("database_atleti.txt")
    cat_m, cat_f = separa_categorie(risultati_gara)
    atleti_migliorati = record_battuto(risultati_gara, database)

    print("\nCLASSIFICA DEI PARTECIPANTI\n")

    print("\nCategoria: M")
    for atleta in cat_m:
        print(f"{atleta['nome']}, {atleta['passo']:.2f} min/km")

    print("\nCategoria: F")
    for atleta in cat_f:
        print(f"{atleta['nome']}, {atleta['passo']:.2f} min/km")

    if len(atleti_migliorati) > 0:
        print("\nATLETI CHE HANNO SUPERATO IL RECORD PERSONALE\n")
        for atleta in atleti_migliorati:
            print(atleta)
            
    print()

main()