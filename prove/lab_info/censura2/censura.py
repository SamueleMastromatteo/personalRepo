# Scrivere un programma 'censore', che legga un file (bad_words.txt) contenente
# una lista di 'parolacce' (come 'sesso', 'droga', 'C++' e così via), una per riga, inserendole in
# un insieme. Leggere poi un altro file di testo (raw_text.txt), che contenga occorrenze di alcune
# delle 'parolacce' in questione. Il programma deve riscrivere il secondo file, generandone un terzo
# (censored_text.txt) nel quale il contenuto sia lo stesso, ma con la differenza che tutte le
# occorrenze di parole e sotto-parole corrispondenti a 'parolacce' sono sostituite da un numero di
# asterischi ('*') pari alla loro lunghezza.

def leggi_bad(input_file):
    parolacce = []
    with open(input_file, "r", encoding="utf-8") as f:
        for riga in f:
            parole = riga.strip()
            parolacce.append(parole)            
    return parolacce
    
def leggi_testo(input_file):
    testo = []
    with open(input_file, "r", encoding="utf-8") as f:
        #legge riga
        for riga in f:
            parole = riga.split()
            #legge parola per parola e le mette in una lista
            for parola in parole:
                parola = parola.rstrip(".,?!")
                testo.append(parola)
    return testo

def scrivi_censure(output_file, parolacce, testo):
    censored_text = []
    for parola in testo:
        for bad in parolacce:
            if bad in parola:
                parola = '*' * len(parola)
                break
        censored_text.append(parola)
        
    with open(output_file, "w", encoding="utf-8") as f:
        for parola in censored_text:
            f.write(parola + ' ')
    
    
def main():
    parolacce = leggi_bad("bad_words.txt")
    testo = leggi_testo("raw_text.txt")
    scrivi_censure("censored_text.txt", parolacce, testo)
    
if __name__ == "__main__":
    main()