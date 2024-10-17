def leggi_dati(nome_file):

    record_gate = {"not": [], "buf":[],"and":[], "nand":[], "or":[], "nor":[], "xor":[], "xnor":[]}
    
    # lista nomi dei diversi tipi di gate in ordine di chiave, li uso per controllare il numero di porte dato che è diverso per not e buf rispetto agli altri
    gate = list(record_gate.keys()) 

    nomi_utilizzati = []
    o_connessi = []
    i_connessi = []
    errori = []

    esiste = False
    
    while not esiste:

        try:

            nome_file = input("\nInserisci exit per chiudere o il nome del file: ")

            if nome_file == "exit":
                exit("chiusura programma...")

            with open(nome_file, "r", encoding="utf-8") as f:

                for i, riga in enumerate(f):
                    campi = riga.rstrip("\n").split()
                    
                    # controllo errori, se ci sono li registro e vado alla prossima riga del file

                    if campi[0] not in gate:
                        errori.append({"Gate sconosciuto": (campi[0], i+1)})
                        continue
                    
                    if campi[1] in nomi_utilizzati:
                        errori.append({"Nome già utilizzato": (campi[1], i+1)})
                        continue
                    
                    if (campi[0] in gate[:2]) and (len(campi[2:]) != 2):
                        errori.append({"Numero di net non valido": (len(campi[2:]), i+1)})
                        continue
                    
                    if campi[0] in gate[2:] and len(campi[2:]) < 3:
                        errori.append({"Numero di net non valido": (len(campi[2:]), i+1)})
                        continue

                    if campi[2] in o_connessi:
                        errori.append({"Net collegata a più output": (campi[2], i+1)})
                        continue
                    
                    # la riga non ha errori, registro i dati che mi servono e contrinuo

                    record_gate[campi[0]].append(len(campi[3:]))

                    nomi_utilizzati.append(campi[1])
                    o_connessi.append(campi[2])
                    i_connessi.extend(campi[3:])

            esiste = True

        except OSError:

            print(f"Il file {nome_file} non esiste, riprovare inserendo il nome corretto")


    return record_gate, o_connessi, i_connessi, errori


def controlla_in_out(lista_input, lista_output):

    output_circuito = []
    input_circuito = set()

    for inp in lista_input:
        if inp not in lista_output:
            input_circuito.add(inp)

    for out in lista_output:
        if out not in lista_input:
            output_circuito.append(out)

    return input_circuito, output_circuito


def conta_gate_input(record_gate):

    for gate in record_gate:

        if len(record_gate[gate]) > 1:

            inp_diversi = set(record_gate[gate])

            for inp in inp_diversi:
            
                print(f"{record_gate[gate].count(inp)} {gate} con {inp} input")

        elif len(record_gate[gate]) == 1:

            print(f"{len(record_gate[gate])} {gate}")


def main():

    # punto 1
    record_gate, o_connessi, i_connessi, errori = leggi_dati("c5315.txt")

    # punto 2
    input_circuito, output_circuito = controlla_in_out(i_connessi, o_connessi)

    # punto 3
    n_gate = sum([len(record_gate[gate]) for gate in record_gate])


    # punto 1
    print("\nRilevamento errori:\n")

    for errore in errori:

        [print(f"Riga {valore[1]}: {nome} ({valore[0]})") for nome, valore in errore.items()]

    print(f"\n{len(errori)} errori\n")


    # punto 2
    print(f"\nInput globali: {len(input_circuito)}\n")

    [print(net) for net in input_circuito]


    print(f"\nOutput globali: {len(output_circuito)}\n")

    [print(net) for net in output_circuito]


    # punto 3
    print(f"\nNumero di gate: {n_gate}\n")
    
    conta_gate_input(record_gate)
    

main()