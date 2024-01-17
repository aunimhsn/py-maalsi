table = int(input('Quelle table voulez-vous afficher ? '))
result = []

for i in range(1, 11):
    result.append(table * i)
    if (table * i) % 3 == 0:
        result[i-1] = f'{result[i-1]}*'
    
print(result)