#ZADANIA : ADRIANNA BANDROWICZ -NOKIA

#13.Stworzyć listę z 3 znaczeniami 'to-delete' i kilku innymi i zabrać wszystkie łancuchy 'to-delete'
print("Zadanie 11 - tablica")
lista=['Ada','to-delete','Michał','to-delete','Kamil','to-delete','Łukasz']

print('Lista przed skasowaniem: ',lista)
x=1
while x<len(lista):
    lista.remove('to-delete')
    x=x+1

print('Lista po skasowaniu: ',lista)

input('Koniec programu?')
