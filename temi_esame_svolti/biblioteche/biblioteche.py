from operator import itemgetter

def leggi_inventario(nome_file):
    inventario = []
    codici_isbn = []
    with open(nome_file, "r", encoding="utf-8") as f:
        for riga in f:
            campi = riga.rstrip("\n").split(";")
            if campi[1] not in codici_isbn:
                inventario.append({
                    "codici_copia": [campi[0]],
                    "ISBN": campi[1],
                    "titolo": campi[2],
                    "autore": campi[3]
                })

                codici_isbn.append(campi[1])

            else:
                for libro in inventario:
                    if campi[1] == libro["ISBN"]:
                        libro["codici_copia"].append(campi[0])

    return inventario


def regala_eccessi(inventario):
    regali = []
    for libro in inventario:
        if len(libro["codici_copia"]) > 3:
            copie_regalo = dict(libro)
            copie_regalo["codici_copia"] = copie_regalo["codici_copia"][3:]
            regali.append(copie_regalo)
            libro["codici_copia"] = libro["codici_copia"][:3]

    return regali


def scrivi_inventario(record_libri, nome_file):
    record_libri.sort(key=itemgetter("ISBN"))
    with open(nome_file,"w", encoding="utf-8") as f:
        for i, libro in enumerate(record_libri):
            f.write(f"{libro['ISBN']};{libro['autore']};{libro['titolo']};{';'.join(libro['codici_copia'])}")
            if i < len(record_libri)-1:
                f.write("\n")
                

def main():

    inventario = leggi_inventario("inventarioOLD.csv")
    regali = regala_eccessi(inventario)
    #scrivi_inventario(inventario, "inventarioNew.csv")
    #scrivi_inventario(regali, "inventarioScuola.csv")
    n_regali = len(regali)
    copie_tot = 0
    for libro in regali:
        copie_tot += len(libro["codici_copia"])
    print(f"\nNumero libri da regalare: {n_regali}, copie totali: {copie_tot}\n")

main()