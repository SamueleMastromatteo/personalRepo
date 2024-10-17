def leggi_dati(nome_file):

    record_origini_eta = {}
    record_n_voli_passeggeri = {}

    with open(nome_file, "r", encoding="utf-8") as f:
        f.readline()
        for riga in f:
            campi = riga.rstrip("\n").split(",")
            if campi[3] not in record_origini_eta:
                record_origini_eta[campi[3]] = [int(campi[1])]
            else:
                record_origini_eta[campi[3]].append(int(campi[1]))
            if campi[5] not in record_n_voli_passeggeri:
                record_n_voli_passeggeri[campi[5]] = [campi[2]]
            else:
                record_n_voli_passeggeri[campi[5]].append(campi[2])
    return record_origini_eta, record_n_voli_passeggeri

def volo_popolare(record_voli):
    occorrenze = 0

    for volo in record_voli:
        if len(record_voli[volo]) > occorrenze:
            popolare = volo
            occorrenze = len(record_voli[volo])
    
    return popolare


def main():

    record_origini, record_voli = leggi_dati("passeggeri.txt")
    popolare = volo_popolare(record_voli)

    print("\nMedia dell'età per ciascuna origine\n")

    for origine in record_origini:

        print(f"Origine: {origine}, Media età: {(sum(record_origini[origine]) / len(record_origini[origine])):.1f} ")

    print(f"\nNumero di volo più popolare: {popolare}, Passeggeri M: {record_voli[popolare].count('M')} / F: {record_voli[popolare].count('F')}\n")
    
main()