# Un supermercato vuole ricompensare il proprio miglior cliente del giorno, mostrandone il nome 
# su uno schermo all’interno del negozio. Vengono memorizzati in una lista (customers) i nomi 
# di tutti i clienti del giorno e, in una lista (sales), l’importo della spesa effettuata da 
# ciascuno di loro. Scrivere la funzione name_of_best_customer(sales, customers) che restituisca
# il nome del cliente che ha speso la cifra più alta. Poi, scrivere un programma che chieda al 
# cassiere di digitare tutti gli importi spesi e i nomi dei relativi clienti, aggiungendoli, 
# dopo ciascuna acquisizione, a due liste distinte, per poi invocare la funzione progettata e 
# visualizzare il risultato. Usate l'importo 0 come sentinella. 

clienti = []
importi = []
sentinella = 0

def name_of_best_customers(sales, customers):
    massimo = max(sales)
    massimo_indice = sales.index(massimo)
    print(f"il miglior cliente è: {customers[massimo_indice]}, con una spesa di: {massimo}")
    
    
def main():
    while True:
        importo = int(input("inserire importo (0 per terminare): "))
        if importo == sentinella:
            break
        nome = input("inserire nome cliente: ")
        
        importi.append(importo)
        clienti.append(nome)
    name_of_best_customers(importi, clienti)
    
main()