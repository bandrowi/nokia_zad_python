#ZADANIA : ADRIANNA BANDROWICZ -NOKIA

print("Zadanie 2 - Liczby pierwsze")
a=input("Podaj liczbę, do kórej mam liczyć liczby pierwsze: ")
a=int(a)
x=1

while x<=a:
    czy_pierwsza="true"
    dzielnik=2
    while dzielnik<x:
        wynik=x%dzielnik
        if wynik==0:
            czy_pierwsza="false"
            
        dzielnik=dzielnik+1
    if czy_pierwsza=="true":
        print(x)
    x=x+1

input("koniec programu?")



