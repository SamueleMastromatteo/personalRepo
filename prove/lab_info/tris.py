# Scrivere un programma che giochi a tris. Il programma deve, ad ogni turno, visualizzare il tabellone 
# di gioco, chiedere in input all'utente le coordinate del prossimo segno (riga e colonna), invertire 
# i giocatori dopo ogni mossa e, finita la partita, decretare il vincitore o la condizione di parità.

def stampa_tabellone(tabellone):
    for riga in tabellone:
        print(" | ".join(riga))
        print("-" * 5)

def verifica_vittoria(tabellone, giocatore):
    # Verifica righe
    for riga in tabellone:
        vittoria = True
        for cella in riga:
            if cella != giocatore:
                vittoria = False
                break
        if vittoria:
            return True

    # Verifica colonne
    for col in range(3):
        vittoria = True
        for riga in range(3):
            if tabellone[riga][col] != giocatore:
                vittoria = False
                break
        if vittoria:
            return True

    # Verifica diagonali
    vittoria = True
    for i in range(3):
        if tabellone[i][i] != giocatore:
            vittoria = False
            break
    if vittoria:
        return True

    vittoria = True
    for i in range(3):
        if tabellone[i][2 - i] != giocatore:
            vittoria = False
            break
    if vittoria:
        return True

    return False

def main():
    tabellone = [[" " for _ in range(3)] for _ in range(3)]
    giocatore = "X"
    mosse = 0

    while mosse < 9:
        stampa_tabellone(tabellone)
        coordinate = input(f"Giocatore {giocatore} -> coordinate (riga,colonna): ")
        x, y = map(int, coordinate.split(","))
        
        if tabellone[x][y] == " ":
            tabellone[x][y] = giocatore
            mosse += 1

            if verifica_vittoria(tabellone, giocatore):
                stampa_tabellone(tabellone)
                print(f"Giocatore {giocatore} ha vinto!")
                return

            giocatore = "O" if giocatore == "X" else "X"
        else:
            print("Mossa non valida, riprova.")

    stampa_tabellone(tabellone)
    print("La partita è finita in parità.")

main()