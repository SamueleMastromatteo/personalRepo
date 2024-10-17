def leggi_stabilimento(nome_file):
    stabilimento = []
    with open(nome_file, "r", encoding="utf-8") as f:
        for riga in f:
            campi = riga.rstrip("\n").split(",")
            stabilimento.append({

                "n_ombrelloni": int(campi[0]),
                "costo_ombrelloni": int(campi[1]),
                "n_sedie": int(campi[2]),
                "costo_sedie": int(campi[3])

            })
    
    return stabilimento


def leggi_clienti(nome_file):
    log_clienti = []
    clienti_registrati = []
    with open(nome_file, "r", encoding="utf-8") as f:
        for riga in f:
            campi = riga.rstrip("\n").split(",")
            if campi[0] not in clienti_registrati:
                log_clienti.append([campi[0], int(campi[1]), int(campi[2]), int(campi[3])])
                clienti_registrati.append(campi[0])
            else:
                log_clienti.append([campi[0]])

    return log_clienti


def cerca_fila(cliente, stabilimento):

    for i, fila in enumerate(stabilimento):

        if cliente[1] <= fila["n_ombrelloni"] and cliente[2] <= fila["n_sedie"]:
            spesa_fila = (cliente[1] * fila["costo_ombrelloni"]) + (cliente[2] * fila["costo_sedie"])
            

            if spesa_fila <= cliente[3]:
                return (i+1), spesa_fila
            
    return False, False
            

def main():

    stabilimento = leggi_stabilimento("stabilimento.txt")
    dati_clienti = leggi_clienti("ingressi-uscite.txt")
    clienti_ospitati = dict() # dict con i clienti entrati con chiave cliente e valori lista di questo tipo [n_fila, n_ombrelloni, n_sedie, spesa]
    incasso_giornata = 0

    print()

    for cliente in dati_clienti:

        if len(cliente) != 1:

            # cliente entra

            # se la funzione non trova una fila adatta restituisce tupla(False, False)
            fila_trovata, spesa = cerca_fila(cliente, stabilimento)  
            
            if fila_trovata == False:
                # non è possibile soddisfare la richiesta del cliente
                print(f"Il cliente {cliente[0]} non ha trovato posto")

            else:
                # aggiungo al dict clienti ospitati i dati che mi servono 
                clienti_ospitati[cliente[0]] = [fila_trovata, cliente[1], cliente[2], spesa] 
                # dato che la fila è stata trovata sottraggo dalla fila trovata in stabilimento gli ombrelloni e le sedie disponibili che sono state prese dal cliente
                stabilimento[fila_trovata-1]["n_ombrelloni"] -= cliente[1]
                stabilimento[fila_trovata-1]["n_sedie"] -= cliente[2]
                incasso_giornata += spesa
                print(f"Il cliente {cliente[0]} è in fila {fila_trovata}")

        else:

            # cliente esce 

            print(f"Il cliente {cliente[0]} è uscito")
            
            # dopo che il cliente esce devo riaggiungere a stabilimento gli ombrelloni e le sedie precedentemente occupati dal cliente
            stabilimento[clienti_ospitati[cliente[0]][0]-1]["n_ombrelloni"] += clienti_ospitati[cliente[0]][1]
            stabilimento[clienti_ospitati[cliente[0]][0]-1]["n_sedie"] += clienti_ospitati[cliente[0]][2]

    print(f"\nL'incasso della giornata è {incasso_giornata}€\n")

main()