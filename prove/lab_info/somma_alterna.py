# Scrivere un programma che riceva in input una sequenza di numeri interi (terminata da una riga vuota), e che calcoli la 
# somma alternata dei suoi elementi. Ad esempio, se il programma legge i dati 1 4 9 16 9 7 4 9 11, deve calcolare e 
# visualizzare 1 – 4 + 9 – 16 + 9 – 7 + 4 – 9 + 11 = –2.

def main():
    somma = 0
    i = 0
    while True:
        num_str = input("inserisci numero: ")
        if num_str == "":
            break
        num = int(num_str)
        if i % 2 == 0:
            somma += num
        else:
            somma -= num
        
        i+=1
            
    print(somma)
    
main()
        