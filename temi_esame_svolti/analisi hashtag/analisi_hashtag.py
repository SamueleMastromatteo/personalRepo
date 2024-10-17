from operator import itemgetter

def leggi_hashtags(nome_file):
    record_hashtags = {}

    with open(nome_file, "r", encoding="utf_8") as f:
        for riga in f:
            campi = riga.rstrip("\n").split()
            
            if campi[0] not in record_hashtags:
                record_hashtags[campi[0]] = campi[2:]

            else:
                record_hashtags[campi[0]].extend(campi[2:])

    # record sotto forma di dizionario chiave data, valori lista hashtag della giornata,
    # le date sono consecutive nel dizionario dato che vengono inserite in ordine di apparizione nel file
                
    return record_hashtags 


def calcolo_occorrenze(hashtags_giornata):
    insieme_hashtags = set(hashtags_giornata)
    occorrenze_hashtag = [] 

    for hashstag in insieme_hashtags:
        occorrenze_hashtag.append((hashstag, hashtags_giornata.count(hashstag)))
    
    return occorrenze_hashtag


def calcolo_tendenza(occorrenze_giorno_1, occorrenze_giorno_2, perc_riferimento = 0.5):
    popolari = []
    for occ1 in occorrenze_giorno_1:
        for occ2 in occorrenze_giorno_2:
            if occ2[0] == occ1[0] and occ2[1] >= (occ1[1] + occ1[1] * perc_riferimento):
                popolari.append((occ2[0], ((occ2[1] / occ1[1]) * 100) - 100)) # fa l'append di tupla con hashtag, incremento percentuale
    
    return popolari


def main():

    record_hashtags = leggi_hashtags("hashtags.csv")
    giorni = [giorno for giorno in record_hashtags.keys()]

    for giorno in record_hashtags:
        calcolo_hashtag_gioranta = calcolo_occorrenze(record_hashtags[giorno])
        record_hashtags[giorno] = calcolo_hashtag_gioranta
    
    # il testo specifica che il file contiene esclusivamente i dati di due giornate consecutive quindi itero direttamente senza fare cicli particolari
    
    popolari = calcolo_tendenza(record_hashtags[giorni[0]], record_hashtags[giorni[1]])  
      
    popolari.sort(key=itemgetter(1), reverse=True)

    if len(popolari) > 0:

        print("\nHashtag in tendenza:\n")
        
        for popolare in popolari:
            
            print(f"{popolare[0]} con un incremento del {popolare[1]:2.0f}%")

    print()


main()