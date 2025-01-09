clienti = []
coda_clienti = []

def aggiungi_cliente(coda):
   for i in range(coda):
       id_cliente = int(input("inserisci un numero cliente: "))
       if id_cliente not in clienti:
           clienti.append(id_cliente)
           servi_cliente(clienti[i])
       else:
           print(f"cliente {id_cliente} già inserito")
           id_cliente = int(input("inserisci un numero cliente: "))

   return clienti

def servi_cliente(coda):
    print(f"serviamo il cliente {coda}")
    clienti.pop(coda)

def main():
   num_clienti = int(input("quanti clienti vuoi inserire? "))
   aggiungi_cliente(num_clienti)
   print(f"coda: {clienti}")
   #servi_cliente(clienti)

main()
