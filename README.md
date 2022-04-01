# AIproject
Descrizione dei file sorgente:
Il progetto comprende 5 file sorgenti:

-**main.py:** è il file da cui parte l'esecuzione, sono presenti alcuni metodi per preimpostare dei grafi ripresi dalla sezione 4.5 dell'articolo Jensen1997 (fra cui il 4.18); è inoltre presente un metodo che chiede se impostare un grafo a partire da uno di questi metodi o definirne uno in autonomia.

-**treeManipulation.py:** è il file che contiene i metodi per la manipolazione del grafo inserito fino ad arrivare al junction tree.

-**graph.py:** è il modulo che contiene la classe di rappresentazione dei grafi con rappresentazione in lista di adiacenza.

-**MSTkruskal.py:** contiene essenzialmente l'algoritmo di Kruskal per gli MST insieme alle classi per la gestione della struttura dati union-find.

-**junctionTree.py:** contiene la classe omonima per la rappresentazione di un junction tree con tanto di classe separatore, rappresenta il junction tree come matrice di adiacenza in cui ogni elemento contiene la label del separatore fra i due nodi.

## Ottenere i risultati del test

Per la riproducibilità dei risultati premere il pulsante di esecuzione e seguire le istruzioni a schermo, in particolare:
1. Verrà chiesto se si vuole caricare uno dei grafi presentati nella sezione 4.5 del libro di Jensen1997, in questo caso:
   - cercare il grafo voluto fra quelli disponibili
   - scrivere il numero della figura senza il punto (es. 4.11 -> 411)
   - premere invio per visualizzare i risultati
2. Nel caso si voglia definire un grafo in modalità manuale inserire 0 premendo invio, poi:
   - viene chiesto di inserire il numero di nodi del grafo, inserirlo e premere invio
   - viene avviata una modalità in cui viene continuamente richesto di inserire un arco oppure visualizzare il junction tree del grafo inserito.
   - scrivendo a,b si inserisce un arco direzionato che parte dal nodo *a* ed arriva al nodo *b*, questi due nodi verranno inseriti automaticamente.
   - una volta inseriti tutti gli archi inserire il simbolo $ per visualizzare il junction tree.

In ogni caso verranno visualizzati i seguenti risultati:
1. il grafo originale inserito in formato lista di adiacenza.
2. il grafo moralizzato in formato lista di adiacenza.
3. l'ordine di eliminazione dei nodi utilizzato per la triangolazione.
4. il grafo triangolato in formato lista di adiacenza.
5. le cricche trovate.
6. le cricche massimali trovate.
7. il grafo delle cricche (junction graph) in formato matrice di adiacenza.
8. il corrispondente Maximum spanning tree in formato matrice di adiacenza.
9. e infine l'MST (junction tree) in formato lista di adiacenza per una maggiore leggibilità.
10. Ripropone l'MST (junction tree in formato matrice di adiacenza nel quale ogni elemento rappresenta il corrispettivo separatore.
