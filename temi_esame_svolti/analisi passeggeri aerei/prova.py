eta_tot = 0
origine = {}
lista_voli = {}

def volo_popolare(record_voli):
    occorrenze = 0

    for volo in record_voli:
        if len(record_voli[volo]) > occorrenze:
            popolare = volo
            occorrenze = len(record_voli[volo])

    return popolare

with open("passeggeri.txt", "r", encoding="utf-8") as f:
    f.readline()
    for riga in f:
        campi = riga.rstrip("\n").split(",")
        eta_tot = eta_tot + int(campi[1])
        num_volo = campi[5]
        if campi[3] not in origine:
            origine[campi[3]] = [int(campi[1])]
        else:
            origine[campi[3]].append(int(campi[1]))
        if campi[5] not in lista_voli:
            lista_voli[campi[5]] = [campi[2]]
        else:
            lista_voli[campi[5]].append(campi[2])


popolare = volo_popolare(lista_voli)
for origin in origine:
    print(f"origine: {origin} età media: {round(sum(origine[origin])/len(origine[origin]), 1)}")
print(f"\nNumero di volo più popolare: {popolare}, Passeggeri M: {lista_voli[popolare].count('M')} / F: {lista_voli[popolare].count('F')}\n")


volo_popolare(num_volo)


