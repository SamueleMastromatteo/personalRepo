from operator import itemgetter

def controllo_file(tipologia_file):
    # tipologia_file consiste nel tipo di file da richiedere in input in modo da capire nel caso di più file quale inserire
    esiste = False
    while not esiste:
        try:
            nome_file = input(f"Inserisci il nome del file {tipologia_file}, nel caso si voglia chiudere il programma non inserire nulla: ")
            file = open(nome_file)
            file.close()
            esiste = True
        except OSError:
            print("Il file inserito non esiste, riprovare...")

    return nome_file

def leggi_comuni(): 
    # leggo il file e lo organizzo in una lista di dizionari, ignoro i dati che non sono necessari (popolazione e regione)
    comuni = []
    #nome_file = "comuni.csv"
    nome_file = controllo_file("comuni")
    with open(nome_file, "r", encoding="utf-8") as f:
        for riga in f:
            campi = riga.rstrip("\n").split(";")
            comuni.append({
                "nome": campi[0],
                "provincia": campi[2],
                "altitudine": int(campi[4])
            })

    return comuni

def leggi_province():
    #nome_file = "provincie.txt"
    nome_file = controllo_file("province")
    province = []
    with open(nome_file, "r", encoding="utf-8") as f:
        for riga in f:
            province.append(riga.rstrip("\n"))

    return province

def massime_altitudini(dati_comuni, lista_provincie):
    comuni_max_alt = []
    for provincia in lista_provincie:
        comuni_provincia = []
        for comune in dati_comuni:
            if comune["provincia"] == provincia:
                comuni_provincia.append(comune)
        comuni_provincia.sort(key=itemgetter("altitudine"), reverse=True)
        max_alt = comuni_provincia[0]
        comuni_max_alt.append(max_alt)

    return comuni_max_alt

def main():
   
    dati_comuni = leggi_comuni()
    lista_province = leggi_province()
    comuni_max_alt = massime_altitudini(dati_comuni, lista_province)

    for comune in comuni_max_alt:
        print(f"Comune più alto nella provincia di {comune['provincia']} e' {comune['nome']} che si trova a {comune['altitudine']} metri")

main()