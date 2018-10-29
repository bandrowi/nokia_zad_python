#ZADANIA : ADRIANNA BANDROWICZ -NOKIA

#GRA 

Pytania=['Czy Ziemia jest płaska?',
         'Czy koty spadaja na cztery łapy?',
         'Czy nokia 3310 to najlepszy telefon?',
         'Czy w terenie zabudowanym mozna jeździć 130 km/h?',
         'Czy gwiazdy to planaty?',
         'Czy 21.11.2018 r. jest dniem wolnym od pracy?',
         'Czy częste mycia skraca zycie?',
         'Czy trawa jest zielona?',
         'Czy kroway lataja?',
         'Czy koty szczekaja?']

Odpowiedzi=['n','t','t','n','n','n','n','t','n','n']
         
         
print('Odpowiedz na pytania uzywająć t/n ')
praw_odp=0
x=0
while x<len(Pytania)-1:
    Odpowiedz=input(Pytania[x])
    if Odpowiedz==Odpowiedzi[x]:
        praw_odp=praw_odp+1
    x=x+1

print('Koniec gry')
print('Prawidłowych odpowiedzi: ',str(praw_odp))







input("koniec programu?")
