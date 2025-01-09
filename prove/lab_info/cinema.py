num_biglietti = 10
i = 0
while num_biglietti > 0:
    
    num_acquistati = int(input("Quanti biglietti vuoi acquistare? (max 4) "))
    if num_acquistati > 4:
        print("Puoi acquistare al massimo 4 biglietti.")
        continue
    
    if num_acquistati <= num_biglietti:
        print("Biglietti acquistati")
        i+=1
        num_biglietti -= num_acquistati
    else:
        print("Biglietti non disponibili")
        continue
    print("Biglietti disponibili: ", num_biglietti)

print("acquirenti: ", i)