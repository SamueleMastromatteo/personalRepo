def leggi_codici(nome_file):
    codici = {}
    with open(nome_file, "r", encoding="utf-8") as f:
        for riga in f:
            campi = riga.rstrip("\n").split(":")
            codici[campi[0]] = [seq for seq in campi[1].split(",")]

    return codici


def leggi_codifiche():
    codifiche = {}
    esiste = False
    while not esiste:
        try:
            nome_file = input("Digitare exit per uscire altrimenti Inserire il nome del file da decodificare: ")
            
            if nome_file == "exit":
                return exit("chiusura programma...")
            
            with open(nome_file, "r", encoding="utf-8") as f:
                righe = [riga.rstrip("\n") for riga in f]
                for i, riga in enumerate(righe):
                    if riga[0] == ">":
                        codifiche[riga] = righe[i+1].split()
            esiste = True

        except OSError:
            print(f"Il file inserito {nome_file} non esiste, riprovare")

    return codifiche


def decodifica_sequenza(codici, sequenza_codificata):
    decodifica = ""
    for tripletta in sequenza_codificata:
        for codice in codici:
            if tripletta in codici[codice] and codice != "STOP":
                decodifica += codice

    return decodifica


def scrivi_file(seq_decodificate):

    nome_file = input("Inserire il nome che desideri per il file decodificato o premere invio per chiamarlo proteins.txt: ")

    if nome_file == "":
        nome_file = "proteins.txt"
        
    with open(nome_file, "w", encoding="utf-8") as f:
        for i, seq in enumerate(seq_decodificate):

            f.write(f"{seq}\n")

            if i < len(seq_decodificate) - 1:
                f.write(f"{seq_decodificate[seq]}\n")

            else:
                f.write(seq_decodificate[seq])


def main():
    
    codici = leggi_codici("codicegenetico.txt")
    sequenze_codificate = leggi_codifiche()
    sequenze_decodificate = {sequenza:decodifica_sequenza(codici, sequenze_codificate[sequenza]) for sequenza in sequenze_codificate}
    scrivi_file(sequenze_decodificate)
            

main()