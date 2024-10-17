LETTERE = "ABCDEFGHIJ"

def leggi_campo():
    campo = []
    errato = True
    while errato:
        try:
            nome_file = input("Inserire exit per chiudere il programma altrimenti Inserire il nome del file con le navi: ")
            
            if nome_file == "exit":
                return exit("chiusura programma...")

            with open(nome_file, "r", encoding="utf-8") as f:
                righe = f.readlines()
                for riga in righe:
                    valori = []
                    for valore in riga.rstrip("\n").split(","):
                        if valore.isnumeric():
                            valori.append(int(valore))
                        elif valore == "":
                            valori.append(0)
                        else:
                            exit("problema con formato file")

                    campo.append(valori)

            errato = False

        except OSError:
            print(f"Il file inserito {nome_file} non esiste")

    return campo


def leggi_mosse(nome_file):
    mosse = []
    with open(nome_file, "r", encoding="utf-8") as f:
        for riga in f:
            campi = riga.rstrip("\n").split(",")
            mosse.append((campi[0], int(campi[1])))
    return mosse


def gioca_turno(tabella, cord_riga, cord_colonna):

    tabella_avversario = list(tabella)

    if tabella_avversario[cord_riga][cord_colonna] == 0:
        print("Acqua\n")
        tabella_avversario[cord_riga][cord_colonna] = "o"
    else:
        print("Colpito\n")
        tabella_avversario[cord_riga][cord_colonna] = "*"
    
    return tabella_avversario


def stampa_matrice(tabella):

    print(f"  | 1| 2| 3| 4| 5| 6| 7| 8| 9|10|\n{'_'*33}")

    for riga in tabella:
        print(f"\n{LETTERE[tabella.index(riga)]}", end=" |")
        for valore in riga:
            if str(valore).isdigit():
                print(" ", end=" |")
            else:
                print(valore, end=" |")

        print(f"\n{'_'*33}")
           
            
def controlla_navi(tabella):
    for riga in tabella:
        if 1 in riga or 2 in riga:
            return True
    else:
        return False


def main():
    ancora_navi = True
    print("Giocatore 1")
    #campo_p1 = leggi_campo("navi1.txt")
    campo_p1 = leggi_campo()
    print("Giocatore 2")
    #campo_p2 = leggi_campo("navi2.txt")
    campo_p2 = leggi_campo()
    mosse = leggi_mosse("mosse.txt")
    n_mossa = 0

    while ancora_navi and n_mossa < len(mosse) :

        r, c = mosse[n_mossa] # riga e colonna mossa attuale

        if n_mossa % 2 == 0:

            print(f"\nE' il turno del giocatore 1\nCoordinate dell'attacco: {r}, {c}")
            esito_turno_p1 = gioca_turno(campo_p2, LETTERE.index(r), c-1)
            stampa_matrice(esito_turno_p1)
            campo_p2 = esito_turno_p1
            ancora_navi = controlla_navi(campo_p2)
            if not ancora_navi:
                print("\nGiocatore 1 ha affondato tutte le navi del suo avversario\n")

        else:
            print(f"\nE' il turno del giocatore 2\nCoordinate dell'attacco: {r}, {c}")
            esito_turno_p2 = gioca_turno(campo_p1, LETTERE.index(r) , c-1)
            stampa_matrice(esito_turno_p2)
            campo_p1 = esito_turno_p2
            ancora_navi = controlla_navi(campo_p1)
            if not ancora_navi:
                print("\nGiocatore 2 ha affondato tutte le navi del suo avversario\n")
            
        n_mossa += 1

    if ancora_navi:
        print("\nLa partita è sospesa a causa dell'esaurimento delle mosse\n")
    

main()