# Scrivere una funzione merge(a, b) che unisca le due liste a e b, alternando un elemento della prima 
# e un elemento della seconda. Se una lista è più corta dell’altra, gli elementi vengono alternati fin 
# quando è possibile, poi gli elementi rimasti nella lista più lunga vengono aggiunti, in ordine, in 
# fondo. Le liste di partenza non devono essere modificate. Se, ad esempio, il contenuto di a è 
# 1 4 9 16 e il contenuto di b è 9 7 4 9 11, l’invocazione di merge(a, b) restituisce una nuova lista 
# contenente i valori 1 9 4 7 9 4 16 9 11.

list1 = [1, 4, 9, 16]
list2 = [9, 7, 4, 9, 11]

def merge(a, b):
    final = []
    
    if len(a) > len(b):
        for i in range(len(a)):
            final.append(a[i])
            if len(b)>i:
                final.append(b[i])
    else:
        for i in range(len(b)):
            if len(a)>i:
                final.append(a[i])
            final.append(b[i])
    final_str = ' '.join(map(str, final))
    print(final_str)
    
merge(list1, list2)