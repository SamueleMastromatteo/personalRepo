lista_canzoni = {}


def confronto_copiatura(canzone, confronto, nomeCanzone, nomeConfronto):
    for i in range(0, len(canzone) - 4):
        for j in range(0, len(confronto) - 4):
            if canzone[i:i + 4] == confronto[j:j + 4]:
                print(f"la canzone {nomeConfronto} è una copiatura di {nomeCanzone}")
                return True

    return False


def confronto_sospetto(canzone, confronto, nomeCanzone, nomeConfronto):
    canzone_trasposta = []
    confronto_trasposto = []
    for i in range(0, len(canzone) - 4):
        canzone_trasposta = {
            int(canzone[i]) - int(canzone[i + 1]),
            int(canzone[i]) - int(canzone[i + 2]),
            int(canzone[i]) - int(canzone[i + 3]),
        }
        for j in range(0, len(confronto) - 4):
            confronto_trasposto = {
                int(confronto[j]) - int(confronto[j + 1]),
                int(confronto[j]) - int(confronto[j + 2]),
                int(confronto[j]) - int(confronto[j + 3])
            }
            if canzone_trasposta == confronto_trasposto:
                print(f"la canzone {nomeConfronto} è sospetta di {nomeCanzone}")
                return True
    return False


with open("brani.txt", "r", encoding="utf-8") as f:
    for riga in f:
        campi = riga.rstrip("\n").split(":")
        lista_canzoni[campi[0]] = campi[1].lstrip().split(" ")
    for canzone in lista_canzoni.keys():
        for confronto in lista_canzoni.keys():
            if canzone == confronto:
                break
            if lista_canzoni[canzone] == lista_canzoni[confronto]:
                print(f"la canzone {canzone} ha plagiato {confronto}")
                continue
            if confronto_copiatura(lista_canzoni[canzone], lista_canzoni[confronto], canzone, confronto):
                continue
            confronto_sospetto(lista_canzoni[canzone], lista_canzoni[confronto], canzone, confronto)
