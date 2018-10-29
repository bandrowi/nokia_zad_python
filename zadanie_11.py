#ZADANIA : ADRIANNA BANDROWICZ -NOKIA

#Stworzyć listę jakichkolwiek liczb 3x4, najpierw wyprowadzić wierszy, zatem kolumny.y.
print("Zadanie 11 - tablica")
lista=[[12, 13, 14],
[11, 14, 12],
[10, 12, 12],
[ 9, 11, 16],
[12, 11, 16]]
y=0
while y <4:
    x=0
    while x < 3:
        print(lista[y][x], end=" ")
        x=x+1
    print()
    y=y+1
    
input('Koniec programu?')
