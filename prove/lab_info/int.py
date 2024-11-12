

scelta = int(input("scelta: "))
if scelta==1:
    somma = 0
    numero=0
    pari=0
    dispari=0
    while True:
        input_str = input("Inserisci un numero intero (lascia vuoto per terminare): ")
        if input_str == "":
            break
        try:
            if int(input_str)>numero:
                numero_max = int(input_str)
            elif int(input_str)<numero:
                numero_min = int(input_str)
            numero = int(input_str)
            
            if numero%2:
                pari+=1
            else:
                dispari+=1
            
            somma += numero
            print(f"Somma attuale: {somma}")
            
        except ValueError:
            print("Per favore, inserisci un numero intero valido.")

    print(f"Somma finale: {somma}, valore massimo: {numero_max}, valore minimo: {numero_min}, pari:{pari}, dispari: {dispari}")

#numeri primi 
elif scelta == 2:
    numero= int(input("numero: "))
    n=numero-1
    primo=True
    while n>1:
        if numero%n == 0:
            primo = False
            break
        n-=1
    if primo:
        print("numero primo")
    else:
        print("numero non primo")
    
    #numeri primi precedenti al numero in input
    while numero>1:
        numero-=1
        n=numero-1
        primo=True
        while n>1:
            if numero%n == 0:
                primo = False
                break
            n-=1
        if primo:
            print(numero)

