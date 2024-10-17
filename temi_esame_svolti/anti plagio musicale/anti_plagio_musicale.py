def leggi_brani(nome_file):
    brani = []
    with open(nome_file, "r", encoding="utf-8") as f:
        for riga in f:
            campi = riga.strip("\n").split(":")
            record = {
                "nome": campi[0],
                "note": campi[1].split(),
            }
            record["note"] = [int(n) for n in record["note"]]
            brani.append(record)
    return brani

def controlla(brano1,brano2):
    # brano1 consiste nel brano attuale che sto confrontando con tutti quelli venuti prima (brano2)

    # controllo PLAGIO 
    if brano1["note"] == brano2["note"]:
        print(f"{brano1['nome']} è un PLAGIO di {brano2['nome']}")

    else:
        # controllo COPIATURA
        copiatura = False
        # queste due istruzioni qua sotto suddividono la lista di note in una lista di liste, in cui ogni sotto_lista è una sequenza di 4 note,
        # le sotto liste sono composte ad esempio in questo modo:
        # se lista principale [1,2,3,4,5,6,7,8,9,0]
        # seq_lista sarà [[1,2,3,4], [2,3,4,5], [3,4,5,6], [4,5,6,7], [5,6,7,8] ... [7,8,9,0]] le liste che non arrivano a 4 elementi sono escluse da seq_lista
        seq_brano1 = [brano1["note"][n:n+4] for n in range(0, len(brano1["note"])) if len(brano1["note"][n:n+4]) == 4]
        seq_brano2 = [brano2["note"][n:n+4] for n in range(0, len(brano2["note"])) if len(brano2["note"][n:n+4]) == 4]
        
        for seq in seq_brano1:
            if seq in seq_brano2:
                copiatura = True
        if copiatura:
            print(f"{brano1['nome']} è una COPIATURA di {brano2['nome']}")

        else:
            sospetto = False
            # controllo SOSPETTO
            for seq1 in seq_brano1:
                for seq2 in seq_brano2:
                    diff = []
                    for i in range(4):
                        diff.append(seq1[i] - seq2[i])
                    if len(set(diff)) == 1:
                        sospetto = True

            if sospetto:
                print(f"{brano1['nome']} è un SOSPETTO di {brano2['nome']}")

def main():
    
    brani = leggi_brani("brani.txt")
    for brano1 in range(len(brani)):
        for brano2 in range(brano1):
            controlla(brani[brano1], brani[brano2])

main()
