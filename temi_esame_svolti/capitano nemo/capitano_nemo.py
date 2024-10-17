from operator import itemgetter
def leggi_viaggi(nome_file):
    with open(nome_file, "r", encoding="utf-8") as f:
        record_viaggi = {
            "luoghi": set(),
            "durata_media": [],
            "passeggeri_tot": 0
        }
        for riga in f:
            campi = riga.rstrip("\n").split(",")
            record_viaggi["luoghi"].add(campi[0])
            record_viaggi["durata_media"].append(int(campi[1]))
            record_viaggi["passeggeri_tot"] += int(campi[2])

        record_viaggi["durata_media"] = sum(record_viaggi["durata_media"])/len(record_viaggi["durata_media"])

        return record_viaggi
    
def leggi_luoghi_pietre(nome_file):
    dati_luoghi = {}
    with open(nome_file, "r", encoding="utf-8") as f:
        for riga in f:
            campi = riga.rstrip("\n").split(",")
            if campi[0] not in dati_luoghi:
                dati_luoghi[campi[0]] = [pietra for pietra in campi[1:]]
            elif campi[0] in dati_luoghi:
                for pietra in campi[1:]:
                    if pietra not in dati_luoghi[campi[0]]:
                        dati_luoghi[campi[0]].append(pietra)

    return dati_luoghi

def trova_frequenti(lista_pietre_incontrate):
    frequenza_pietre = []
    top_3 = []
    insieme = set(lista_pietre_incontrate)
    for pietra in insieme:
        frequenza_pietre.append((pietra, lista_pietre_incontrate.count(pietra)))
    frequenza_pietre.sort(key=itemgetter(1), reverse=True)
    for pietra, occorrenze in frequenza_pietre[:3]:
        top_3.append(pietra)
    return top_3

def main():
    dati_viaggi = leggi_viaggi("viaggi_nemo.txt")
    dati_luoghi = leggi_luoghi_pietre("pietre_preziose_luoghi.txt")
    pietre_incontrate = []
    print(f"Durata media dei viaggi: {dati_viaggi['durata_media']}")
    print(f"Numero totale di passeggeri: {dati_viaggi['passeggeri_tot']}")
    print("Tipi di pietre preziose per luogo visitato:")
    for luogo in dati_viaggi["luoghi"]:
        print(f"- {luogo}: {', '.join(dati_luoghi[luogo])}")
        pietre_incontrate.extend(dati_luoghi[luogo])
    top_3 = trova_frequenti(pietre_incontrate)
    print(f"I tre tipi di pietre più comuni: {', '.join(top_3)} ")
   
main()