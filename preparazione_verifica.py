#esercizio A
Animale_1 = "Cane"
Animale_2 = "Gatto"
Animale_3 = "Topo"
Animale_4 = "Cerbiatto"
Animale_5 = "Pescepalla"

print(Animale_1, Animale_2, Animale_3,  Animale_4, Animale_5)
#esercizio B
def funzione_1():
    x = 7 
    y = 12
    if x < y:
        print("ciao")
    else:
        print("il contrario di ciao")
funzione_1()
#esercizio C
def funzione_2():
    x = 4
    y = 18
    z = 45
    if x > y and x > z:
        print("Ciao")
funzione_2()
   
#esercizio D
def funzione_3():
    x = 4
    y = 18
    z = 45
    if x > y and x > z:
        print("x")
    elif y > x and y > z:
        print("y")
    else:
        print("z")
funzione_3()
#esercizio E
def funzione_4():
    città = ["Milano", "Pag", "Imperia"]
    nomi = ["Paolo", "Marco", "Umberto"]
    for x in città:
        for y in nomi:
            print(x,y)
funzione_4()
#esercizio F
def funzione_5():
    numero = 22
    numeri = [23, 67, 32, 12, 77]
    for x in numeri:
         if x > numero:
            print(x)
funzione_5()
#esercizio G
print ("*************************")
def funzione_6():
    lista_numeri = [34, 56, 87, 36, 26]
    minore = 99999999
    for i in lista_numeri:
        if i < minore:
            minore = i
    print(minore)
funzione_6()
#esercizio H
def funzione_7():
    Animali = ["Paguro", "Cavallo", "Ghepardo", "pterdotall"]
