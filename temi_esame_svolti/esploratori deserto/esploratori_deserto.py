import math
from operator import itemgetter

def leggi_oasi(nome_file):
    record_oasi = []
    with open(nome_file, "r", encoding="utf-8") as f:
        f.readline()
        for riga in f:
            campi = riga.rstrip("\n").split(",")
            if campi[2] == "oasis":
                record_oasi.append((int(campi[0]), int(campi[1])))
    
    return record_oasi


def leggi_partecipanti(nome_file):
    record_partecipanti = []
    with open(nome_file, "r", encoding="utf-8") as f:
        f.readline()
        for riga in f:
            campi = riga.rstrip("\n").split(",")
            pos = tuple([int(n) for n in campi[1:3]])
            max_strada = float(campi[3]) * int(campi[4])
            record_partecipanti.append({
                
                "id": int(campi[0]),
                "pos": pos,
                "km": max_strada
            })

    return record_partecipanti


def calcola_distanza(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def cerca_oasi(pos, strada_percorribile, lista_oasi):
    oasi = []
    for cord in lista_oasi:
        distanza = calcola_distanza(pos, cord)

        if distanza <= strada_percorribile:
            oasi.append((cord, distanza))
        
    if len(oasi) > 0:

        oasi.sort(key=itemgetter(1))

        return oasi[0][0] # cordinata oasi più vicina
    
    else:
        return -1


def cerca_uscita(pos, strada_percorribile):

    x, y = pos

       # uscita a destra                    # uscita a sinistra               # uscita in avanti                  # uscita dietro     
    if (x + strada_percorribile >= 499) or (x - strada_percorribile <= 0) or (y + strada_percorribile >= 499) or (y - strada_percorribile <= 0):
    
        return True
    
    else:

        return False
    
    
def main():
    
    cord_oasi = leggi_oasi("desert.csv")
    partecipanti = leggi_partecipanti("survivors.txt")
    
    morti = []
    sopravvissuti = []

    for partecipante in partecipanti:
        morto = False
        uscito = False
        oasi = list(cord_oasi)

        while not morto and not uscito:

            uscito = cerca_uscita(partecipante["pos"], partecipante["km"])

            if not uscito:

                pos = cerca_oasi(partecipante["pos"], partecipante["km"], oasi)
                
                if pos == -1:

                    morto = True

                else:

                    oasi.remove(pos)
                    partecipante["pos"] = pos
        
        if uscito:
            sopravvissuti.append(partecipante)
        
        if morto:
            morti.append(partecipante)
    
    print(f"\nSopravvissuti: {(len(sopravvissuti) / len(partecipanti)*100):.2f}%")

    print("\nRecupero salme esploratori\n")
    
    for morto in morti:
        print(f"<{morto['id']}>: {morto['pos']}")

    print()

main()