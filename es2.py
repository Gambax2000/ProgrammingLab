#inizializzo una lista vuota
values=[]
#apro e leggo i file
my_file=open('shampoo_sales.csv','r')
    for line in my_file:
        #faccio lo split di ogni riga su virgola
        elements =line.split(',')
        #Se non sto precessando l'intestazione
        if elemts[0] != 'Date'
        
        