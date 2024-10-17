from operator import itemgetter


def leggi_viaggi(nome_file):
    record_viaggi = {"pianeti": [], "durata_media": [], "passeggeri": 0}
    with open(nome_file, "r", encoding="utf-8") as f:
        for riga in f:
            campi = riga.rstrip("\n").split(",")
            record_viaggi["pianeti"].append(campi[0])
            record_viaggi["durata_media"].append(float(campi[1]))
            record_viaggi["passeggeri"] += int(campi[2])

        record_viaggi["durata_media"] = sum(record_viaggi["durata_media"])/len(record_viaggi["durata_media"])
    
    return record_viaggi


def leggi_pianeti(nome_file):
    record_pianeti = {}
    with open(nome_file, "r", encoding="utf-8") as f:
        for riga in f:
            campi = riga.rstrip("\n").split(",")
            record_pianeti[campi[0]] = [lingua for lingua in campi[1:]]
    return record_pianeti


def calcola_frequenze(lista_occorrenze):
    lingue = set(lista_occorrenze)
    occorrenza_lingue = []

    for lingua in lingue:
        occorrenza_lingue.append((lingua, lista_occorrenze.count(lingua)))
    
    occorrenza_lingue.sort(key=itemgetter(1), reverse=True)

    lingue_frequenti = [lingua[0] for lingua in occorrenza_lingue][:3]

    return lingue_frequenti


def main():
    
    record_viaggi = leggi_viaggi("viaggi_enterprise.txt")
    record_pianeti = leggi_pianeti("lingue_pianeti.txt")
    lingue_incontrate = []

    print(f"\nDurata media dei viaggi: {record_viaggi['durata_media']}")
    print(f"Numero totale di passeggeri: {record_viaggi['passeggeri']}")

    print("\nLingue parlate su ciascun pianeta visitato:\n")

    for pianeta in record_viaggi["pianeti"]:
        print(f"{pianeta} : {', '.join(record_pianeti[pianeta])}")
        lingue_incontrate.extend(record_pianeti[pianeta])

    top_3 = calcola_frequenze(lingue_incontrate)

    print(f"\nTre lingue più ricorrenti tra i pianeti visitati: {', '.join(top_3)}\n")


main()
