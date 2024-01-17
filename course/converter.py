

speed_kmh = float(input('Veuillez entrer une vitesse en km/h :'))
KMH_TO_MPH = 1.609

speed_mph = speed_kmh / KMH_TO_MPH

print(f'{speed_kmh} km/h = {speed_mph:.2f} m/h')
# print(f'{speed_kmh} km/h = {round(speed_mph, 2)} m/h')