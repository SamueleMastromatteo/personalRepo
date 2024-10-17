def leggi_abitazioni(nome_file):
    stanze = []
    with open(nome_file, "r", encoding="utf-8") as f:
        for riga in f:
            stanze.extend([stanza for stanza in riga.rstrip("\n").split() if stanza != "-"])
            
    return stanze
        
def leggi_temperature(nome_file):
    temperature = []
    with open(nome_file, "r", encoding="utf-8") as f:
        for riga in f:
            temperature.extend([float(temp) for temp in riga.rstrip("\n").split() if temp != "-"])

    return temperature

def gestisci_stanze(stanze, temperature):
    record = {}
    for i, cod_stanza in enumerate(stanze):
        if cod_stanza not in record:
            record[cod_stanza] = [temperature[i]]
        else:
            record[cod_stanza].append(temperature[i])

    return dict(sorted(record.items())) # ordino con sorted il dizionario in ordine alfabetico di chiavi e riconverto in dizionario con dict

def stampa_dati_stanze(record_stanze):
    print("\nStanza T.Min T.Max T.Media")
    for stanza in record_stanze:
        t_max = max(record_stanze[stanza])
        t_min = min(record_stanze[stanza])
        t_med = (sum(record_stanze[stanza])/len(record_stanze[stanza]))
        print(f"{stanza:<6s}  {t_min:4.1f}  {t_max:4.1f}  {t_med:4.1f}")

def main():
    stanze = leggi_abitazioni("mappa.txt")
    temperature = leggi_temperature("temperature.txt")
    escursione_termica = (max(temperature) - min(temperature))
    stanze_gestite = gestisci_stanze(stanze, temperature)
    stampa_dati_stanze(stanze_gestite)
    print(f"\nEscursione termica: {escursione_termica:.1f} gradi\n")

main()