# Scrivere un programma che modelli e simuli il movimento di un oggetto di massa m collegato ad una 
# molla oscillante. Quando la molla viene spostata dalla sua posizione di equilibrio di una quantità x,
# la legge di Hooke afferma che la forza di ripristino è data dalla formula: F = -kx
# dove k è una costante che dipende dalla molla. 
# Per questa simulazione, utilizzare k = 10 N/m.
# Iniziare con un determinato spostamento x (ad esempio, x = 0.5 m). Impostare la velocità
# iniziale v = 0. Calcolare l’accelerazione a in base alla legge di Newton (a = F/m) e alla legge di
# Hooke, utilizzando una massa m = 1 kg. Utilizzare un piccolo intervallo di tempo delta_t =
# 0.01 s e, ad ogni passo, aggiornare la velocità, calcolando una variazione di aΔt , e lo spostamento,
# calcolando una variazione di vΔt.

k = 10
v0 = 0
m = 1

