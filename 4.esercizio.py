values = []

myfile = open('datevalue.csv', 'r')

for line in myfile: #leggo file riga per riga

    elements = line.split(',') #faccio lo split di ogni riga sulla virgola

    if elements[0] != 'Date': #se non sto processando l'intestazione

        #setto la data e il valore
        date = elements[0]
        print(date)
        value = elements[1]
        print(value)

        values.append(float(value)) #aggiungo alla lista dei valori questo valore