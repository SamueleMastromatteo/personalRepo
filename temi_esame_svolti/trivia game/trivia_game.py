import random
from operator import itemgetter


def leggi_domande(nome_file):

    domande = []

    try:

        with open(nome_file, "r", encoding="utf-8") as f:

            righe = f.readlines()
            domanda = list()

            for riga in righe:

                if riga != "\n":
                    domanda.append(riga.rstrip("\n"))

                else:
                    domande.append(domanda)
                    domanda = list()
                    continue

            domande.append(domanda) # inserisco l'ultima domanda del file

    except OSError:

        exit(f"Il file {nome_file} non esiste, controllare che sia presente o che il nome sia corretto")

    return domande


def organizza_domande(lista_domande): # raggruppo le domande per difficoltà

    record_domande = {}

    for domanda in lista_domande:
        if domanda[1] not in record_domande:
            record_domande[domanda[1]] = [{"domanda": domanda[0], "risposte":domanda[2:], "corretta": domanda[2]}]

        else:
            record_domande[domanda[1]].append({"domanda": domanda[0], "risposte": domanda[2:], "corretta": domanda[2]})

    # restituisco dizionario ordinato per ordine crescente di chiavi, difficoltà in questo caso

    return dict(sorted(record_domande.items())) 


def leggi_punti(nome_file): # leggo il file punti per sapere i punteggi e i nick precedenti poi lo riscriverò per modificarlo con i dati aggiornati

    record_punti = {}

    try:

        with open(nome_file, "r", encoding="utf-8") as f:

            for riga in f:

                campi = riga.rstrip("\n").split()

                record_punti[campi[0]] = int(campi[1])

    except OSError:

        exit(f"Il file {nome_file} non esiste, controllare che sia presente o che il nome sia corretto")

    return record_punti


def gioca_partita(domande_organizzate):

    nickname = input("\nInserisci il tuo nickname: ")

    punteggio = 0

    risposte_valide = [1,2,3,4]

    
    for livello in domande_organizzate:

        valida = False

        domanda_scelta = random.choice(domande_organizzate[livello])

        print(f"\nLivello {livello}) {domanda_scelta['domanda']}\n")

        random.shuffle(domanda_scelta["risposte"]) 

        [print(f"{i+1}. {risposta}") for i, risposta in enumerate(domanda_scelta["risposte"])]

        
        while not valida:

            try:

                risposta = int(input("\nInserisci la risposta: "))

                if risposta in risposte_valide:
                    valida = True

                else:
                    raise ValueError
                
            except ValueError:

                print("\nriprovare, la risposta inserita non è valida devi inserire il numero corrispondente alla risposta")


        risposta_scelta = domanda_scelta["risposte"][risposta - 1]


        if risposta_scelta == domanda_scelta["corretta"]:

            print("\nRisposta corretta!\n")

            punteggio += 1

            continue
        
        else:

            print(f"\nRisposta sbagliata! La risposta corretta era: {(domanda_scelta['risposte'].index(domanda_scelta['corretta'])) + 1}")

            print(f"\n\nHai totalizzato {punteggio} punti!\n")

            break
    
    return nickname, punteggio


def aggiorna_punteggi(record_punteggi, nick, punteggio):

    if nick in record_punteggi:
        record_punteggi[nick] += punteggio

    else:
        record_punteggi[nick] = punteggio

    # ordino dizionario per ordine decrescente di valori, punti in questo caso
        
    punteggi_aggiornati = dict(sorted(record_punteggi.items(), key=itemgetter(1), reverse=True)) 

    # riscrivo il file punti.txt con i punteggi aggiornati

    with open("punti.txt", "w", encoding="utf-8") as f:

        for i, (nick, punti) in enumerate(punteggi_aggiornati.items()):

            f.write(f"{nick} {punti}")

            if i != len(punteggi_aggiornati) - 1:

                f.write("\n")


def main():


    domande = leggi_domande("domande.txt")

    domande_organizzate = organizza_domande(domande)

    punteggi = leggi_punti("punti.txt")

    nick, punteggio = gioca_partita(domande_organizzate)
    
    aggiorna_punteggi(punteggi, nick, punteggio)


main()