# Scrivere un programma che permetta di giocare più partite a parole concatenate. Per 
# semplicità, si considerino tutte le sillabe di 2 caratteri. Il gioco finisce quando un
# giocatore non trova la parola o sbaglia a concatenarla

i = 0
parole = []
perso = False
while True:
    print("inizia una nuova partita! ")
    
    if i%2 == 0:
        parola = input("giocatore 1 -> ")
        for p in parole:
            if parola == p:
                print("giocatore 1 ha perso!")
                perso = True
                break
