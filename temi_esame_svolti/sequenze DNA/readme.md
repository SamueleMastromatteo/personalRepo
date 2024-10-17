Sequenze DNA
La vita dell’uomo e di molti altri esseri viventi è regolata dal DNA, e dalla successiva trascrizione e traduzione di
quest’ultimo in proteine. L’informazione del DNA è contenuta nella successione di 4 basi azotate: adenina, timina,
citosina, guanina, rappresentate ognuna con una rispettiva lettera dell’alfabeto (A, T, C, G). Pertanto, una
molecola di DNA può essere memorizzata in un calcolatore con una sequenza delle quattro basi azotate (e.g.
ATTTGGACACACTAA); un amminoacido è composto dalla sequenza di 3 basi azotate. Similarmente,
l’informazione delle proteine è portata dalla successione di 21 diversi amminoacidi (metionina, leucina, etc…),
rappresentate ognuna con una lettera univoca (M,L,…).
Si scriva un programma Python che dato in ingresso un file contente sequenze di DNA, scriva in un altro file le
sequenze di proteine che derivano da quelle sequenze di DNA (vedi il formato di entrambi i file nell’esempio).
Il programma deve contenere una funzione che, preso in ingresso una sequenza di DNA, restituisca la proteina
risultante. Tale funzione deve essere utilizzata per generare il file di output.
Il codice di conversione da amminoacido a sequenza di basi azotate è contenuto nel file codicegenetico.txt:
Esempio di file "codicegenetico.txt":
F:TTT,TTC
L:TTA,TTG,CTT,CTC,CTA, CTG
I:ATT,ATC,ATA
M:ATG
V:GTT,GTC,GTA,GTG
S:TCT,TCC,TCA,TCG
P:CCT,CCC,CCA,CCG
T:ACT,ACC,ACA,ACG
A:GTC,GCC,GCA,GCG
Y:TAT,TAC
H:CAT,CAC
Q:CAA,CAG
N:AAT,AAC
K:AAA,AAG
D:GAT,GAC
E:GAA,GAG
C:TGT,TGC
W:TGG
R:CGT,CGC,CGA,CGG,AGA,AGG
S:AGT,AGC
G:GGT,GGC,GGA,GGG
STOP:TAA,TAG,TGA
Come si può notare, alcuni amminoacidi sono tradotti da una e una sola tripletta, altri invece possono essere
ottenuti a partire da triplette diverse.
Si scriva un programma per costruire le proteine risultanti dalla loro sequenza di DNA.
Il programma richiede all'utente due informazioni:
1. il nome del file da decodificare. Contiene, per ogni sequenza da ricostruire, un codice identificativo univoco
preceduto dal simbolo “>” (es. “>id_000458”) e la sequenza del DNA.
2. il nome del file decodificato. Conterrà le sequenze di proteine costruite a partire dalla sequenza di DNA e
precedute dal loro codice identificativo univoco. I due file, quindi, avranno un numero uguale di righe, in
quanto ad ogni sequenza di DNA corrisponde una e una sola proteina.
Note Si assuma che il formato del file di input sia corretto (riga con l’identificativo, seguita dalla sequenza da
tradurre; la sequenza di DNA, ad eccezione dei caratteri di spaziatura, ha un numero di caratteri multiplo di tre
contiene almeno due triplette di cui l’ultima di STOP. Inoltre, non sono presenti triplette non associate ad
amminoacidi).
Messaggi stampati a video dal programma:
Esempio di esecuzione: Supponendo che il file "dna.txt" contenga:
Esempio di file "dna.txt":
>id_0006545
ATG TGG ATG TGG ATG TGG TGG TGG TGG TAA
>id_058496545
ATG GTC AAC CAA TCA CAC TGA
>id_00556183
ATG ATT CCT TGT TTC GTC CGT CGT TAG
il risultato sarà il file "proteins.txt":
Esempio di file "proteins.txt"
>id_0006545
MWMWMWWWW
>id_058496545
MVNQSH
>id_00556183
MIPCFARR