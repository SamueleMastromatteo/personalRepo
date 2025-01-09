# Scrivere un programma che legga un file di testo (maze.txt) contenente
# l’immagine di un labirinto, come il seguente, in cui gli asterischi ('*') rappresentano muri invalicabili
# e gli spazi (' ') rappresentano corridoi percorribili.
# * *******
# *   * * *
# * ***** *
# * * *   *
# * * *** *
# *   *   *
# ***** * *
# *     * *
# ******* *
# Creare un dizionario corridors le cui chiavi sono tuple (riga,
# colonna) di posizioni corrispondenti a un corridoio e i cui valori sono
# insiemi di posizioni anch’esse corrispondenti a un corridoio, e adiacenti
# alla posizione specificata dalla rispettiva chiave. Nell'esempio sopra, la
# chiave corrispondente alla tupla (1, 1), evidenziata in blu, ha come
# posizioni adiacenti {(1, 2), (0, 1), (2, 1)}. Visualizzare il
# dizionario.


with open("maze.txt", "r", encoding="utf-8") as f:
    maze = []
    for riga in f:
        maze.append(riga.rstrip())
        
positions = {}
for row in range(len(maze)):
    for col in range(len(maze[row])):
        if maze[row][col] == " ":
            positions[(row, col)] = set()
            if row > 0 and maze[row-1][col] == " ":
                positions[(row, col)].add((row-1, col))
            if row < len(maze) - 1 and maze[row+1][col] == " ":
                positions[(row, col)].add((row+1, col))
            if col > 0 and maze[row][col-1] == " ":
                positions[(row, col)].add((row, col-1))
            if col < len(maze[row]) -1 and maze[row][col+1] == " ":
                positions[(row, col)].add((row, col+1))
                
for i in sorted(positions):
    print(i, ":", positions[i])
