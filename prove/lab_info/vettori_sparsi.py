# Un vettore sparso è una sequenza di numeri, la maggior parte dei quali è 0.
# Un modo efficiente per memorizzare un vettore sparso è un dizionario, nel quale le chiavi sono le
# posizioni in cui sono presenti i soli valori diversi da zero, e i valori sono i corrispondenti valori nella
# sequenza. Per esempio, la sequenza 0 0 0 0 0 4 0 0 0 2 9 sarebbe rappresentata dal
# dizionario {5:4, 9:2, 10:9}. Scrivere una funzione, sparse_array_sum(a, b), i cui
# argomenti sono due dizionari di questo tipo, a e b. La funzione, senza modificare i dizionari passati
# come argomenti, deve restituire il loro vettore somma come un vettore sparso, dove un valore nella
# posizione i è la somma dei valori di a e b nelle rispettive posizioni i.

def sparse_array_sum(a, b):
    somma = {}

    for key in a:
        if key in b:
            somma[key] = a[key] + b[key]
        else:
            somma[key] = a[key]
            
    for key in b:
        if key not in somma:
            somma[key] = b[key]
            
    return somma
    
    
def main():
    a = {3:4, 5:8, 6:9}
    b = {2:3, 3:1, 6:10}
    
    result = sparse_array_sum(a, b)
    print(result)
    
if __name__ == "__main__":
    main()