
# 1. Acquisition des notes
marks = []

while True:
    mark = input('Veuillez entrer une note : ')
    try:
        mark = float(mark)
    except ValueError:
        print('Ceci n\'est pas un nombre')
    else:
        if mark < 0:
            break
        marks.append(mark)

# 2. Calcul de la moyenne
try:
    marks_mean = sum(marks) / len(marks)
except ZeroDivisionError:
    print('Vous n\'avez pas entré de note...')
else:
    print(f'La moyenne est {marks_mean}')