#.In questo gioco, due giocatori prelevano alternativamente biglie da un mucchietto. 
# Ad ogni mossa, un giocatore sceglie quante biglie prendere: almeno una e al massimo metà delle biglie disponibili.
# Il giocatore che prende l’ultima biglia perde la partita.

from random import randint
from math import log2

potenze2 = [3, 7, 15, 31]

num_biglie = randint(10,100)
#partenza = randint(0,1)
partenza = 0
intelligenza = randint(0,1)
print(f"intelligenza: {intelligenza}")


def computer(num_biglie):
    if intelligenza==0: #computer gioca in modo stupido
        computer_biglie = randint(1, int(num_biglie/2))
        num_biglie-=user_biglie
        print(f"il computer ha preso {computer_biglie} biglie")
    elif intelligenza==1: #computer gioca in modo intelligente
        if log2(num_biglie)-1: #verifico se è potenza di 2
            computer_biglie = randint(1, int(num_biglie/2))
            print(f"il computer ha preso {computer_biglie} biglie")
        else:
            i = randint(0,3)
            computer_biglie = potenze2[i]
            print(f"il computer ha preso {computer_biglie} biglie")
    num_biglie-=computer_biglie
    return num_biglie


if partenza==0: #parte prima l'utente
    if num_biglie <=1:
        print("hai perso!")
    while num_biglie>1:
        print(f"numero di biglie rimanenti: {num_biglie}")
        #utente
        user_biglie = int(input("inserisci numero di biglie: "))
        if user_biglie > (num_biglie/2):
            print("numero non valido")
            continue
        num_biglie-=user_biglie
        
        print(f"numero di biglie rimanenti: {num_biglie}")
        if num_biglie <=1:
            print("il computer ha perso!")
        #computer
        num_biglie = computer(num_biglie)
        
        

