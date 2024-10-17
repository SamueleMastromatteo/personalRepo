from operator import itemgetter


def leggi_schedine(nome_file):
    record_schedine = []
    with open(nome_file, "r", encoding="utf-8") as f:
        for riga in f:
            campi = riga.rstrip("\n").split(",")
            record_schedine.append({

                "id": campi[0],
                "numeri": [int(n) if n.isnumeric() else n for n in campi[1:7]],
                "prezzo": float(campi[-1])

            })

    return record_schedine


def leggi_vincente(nome_file):
    with open(nome_file, "r", encoding="utf-8") as f:
        vincente = [int(n) for n in f.readline().strip("\n").split()]

    return vincente


def leggi_premi(nome_file):
    premi = {}
    with open(nome_file, "r", encoding="utf-8") as f:
        for riga in f:
            campi = riga.rstrip("\n").split()

            if int(campi[0]) > 2:
                premi[int(campi[0])] = int(campi[1])
    
    return premi


def controlla_numeri(schedina, vincente):
    n_indovinati = []
    for n in schedina["numeri"]:

        if n == "*" or n in vincente:
            n_indovinati.append(n)

    return n_indovinati


def main():

    schedine = leggi_schedine("schedine.txt")
    vincente = leggi_vincente("vincente.txt")
    premi = leggi_premi("premi.txt")

    vincitori = []

    incasso = 0.0
    spesa_premi = 0.0
    
    print("\nSchedine Vincenti:\n")

    for schedina in schedine:
        numeri = controlla_numeri(schedina, vincente)
        incasso += schedina["prezzo"]

        if len(numeri) > 2:
            schedina["n_indovinati"] = [str(n) for n in numeri]
            schedina["tipo_premio"] = len(numeri)
            schedina["vincita"] = premi[len(numeri)]
            vincitori.append(schedina)
    
    vincitori.sort(key=itemgetter("tipo_premio"), reverse=True)

    for schedina in vincitori:

        print(f"ID_SCHEDINA: {schedina['id']} NUMERI_INDOVINATI: {' '.join(schedina['n_indovinati'])} VINCITA: {schedina['vincita']}  TIPO PREMIO: {schedina['tipo_premio']}")

        spesa_premi += schedina["vincita"]

    print(f"\nGuadagno netto degli organizzatori: {(incasso - spesa_premi):.1f} euro\n")


main()