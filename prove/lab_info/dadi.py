# Programma che genera sequenza di 20 lanci di dadi, li memorizzi in una lista e visualizzi i valori generati, contrassegnando tra parentesi la serie di valori
# identici più lunga. Se sono presenti più sequenze di lunghezza massima, si metta tra parentesi la prima

import random

def sequenza():
    seq = []
    for i in range(20):
        rand = random.randint(1,3)
        seq.append(rand)
        
    serie_max = 1
    serie_attuale = 1
    index_max_inizio = 0
    index_attuale = 0
    
    for i in range (len(seq)):
        if i>0:
            if seq[i] == seq[i-1]:
                serie_attuale +=1
                
            else:
                if serie_attuale > serie_max:
                    serie_max = serie_attuale
                    index_max_inizio = index_attuale
                serie_attuale = 1
                index_attuale = i
           
    #verifico l'ultima sequenza 
    if serie_attuale > serie_max:
        serie_max = serie_attuale
        index_max_inizio = index_attuale
        
    output = []
    for i in range(len(seq)):
        if i == index_max_inizio:
            output.append('(')
        output.append(str(seq[i]))
        
        if i == index_max_inizio + serie_max -1:
            output.append(')')
        seq_str = ' '.join(output)

    print(seq_str)
        
    
sequenza()
    