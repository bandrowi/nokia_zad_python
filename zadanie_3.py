#ZADANIA : ADRIANNA BANDROWICZ -NOKIA

print("Zadanie 3 - kalkulator")
x=""
while x!="k":
    a=input("Podaj pierwszą liczbę: ")
    a=int(a)
    b=input("Podaj druga liczbę: ")
    b=int(b)
    c=input("Podaj rodzaj działania +,-,/,*: ")

    if c=="+":
        suma=a+b
        print("Wynik działania wynosi: ",suma)

    if c=="-":
        roznica=a-b
        print("Wynik działania wynosi: ",int(roznica))

    if c=="*":
        mnozenie=a*b
        print("Wynik działania wynosi: ",int(mnozenie))
        
    if c=="/":
        dzielenie=a/b
        print("Wynik działania wynosi: ",float(dzielenie))

    x=input("Wynik uzyskany koniec programu (nacisnij k)")

