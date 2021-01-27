# Modul med minst två funktioner
# Funktion 1: Ta emot två tal i parameterlista, returneras en lista med de tal från 1 till 1000 som är delbara till heltal.
# Delbart med 7 & 11, resultat: [77, 154, 231, 308, 385, 462, 539, 616, 693, 770, 847, 924]
# Funktion 2: Låta användaren gissa på ett tal mellan 1 och 100.
# Berätta vid varje försök om för lågt eller för högt.
# from random import randint
# Alla funktioner ska anropas ifrån en fil som heter program.py. Dvs ni måste importera er modules.py fil i program.py.
# Extra: Felhantering, returnera dictionary med talen samt medelvärdet på funktion 1.

from modules import division, guessing_game


print('Hej och välkommen till Josefins Kaos')
print('Först kommer du få en lista returnerad till dig med de tal som är delbara till heltal med 7 och 11.')
print('Efter det kommer du få gissa på ett slumpat tal mellan 1 och 100. ')
print('Lycka till och ha så kul! ')

while True:
    try:
        num1 = int(input('Ange första siffran du vill dela med: '))
        if num1 > 0:
            break
        else:
            print("Du måste ange en siffra större än 0")
    except ValueError:
        print('Ange en siffra, försök igen')
while True:
    try:
        num2 = int(input('Ange andra siffran du vill dela med: '))
        if num2 > 0:
            break
        else:
            print("Du måste ange en siffra större än 0")
    except ValueError:
        print('Ange en siffra, försök igen')

print(f'Du angav {num1} & {num2}. Här är resultatet: ')

division(num1, num2)

print('Nu börjar gissningsleken, lycka till! ')
guessing_game()
