from operator import itemgetter


def leggi_menu(nome_file):
    with open(nome_file, "r", encoding="utf-8") as file:
        menu = []
        for riga in file:
            campi = riga.strip("\n").split(",")
            campi = [elemento.strip() for elemento in campi]
            menu.append({
                "ID": campi[0],
                "DESCRIZIONE": campi[1],
                "COSTO_UNITARIO": float(campi[2]),
                "IVA": float(campi[3])
            })
    return menu


def genera_ricevuta(menu, lista_ordine):
    ricevuta = []
    for ordine in lista_ordine:
        codice_prodotto = ordine[0]
        quantita_prodotto = int(ordine[1])
        for prodotto in menu:
            if codice_prodotto == prodotto["ID"]:
                ricevuta.append({
                    "quantita": quantita_prodotto,
                    "descrizione": prodotto["DESCRIZIONE"],
                    "tot_prezzo": prodotto["COSTO_UNITARIO"] * quantita_prodotto,
                    "iva_applicata": prodotto["IVA"]
                })
                
    ricevuta.sort(key=itemgetter("iva_applicata"))
    return ricevuta


def main():

    menu_letto = leggi_menu("menu.txt")

    with open("ordine.txt", "r", encoding="utf-8") as ordine:
        lista_ordine = []
        for elemento in ordine:
            campi_ordine = elemento.strip("\n").split(",")
            lista_ordine.append(campi_ordine)

    ricevuta = genera_ricevuta(menu_letto, lista_ordine)
    totale = 0
    imponibile = 0

    for prodotto in ricevuta:
        print(f"{prodotto['quantita']:3d} {prodotto['descrizione']:25s} {prodotto['tot_prezzo']:5.2f} IVA {prodotto['iva_applicata']:5.2f}%")
        totale += prodotto["tot_prezzo"]
        imponibile += (100*prodotto["tot_prezzo"])/(100+prodotto["iva_applicata"])
    totale_iva = totale - imponibile

    print(f"  Totale: {totale:.2f}€\n  Di cui IVA: {totale_iva:.2f}€")


main()
