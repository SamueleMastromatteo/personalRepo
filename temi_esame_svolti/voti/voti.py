import csv
from operator import itemgetter

def leggi_appello(nome_file):
    with open(nome_file, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        appello = [studente for studente in reader] # crea lista di dizionari contenenti i dati dell'appello con la comprehension iterando su reader 
    return appello

def scrivi_sessione(dati_sessione):
    with open("sessione.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, dati_sessione[0].keys())
        writer.writeheader() # scrive la prima riga che indica i campi presi dalle chiavi dei dizionari
        writer.writerows(dati_sessione) # scrive il resto delle righe 

def media_differenze(lista_studenti):
    differenze = [float(studente["voto"]) - float(studente["media_esami_precedenti"]) for studente in lista_studenti]
    return sum(differenze)/len(differenze)

def main():

    dati_sessione = leggi_appello("primo_appello.csv") + leggi_appello("secondo_appello.csv") # sommo le due liste di dizionari ottenute leggendo i 2 file con la funzione
    dati_sessione.sort(key=itemgetter("voto", "cognome")) # ordino la lista di dizionari completa prima per voto poi per cognome
    scrivi_sessione(dati_sessione)
    media_diff_top_5 = media_differenze(dati_sessione[-5:]) # do in argomento solo una lista di dizionari con i 5 studenti con i voti piu alti usando il fatto che è ordinata
    print(f"La media tra le differenze tra voto e media pregressa per i cinque studenti con voto maggiore nella sessione è : {media_diff_top_5:.2f}")

main()    