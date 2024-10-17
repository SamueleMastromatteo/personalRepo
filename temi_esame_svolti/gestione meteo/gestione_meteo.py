import csv
def leggi_dati_meteo():
    sbagliato = True
    while sbagliato:
        try:
            nome_file = input(f"scrivi exit per chiudere il programma o il nome del file con i dati metereologici per continuare: ")
            
            if nome_file == "exit":
                return exit("chiusura programma...")
            
            with open(nome_file, "r", encoding="utf-8", newline="") as f:
                reader = csv.DictReader(f, delimiter=";")
                dati_meteo = list(reader)
                for dato in dati_meteo:
                    dato["Data"] = dato["Data e Ora"][:8] 
                    # interessa solo la data, l'ora non è necessaria per l'esercizio
                    del dato["Data e Ora"]
                    for chiave, valore in dato.items():
                        # guardo tutte le coppie chiavi, valori e se la chiave non è data converto i valori della chiave in float
                        if chiave != "Data":
                            dato[chiave] = float(valore)
                
            sbagliato = False

        except OSError:
            print(f"input non valido, riprovare...")

    return nome_file, dati_meteo # restituisco anche il nome file dato che serve per la print finale


def organizza_dati(dati_stazione):

    nomi_variabili = [] # questa lista serve solo per la print finale
    dati_organizzati = dict()
    date = []

    # non uso un set per le singole date dato che poi dovrei riordinare il file in ordine cronologico
    for dato in dati_stazione:
        if dato["Data"] not in date:
            date.append(dato["Data"])


    for giorno in date:
        dati_giornata = dict()

        for dato in dati_stazione:
            if dato["Data"] == giorno:
                for chiave, valore in dato.items(): # dict.items() la uso per controllare le chiavi che non sono data, visto che il nome e numero non è noto
                    if chiave != "Data":
                        if chiave not in nomi_variabili:
                            nomi_variabili.append(chiave)
                        if chiave not in dati_giornata:
                            dati_giornata[chiave] = [valore]
                        else:
                            dati_giornata[chiave].append(valore)

        dati_organizzati[giorno] = dati_giornata

    return dati_organizzati, nomi_variabili     


def compila_tabella(lista, valori):
    insieme = set(valori)
    moda = 0.0
    massimo = max(valori)
    minimo = min(valori)
    media = sum(valori)/len(valori)
    for valore in insieme:
        n_occorrenze = valori.count(valore)
        if n_occorrenze >= valori.count(moda):
            moda = valore
    
    lista.append([media, massimo, minimo, moda])
    return lista


def main():
    nome_file, dati_meteo = leggi_dati_meteo()
    dati_organizzati, nome_variabili= organizza_dati(dati_meteo)
    nomi_calcoli = ["media", "massimo", "minimo", "moda"]
    print(f"\nReport metereologico per la stazione di {nome_file.strip('.csv').capitalize()}\n\n", end="        ")
    
    for variabile in nome_variabili:
            print(f"{variabile:^25s}", end="")
            
    for giorno, informazioni in dati_organizzati.items():
        lista= []
        print(f"\n{giorno}\n")

        for valori in informazioni.values():
            # genero una lista di liste, la tabella contiene n_liste in base alle variabili nel file e ogni lista ha i valori media,massimo,minimo e moda
            tabella = compila_tabella(lista, valori)

        for i_riga in range(len(tabella[0])):
            # il nome dei calcoli che ci sono a ogni riga della tabella stampata è noto a priori
            # uso una lista creata manualmente in precedenza assieme all'indice riga per stamparlo al momento giusto 
            print(f"{nomi_calcoli[i_riga]:>8s}", end="") 

            for i_colonna in range(len(tabella)): 
                # uso questi due cicli per stampare solo il primo valore di ogni lista presente nella tabella, per poi passare al secondo ecc...
                print(f"{tabella[i_colonna][i_riga]:^25.2f}", end="") 
            print("\n")
main()