#questa funzione leggerà il file organizzandolo in un dizionario, ignorerò l'opzione della data considerato che il file è ordinato già cronologicamente
from operator import itemgetter


def leggi_registrazioni(nome_file): 
    registrazioni = []
    with open(nome_file, "r", encoding="utf-8") as f:
        for riga in f:
            campi = riga.rstrip("\n").split(":")
            registrazioni.append({

                "pc": campi[0],
                "dipendente": campi[1] 

            })

    return registrazioni

def leggi_parco_pc(nome_file):
    with open(nome_file, "r", encoding="utf_8") as f:
        parco_pc = [riga.rstrip("\n") for riga in f]
    return parco_pc


def gestione_pc(parco_pc, registrazioni):
    disponibili = list(parco_pc)
    occupati = []
    for log in registrazioni:
        pc, dipendente = (log["pc"], log["dipendente"])

        if pc in disponibili and (pc, dipendente) not in occupati:
            occupati.append((pc,dipendente))
            disponibili.remove(pc)
        elif (pc,dipendente) in occupati:
            occupati.remove((pc,dipendente))
            disponibili.append(pc)
    occupati.sort(key=itemgetter(0))
                  
    return sorted(disponibili), occupati



def main():
    parco_pc = leggi_parco_pc("parcoPC.txt")
    registrazioni = leggi_registrazioni("registrazioni.txt")
    disponibili, occupati = gestione_pc(parco_pc, registrazioni)
    dipendenti = sorted(set([coppia[1] for coppia in occupati]))

    print("\nElenco dei prestiti in corso: ")

    for dipendente in dipendenti:
        pc = []
        for log in occupati:
            if dipendente in log:
                pc.append(log[0])
        print(f"{dipendente}: {', '.join(pc)}")
        

    if len(disponibili) != 0:
        print(f"\nPC disponibili per il prestito: {', '.join(disponibili)}\n")
    else:
        print("Al momento non ci sono PC disponibili per il prestito")

main()