import csv
from operator import itemgetter


def leggi_report(nome_file):

    try:
        with open(nome_file, "r", encoding="utf-8", newline="") as f:

            reader = csv.DictReader(f, delimiter=";")
            report = list(reader)

    except OSError:
            exit(f"il file inserito {nome_file} non esiste, controllare che esista e sia presente nella cartella del file.py")


    print(f"\nNome file: {nome_file}\nAnni monitorati: da {report[0]['Anno']} a {report[-1]['Anno']}")


    try:
        for dato in report:
                for chiave, valore in dato.items():
                    if chiave not in ["Paese", "Anno"]:
                        dato[chiave] = int(valore)

    except ValueError:
        exit("c'è un errore nei valori del file")


    return report


def leggi_comandi(nome_file):
      
    comandi = []

    try:
        with open(nome_file, "r", encoding="utf-8") as f:
           
            for riga in f:
                
              comandi.append([campi for campi in riga.rstrip("\n").split()])

    except OSError:
         
         exit(f"Il file inserito {nome_file} non esiste, controllare che esista e sia presente nella cartella del file.py")
    
    return comandi
            

def esegui_paese(report, comando):
        
    anni = []
    valori = []
    
    for dati in report:
        
        if dati["Paese"] == comando[1]:
            
            anni.append(dati["Anno"])
            valori.append(dati[comando[2]])

    differenza = ((valori[-1] - valori[0]) / valori[0]) * 100

    return anni, valori, differenza


def esegui_massimo(report, comando):
    
    paesi = []

    for dati in report:

        if dati["Anno"] == comando[1]:

            paesi.append((dati["Paese"], int(dati[comando[2]])))
    

    paese_massimo = max(paesi, key=itemgetter(1))
    paese_minimo = min(paesi, key=itemgetter(1))
    aumento = ((paese_massimo[1] - paese_minimo[1]) / paese_minimo[1]) * 100

    return paese_massimo[0], paese_massimo[1], aumento


def main():
     
    report = leggi_report("GCB2023.csv")
    
    lista_comandi = leggi_comandi("queries.txt")
    
    cod_paesi = []

    [cod_paesi.append(cod["Paese"]) for cod in report if cod["Paese"] not in cod_paesi]

    cod_quantita = [chiave for chiave in report[0].keys() if chiave not in ["Paese", "Anno"]]

    print(f"Paesi monitorati: {' '.join(cod_paesi)}\nQuantità monitorate: {' '.join(cod_quantita)}\n")


    for comando in lista_comandi:
         
        if comando[0] == "paese":
         
            anni, valori, differenza = esegui_paese(report, comando)
            
            print(f"Paese: {comando[1]} - Valore: {comando[2]}")

            [print(f"{anno:>8s}", end="") for anno in anni]

            print()

            [print(f"{valore:>8d}", end="") for valore in valori]

            print(f"\nDifferenza: {differenza:+.2f}%")

        elif comando[0] == "massimo":

            paese, quantita, aumento = esegui_massimo(report, comando)

            print(f"\nAnno: {comando[1]} - Valore: {comando[2]}")

            print(f"Paese massimo: {paese} ({quantita}, {aumento:+.2f}% rispetto al minimo)")

        else:
            exit("comando non riconosciuto")


    print()


main()