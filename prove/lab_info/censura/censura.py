# Scrivere un programma 'censore', che legga un file (bad_words.txt) contenente una lista di 
# 'parolacce' (come 'sesso', 'droga', 'C++' e così via), una per riga, inserendole in un 
# insieme. Leggere poi un altro file di testo (raw_text.txt), che contenga occorrenze di alcune
# delle 'parolacce' in questione. Il programma deve riscrivere il secondo file, generandone un 
# terzo (censored_text.txt) nel quale il contenuto sia lo stesso, ma con la differenza che tutte
# le occorrenze di parole e sotto-parole corrispondenti a 'parolacce' sono sostituite da un 
# numero di asterischi ('*') pari alla loro lunghezza.

def leggi_parolacce(input_file):
    parolacce = set()
    with open(input_file, "r", encoding="utf-8") as p:
        for riga in p:
            parolacce.add(riga.strip())
    return parolacce
        
def leggi_testo(input_file):
    testo = set()
    with open(input_file, "r", encoding="utf-8") as t:
        for riga in t:
            testo.add(riga.split(" "))
            #testo.append(riga.strip().split(" "))
            #print(testo)
        print(testo)
    return testo
        
def scrivi_censure(output_file, parolacce, testo):
    for parola in range(len(testo)):
        #print(testo[parola])
        for bad in parolacce:
            if testo[parola] == bad:
                #print(bad)
                testo[parola] == len(bad)*"*"
    print(testo)
    
def main():
    parolacce = leggi_parolacce("bad_words.txt")
    testo = leggi_testo("raw_text.txt")
    scrivi_censure("censored_text.txt", parolacce, testo)
    
if __name__ == "__main__":
    main()