#dichiaro due variabili e le stampo
x = 5
y = "John"
print(x)
print(y)
#attribuisco alla variabile il tipo 
z = float(6)
print(type(y)) #stampo il tipo di variabile 
print (z)
#A variable name must start with a letter or the underscore character
#assegno a diverse variabili diversi valori sulla stessa riga
j,k,l = "salvatore", "mariolina", "ippocrate"
print(j)
print(k)
print(l)
#assegno a diverse variabili lo stesso valore
e = r = t = "ferdinando"
print(e)
print(r)
print(t)
#assegno a ogni valore di una lista una variabile e la stampo
macchine = ["fiat", "mercedes", "ferrari"]
a,s,d = macchine
print(a)
print(s)
print(d)
#creo una variabile fuori dalla funzione e la stampo
t = "scemo"
def funx():
    print("Tu " + t+ " mangia brosciutto")
funx()    
#creo due variabili con lo stesso lo stesso nome(una dentro la funzione e l'altra fuori) e le stampo
PO = " fenomeno"
def funxia():
    PO = "un"
    print("sei "+ PO)
funxia()
print(PO)    
#il comando global rende una variabile all'interno della funzione globale
def funxio():
    global w
    w = "nota"
funxio()
print("ti metto la "+ w)