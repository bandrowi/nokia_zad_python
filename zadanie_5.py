#ZADANIA : ADRIANNA BANDROWICZ -NOKIA

#Stworzyć listę z 6 randomowych liczb i odsortować.
import random
print("Zadanie 5 - random")
my_list=[]
x=0
while x<6:
    my_list.append(random.randint(0,1000))
    x=x+1
print(my_list)
#teraz sortujemy
my_list.sort(key=abs)
print(my_list)

input("koniec programu?")



