def leggi_calendario(nome_file):
    with open(nome_file, "r", encoding="utf-8") as f:
        calendario = [riga.rstrip("\n") for riga in f]

    return calendario

def leggi_occupazioni(nome_file, calendario):
    occupazioni = []
    with open(nome_file, "r", encoding="utf-8") as f:
        f.readline()
        for riga in f:
            campi = riga.rstrip("\n").split(";")
            arrivo = int(calendario.index(campi[1]))
            partenza = int(calendario.index(campi[2]))
            occupazioni.append({
                "id_cliente": campi[0],
                "arrivo": arrivo,
                "partenza": partenza,
                "n_notti": abs(partenza - arrivo),
                "alloggio": campi[3],
                "n_persone": int(campi[4]) + int(campi[5]), 
                "elettricita": campi[6]         
            })

    return occupazioni

def leggi_prezzi(nome_file, calendario):
    prezzi = []
    with open(nome_file, "r", encoding="utf-8") as f:
        f.readline()
        for riga in f:
            campi = riga.rstrip("\n").split(";")
            inizio_periodo = int(calendario.index(campi[0]))
            fine_periodo = int(calendario.index(campi[1]))
            prezzi.append({
                "periodo": [n for n in range(inizio_periodo, fine_periodo + 1)],
                "p_tenda": float(campi[2]),
                "p_camper": float(campi[3]),
                "p_persona": float(campi[4]),
                "p_elettricita": float(campi[5])
            })

    return prezzi

def main():

    calendario = leggi_calendario("calendario.txt")
    log_occupazioni = leggi_occupazioni("occupazione.txt", calendario)
    listino_prezzi = leggi_prezzi("prezzi.txt", calendario)
    for cliente in log_occupazioni:
        prezzo_totale = 0.0
        for giorno in range(cliente["arrivo"], cliente["partenza"]):
            for prezzo in listino_prezzi:
                if giorno in prezzo["periodo"]:
                    prezzo_giorno = 0.0
                    if cliente["alloggio"] == "tenda":
                        prezzo_giorno += prezzo["p_tenda"]
                    elif cliente["alloggio"] == "camper":
                        prezzo_giorno += prezzo["p_camper"]
                    if cliente["elettricita"] == "sì":
                        prezzo_giorno += prezzo["p_elettricita"]
                    
                    prezzo_totale += prezzo_giorno + (prezzo["p_persona"] * cliente["n_persone"])

        cliente["spesa_tot"] = prezzo_totale
        
        print(f"cliente: {cliente['id_cliente']}, arrivo: {calendario[cliente['arrivo']]}, partenza {calendario[cliente['partenza']]}, tipo: {cliente['alloggio']}, persone: {cliente['n_persone']}, elettricità: {cliente['elettricita']}, prezzo: {cliente['spesa_tot']}, numero notti: {cliente['n_notti']} ")

main()