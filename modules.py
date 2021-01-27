def division(num1, num2):

    # skapar lista för att lägga till nummer
    num_list = []
    max_num = 1

    # loop för att lägga till siffrorna som uppfyller if-satsen till listan.
    while max_num < 1000:
        if max_num % num1 == 0 and max_num % num2 == 0:
            num_list.append(max_num)
            max_num += 1
        else:
            max_num += 1
    
    # skriver ut de nummer som lagts till i listan.
    return print(f'{num_list}')

def guessing_game():
    
    from random import randint

    # skapar slumpad siffra i random_num
    random_num = randint(1,101)

    # säkerställer att man anger en siffra, kollar sedan om siffran är samma som random nummer.
    # kollar annars om den är större och slutligen är den annars mindre. Skickar meddelande beroende på resultat.
    while True:
        while True:
            try:
                guess = int(input('Gissa på ett nummer: '))
                break
            except ValueError:
                print('Du måste ange ett heltal, försök igen!')

        if guess == random_num:
            print("Du gissade rätt, grattis! ")
            break
        elif guess > random_num:
            print("Du gissade för högt, försök igen. ")
        else:
            print('Du gissade för lågt, försök igen, ')