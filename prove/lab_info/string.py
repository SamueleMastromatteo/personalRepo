scelta = int(input("scelta: "))
if scelta==1:
    s = input("inserisci una stringa: ")
    vocali= "aeiouAEIOU"

    #maiuscole
    for i in s:
        if i.isupper():
            print(i, end='')

    #pari    
    for i in range(0, len(s), 2):
        print(s[i], end='')

    #vocali e posizione vocali
    for i in range(len(s)):
        if s[i] in vocali:
            print(f"{s[i]} in posizione {i}")
            
    #numeri
    for i in s:
        if i.isnumeric:
            print(i, end='')

elif scelta==2:
    #parola al contrario
    word = input("inserisci parola: ")

    word_len = len(word)
    reversed_word = word[::-1]  # with string slicing, negative step
    print(reversed_word)
    
    for s in reversed_word:
        if s.isupper():
            print(s, end='')

#Scrivere un programma che legga una parola e visualizzi tutte le sue sottostringhe, ordinate per lunghezza crescente
elif scelta==3:
    str = input("stringa: ")
    # Generate and display all substrings ordered by increasing length.
for length in range(1, len(str) + 1):
    for pos in range(0, len(str) - length + 1):  # all starting positions of substrings of length 'length'
        print(str[pos: pos + length])