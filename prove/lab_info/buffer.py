# Programma che, data una lista, sposta gli elementi avanti di una unità,
# e che sposti l'ultimo elemento in prima posizione.

list = [1, 2, 3, 4, 5]


# Spostare l'ultimo elemento in prima posizione e gli altri elementi avanti di una posizione
def shift_list(lista):
    if len(lista) > 0:
        last_element = lista.pop()  # Rimuove l'ultimo elemento
        lista.insert(0, last_element)  # Inserisce l'ultimo elemento in prima posizione
    return lista

shifted_list = shift_list(list)
print(shifted_list)