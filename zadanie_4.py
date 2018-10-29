#ZADANIA : ADRIANNA BANDROWICZ -NOKIA

print("Zadanie 4 - modulo 5")
a=input("Podaj liczbę, od której mam liczyć: ")
a=int(a)
b=input("Podaj liczbę, do której mam liczyć: ")
b=int(b)
x=a
while x<=b:
    wynik=x%5
    if wynik==0:
        print(x)
    x=x+1

input("koniec programu?")




