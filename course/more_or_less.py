import random


level = input('1. Facile (0-10) / 2. Moyen (0-100) / 3. Difficile (0-1000) : ')

match level:
    case '1':
        maximum = 10
    case '2':
        maximum = 100
    case '3':
        maximum = 1000
    case other:
        maximum = 100

secret = random.randint(0, maximum)
user_nbr = int(input(f'Veuillez entrer un nombre entre 0 et {maximum} : '))
nbr_tries = 1

while secret != user_nbr:
    if secret > user_nbr:
        print('C\'est plus !')
    else:
        print('C\'est moins !')
    
    # Ternary 
    # info = 'C\'est plus !' if secret > user_nbr else 'C\'est moins !'
    # print(info)

    user_nbr = int(input(f'Veuillez entrer un nombre entre 0 et {maximum} : '))
    nbr_tries += 1

print(f'Bravo, vous avez trouvé le nombre secret en {nbr_tries} essai.s')

    