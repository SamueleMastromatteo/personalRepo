from operator import itemgetter

#legge la lista di allarmi
def leggi_allarmi(nome_file):
    allarmi = [] #lista che conterrà i dizionari
    record_robot = set() #set per evitare duplicati
    with open(nome_file, "r", encoding="utf-8") as f:
        f.readline() #salta la prima riga che sono nomi dei campi
        for riga in f: #legge ogni riga del file dalla 2°
            campi = riga.rstrip("\n").split(";") #crea lista campi
            if campi[0] not in record_robot:
                record_robot.add(campi[0]) #aggiungo robot al set
                #creo nuovo dizionario dentro lista allarmi
                allarmi.append({
                    "robot": campi[0], #nome
                    "valori": [int(campi[1])] #severity
                })
            else:
                for allarme in allarmi:
                    #aggiungo valore severity alla lista valori nel dizionario del robot specificato
                    if campi[0] == allarme["robot"]:
                        allarme["valori"].append(int(campi[1]))
    return allarmi

def organizza_dati(allarmi):
    max_val = 0
    max_robot = [] #lista robot che hanno valore severity massimo
    for allarme in allarmi:
        #conta quanti allarmi ha ogni robot
        allarme["n_allarmi"] = len(allarme["valori"])
        for val in allarme["valori"]:
            #cerca il valore severity massimo per ogni robot
            if val > max_val:
                max_val = val
    for allarme in allarmi:
        #aggiungo alla lista max_robot i robot che hanno massima severity
        if max_val in allarme["valori"]:
            max_robot.append(allarme["robot"])
    #ordina i robot a partire da quello con più allarmi
    allarmi.sort(key=itemgetter("n_allarmi"), reverse=True)
    return max_robot, max_val

def main():
    allarmi = leggi_allarmi("allarmi.csv")
    max_robot, max_val = organizza_dati(allarmi)
    for allarme in allarmi:
        print(f"Per il robot {allarme['robot']} si sono verificati {allarme['n_allarmi']} allarmi")
    print(f"\nIl livello massimo di severità {max_val} è stato raggiunto dai seguenti robot:")
    for robot in max_robot:
        print(robot)
    print(allarmi)

main()