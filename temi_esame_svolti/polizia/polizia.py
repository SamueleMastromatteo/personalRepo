def leggi_intercettazioni(nome_file):
    with open(nome_file, "r",encoding="utf-8") as f:
        testo = f.readlines()
    return testo

def censura(testo):
    with open("censurato.txt", "w", encoding="utf-8") as f:
        righe_nome = set()
        righe_sicure = []
        for i, riga in enumerate(testo):
            
            if "bob" in riga or "arctor" in riga:
                for n in range(i-2,i+3):
                    righe_nome.add(n)
    
        for i, riga in enumerate (testo):
            if i not in righe_nome:
                righe_sicure.append(riga)

        return f.writelines(righe_sicure)

def distanza_polizia(testo):
    righe_nome = set()
    righe_polizia = set()
    distanze = set()
    for i, riga in enumerate(testo):
        if "bob" in riga or "arctor" in riga:
            righe_nome.add(i)
        if "polizia" in riga:
            righe_polizia.add(i)
    if len(righe_nome) == 0 or len(righe_polizia) == 0:
        return None
    else:
        for i_nome in righe_nome:
            for i_polizia in righe_polizia:
                distanze.add(abs(i_polizia-i_nome))

        return min(distanze)


def main():
    testo = leggi_intercettazioni("intercettazione.txt")
    censura(testo)
    distanza = distanza_polizia(testo)
    if distanza == None:
        print("polizia e il nome non sono stati proncunciati assieme, non sei in pericolo")
    else:
        print(f"polizia è stato pronunciato a {distanza} righe di distanza dal nome")

main()
