#apro,leggo e chiudo file csv
file = open('clienti.csv', 'r')

print(file.read()) #leggo e stampo

for line in file:  #stampo riga per riga
    print(line)

print(file.readline()) #leggo una sola riga

print(file.read()[0:3]) #slicing per stampare solo un pezzo del file

#in modo più sofisticato:
contenuto = file.read()
if len(contenuto) > 4:
    print(contenuto[0:4])
else:
    print(contenuto)

file.close()


#scrivo su file
file = open('cienti.csv', 'w')
file.write = ('Ciao!')
file.close()

#split per separare le stringhe su uno specifico carattere
stringa = 'Ciao, sono Sofia!'
lista_elementi = stringa.split(',')
print(lista_elementi)

#conversione di una stringa a valore numerico
string = '5.5'
numero = float(string)
print(numero)

#aggiungere elemento ad una lista 
mia_lista = [1,2,3]
mia_lista.append(4)
print(mia_lista)