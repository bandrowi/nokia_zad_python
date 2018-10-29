#ZADANIA : ADRIANNA BANDROWICZ -NOKIA

#W przedziale [1,100] znaleźć wszystkie liczby, które dzielą się na 7 bez reszty.
print("Zadanie 10 - Liczby podzielne przez 7")

a=100
x=1

while x<=a:
    dzielnik=7
    wynik=x%dzielnik
    if wynik==0:
        print(x)
    x=x+1
    
input("koniec programu?")
