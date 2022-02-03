#stampa numero di lista
listadinumeri = [13,12,34,4,51,8,2,18]
for item in listadinumeri: 
    if item < 5:
        print(item)


a = 3 #non serve esplicitare il tipo di dati
b = 2
print('Primo: {}, secondo: {}' .format(a,b))


#if-else 
if(a > b):
    massimo = a
    if (a-b) <= 1:
        print('a è maggiore ma non di molto')
else: 
    massimo = b
    if (b-a) <= 1:
        print("b è maggiore ma non di molto")
print('max:{}' .format(massimo))


#VARIABILI BOOLEANE
var1 = True
var2 = False
var3 = None


#SLICING: taglio stringa
stringa = 'Sofia'
print(stringa[0:3]) #dal primo al terzo carattere
print(stringa)


#LISTE
listanum = [1,2,3,4]
listastring = ['Sofia', 'Anna']


#Esponente **
print(a**b) 


#operatori logici: and, or, not

#operatori di appartenenza: in (ritorna True se una sequenza con il valore specificato è presente nell'oggetto), not in (se NON è presente)
if 'Sofia' in listastring:
    print("Sofia is in listastring")


#DIZIONARI
dizionario = {'Trieste': 34100, 'Padova': 35100} #parentesi diverse delle liste
print('CAP di Trieste : {}' .format(dizionario['Trieste']))


#FOR E WHILE
i = 0
while i < 10:
    print(i)
    i = i + 1

for i in range(10):
    print(i)

#ciclo for per stampare tutti gli elementi di una lista con annesso indice
for i, item in enumerate(listanum):
    print("Posizione {}: {}" .format(i, item))
