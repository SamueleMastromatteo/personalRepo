# Scrivere un programma che legga tutte le righe di un file di testo input.txt, ne
# inverta l’ordine e le scriva in un altro file output.txt.



def leggi_file(input_file):
    with open(input_file, "r", encoding="utf-8")as i:
        righe = i.readlines()
        
    righe_invertite = righe[::-1]
    return righe_invertite

def scrivi_file(output_file, righe):
    with open(output_file, "w", encoding="utf-8") as o:
        for riga in righe:
            o.write(riga if riga.endswith("\n") else riga + "\n")
        
def main():
    righe_invertite = leggi_file("input.txt")
    scrivi_file("output.txt", righe_invertite)
    
if __name__ == "__main__":
    main()