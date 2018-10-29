#ZADANIA : ADRIANNA BANDROWICZ -NOKIA

#14. Sortowanie odwrotne: z listy od 1 do 10 wyprowadzić do konsoli w odwrotnym znaczeniu.

print("Zadanie 14 - sortowanie odwrotne")
my_list=[]
x=0
while x<10:
    my_list.append(x+1)
    x=x+1
print(my_list)
#teraz sortujemy
my_list.sort(key=abs,reverse=True)
print(my_list)

input("koniec programu?")
