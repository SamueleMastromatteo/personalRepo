# Scrivere un programma che riceva in input una sequenza di valori reali e visualizzi un grafico a 
# barre che li rappresenti, usando asterischi (*) per disegnare le barre. L’output deve seguire il 
# seguente formato:
# **********************
# ****************************************
# ****************************
# **************************
# **************
# Assumere che tutti i valori nella sequenza di input siano positivi. Come primo passo, identificare il
# valore massimo. La barra che lo rappresenta deve essere composta di 40 asterischi. Le barre più corte
# devono usare un numero di asterischi proporzionale a questo per rappresentare i valori restanti.

list = []

while True:
    valore_str = input("numero: ")
    if valore_str == "":
        print()
        break
    valore = int(valore_str)
    
    list.append(valore)
    
massimo = max(list)
massimo_ast = 40

minimo = min(list)
minimo_ast = 0


for i in range(len(list)):
    ast = int((list[i] * massimo_ast) / massimo)
    if list[i] == minimo:
        minimo_ast = ast
    
    if minimo < 0:
        if list[i] < 0:
            print((ast*-1)*"*")
        elif list[i]>= 0:
            print((minimo_ast*-1)*" " + ast*"*")
    elif minimo >= 0:
        print(ast*"*")
