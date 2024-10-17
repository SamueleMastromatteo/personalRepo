import operator
import random


# versione con la lettura iniziale di tutto il file in una lista di stringhe con readlines
# ed analisi della lista a blocchi di 7 righe per volta
def leggi_domande(nome_file):
    lista_domande = []
    livelli = []

    with open(nome_file, "r", encoding="utf-8") as f:
        linee = f.readlines()

    i = 0
    while i < len(linee):
        domanda = linee[i].strip()
        livello = int(linee[i + 1])
        livelli.append(livello)
        risposte = [r.strip() for r in linee[i + 2 : i + 6]]
        lista_domande.append(
            {"domanda": domanda, "livello": livello, "risposte": risposte}
        )
        i += 7  # vai avanti di 7 righe alla prox domanda

    return lista_domande, max(livelli)


# versione con la lettura di una riga per volta (con readline)
# e controllo sulla fine del file (riga vuota)
def leggi_domande_2(nome_file):
    lista_domande = []
    livelli = []
    riga_vuota = "*"  # sentinella per entrare nel while
    with open(nome_file, "r", encoding="utf-8") as f:
        while riga_vuota != "":  # finché il file non è finito
            domanda = f.readline().rstrip()
            livello = int(f.readline())
            livelli.append(livello)
            risposta1 = f.readline().rstrip()
            risposta2 = f.readline().rstrip()
            risposta3 = f.readline().rstrip()
            risposta4 = f.readline().rstrip()
            riga_vuota = f.readline()
            # se sono alla fine del file, riga_vuota diventa '' perché non c'è la riga vuota di separazione

            lista_domande.append(
                {
                    "domanda": domanda,
                    "livello": livello,
                    "risposte": [risposta1, risposta2, risposta3, risposta4],
                }
            )

    return lista_domande, max(livelli)


def trova_quesito(domande, livello):
    # estrai solo le domande del livello utile
    domande_livello = [d for d in domande if d["livello"] == livello]
    # prendine una a caso tra quelle estratte
    scelta = random.choice(domande_livello)
    return scelta


def leggi_risposta():
    """
    Leggi un numero tra 1 e 4 gestendo tutti i possibili errori
    """
    while True:
        try:
            risp = int(input("Inserisci la risposta: "))
            if 1 <= risp <= 4:
                return risp
            else:
                print("Valore errato, deve essere compreso tra 1 e 4")
        except ValueError:
            print("Formato errato, devi inserire un numero intero")


def aggiorna_classifica(nick, punti):
    # leggi punteggi vecchi
    punteggi = dict()
    with open("punti.txt", "r", encoding="utf-8") as f:
        for line in f:
            campi = line.rstrip().split()
            punteggi[campi[0]] = int(campi[1])

    # aggiungi o incremente questo giocatore
    if nick in punteggi:
        punteggi[nick] += punti  # incrementa giocatore esistente
    else:
        punteggi[nick] = punti  # aggiungi nuovo giocatore

    # ordina classifica
    classifica = list(punteggi.items())  # lista di coppie (nome, punti)
    # ordina per punti decrescenti
    classifica.sort(key=operator.itemgetter(1), reverse=True)

    # ri-scrive il file
    with open("punti.txt", "w", encoding="utf-8") as f:
        for voce in classifica:
            f.write(f"{voce[0]} {voce[1]}\n")


def main():
    domande, max_livello = leggi_domande("domande.txt")

    nick = ""
    while nick == "":
        nick = input("Inserisci il tuo nickname: ")

    livello = 0
    perso = False
    punteggio = 0

    while livello <= max_livello and not perso:

        quesito = trova_quesito(domande, livello)
        print(f'Livello {livello}) {quesito["domanda"]}')

        risposte = list(
            enumerate(quesito["risposte"])
        )  # faccio una copia perché le rimescolo. Uso enumerate per ricordare la posizione (la 0 è quella giusta)
        random.shuffle(risposte)  # mescola in ordine casuale
        # risposte[pos][0] sarà la posizione originaria
        # risposte[pos][1] sarà il testo

        # scopro dove è finita la risposta giusta dopo avere rimescolato
        pos_corretta = -1
        for pos in range(len(risposte)):
            if risposte[pos][0] == 0:
                pos_corretta = pos

        for pos in range(len(risposte)):
            print(f"    {pos+1}: {risposte[pos][1]}")
        # print(risposte)
        r = leggi_risposta()
        if risposte[r - 1][0] == 0:
            # risposta corretta
            print("Risposta corretta!")
            livello += 1
            punteggio += 1
        else:
            # errata
            print(f"Risposta errata, la risposta corretta era {pos_corretta+1}")
            perso = True

    print(f"Partita conclusa con punti {punteggio}")

    aggiorna_classifica(nick, punteggio)


main()
