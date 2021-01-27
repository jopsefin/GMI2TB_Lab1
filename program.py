from modules import division, guessing_game

print('Hej och välkommen till Josefins Kaos')
print('Först kommer du få en lista returnerad till dig med de tal som är delbara till heltal med 7 och 11.')
print('Efter det kommer du få gissa på ett slumpat tal mellan 1 och 100. ')
print('Lycka till och ha så kul! ')

# Kollar så siffran är en integer samt större än 0
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