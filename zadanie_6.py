#ZADANIA : ADRIANNA BANDROWICZ -NOKIA

#6. Stworzyć słownik z 5-ciu part int -> str, np {6: '6'}, i wyprowadzić każde znaczenie do konsoli osobno

print("Zadanie 6 - słownik")
slownik={}
x=1
while x<6:
    slownik[x]=input('Podaj wartość '+str(x)+':')
    x=x+1
x=1
while x<6:
    print(str(x)+':'+slownik[x])
    x=x+1

input("koniec programu?")
