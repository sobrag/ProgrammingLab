#Buona funzione: agisce solo su variabili locali, torna sempre il risultato con return

def funzione(argomento1, argomento2):
    print("Argomenti: {} e {}" .format(argomento1, argomento2))

funzione("Sofia", "Anna")#chiamo funzione che stamperà a schermo "Anna e Sofia"


def quadrato(numero):
    return numero*numero

quadrato(4) #chiamo funzione che tornerà 16
risultato = quadrato(4)
print('Risultato: {}'.format(risultato))


unalista = [1,4,5,8,9]
def sommalista(unalista):
    som = 0
    for item in unalista:
        som = som + item
    return som

print(sommalista(unalista))

#MODULI
from math import sqrt
sqrt(100)

#PYTHONICO VUOL DIRE:
lista = ["Sofia", "Anna", "Elena", "Giorgio"]
for item in lista:
    print(item)

if "Anna" in lista:
    print("Ho trovato Anna!")


