# Scrivere la funzione neighbor_average(values, row, column) che, in una tabella values, calcoli il 
# valore medio dei vicini di un elemento nelle otto direzioni(escludendo l’elemento stesso). Se, però, 
# l’elemento si trova su un bordo della tabella, la media va calcolata considerando soltanto i vicini 
# che appartengono effettivamente alla tabella.

def neighbor_average(values, row, column):
    rows = len(values)
    cols = len(values[0])
    neighbors = []

    # Definire gli offset per le otto direzioni
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for dr, dc in directions:
        r, c = row + dr, column + dc
        if 0 <= r < rows and 0 <= c < cols:
            neighbors.append(values[r][c])

    if neighbors:
        average = sum(neighbors) / len(neighbors)
    else:
        average = 0

    return average

tab = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
row, column = 1, 1  # Elemento centrale
print(neighbor_average(tab, row, column))  # Output: 4.0

row, column = 0, 0  # Elemento in alto a sinistra
print(neighbor_average(tab, row, column))  # Output: 3.6666666666666665