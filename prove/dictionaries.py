

persona = {
    'nome': 'Mario',
    'cognome': 'Rossi'
}

persona['matricola'] = int(input("inserire numero matricola: "))
persona['esami'] = []
n_esami = int(input("inserire numero esami: "))

for i in range(1, n_esami+1):
    materia = input(f"esame numero {i}: ")
    voto= int(input(f"voto per l'esame {materia}: "))

    persona["esami"] += [{
        'materia': materia,
        'voto': voto
    }]

print(persona)