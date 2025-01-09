# Scrivere la funzione same_set(a, b) che verifichi se due liste contengono gli stessi elementi, indipendentemente dall’ordine e ignorando 
# la presenza di duplicati. Ad esempio, le due liste [1 4 9 16 9 7 4 9 11] e [11 11 7 9 16 4 1] devono essere considerate uguali. La 
# funzione non deve modificare le liste che sono state passate come parametri.


list1 = [1, 4, 9, 16, 9, 7, 4, 9, 11]
list2 = [11, 11, 7, 9, 16, 4, 1]

def same_set(a, b):
    if set(a) == set(b):
        print("liste uguali")
    else:
        print("liste diverse")

same_set(list1, list2)