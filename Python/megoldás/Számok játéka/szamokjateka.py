from random import randint
probalkozasok = 0
generaltszam = int(randint(1, 25))
print('Szám legenerálva.')

while probalkozasok < 5:
    tipp = int(input('\nÍrja be a tippét: '))
    probalkozasok += 1
    print(f'Még {5 - probalkozasok} próbálkozása maradt.')
    if tipp == generaltszam:
        probalkozasok += 5
        input('Sikeresen kitalálta a számot.')
    elif tipp > generaltszam:
        print('Próbáljon egy kisebb számot.')
    else:
        print('Próbáljon egy nagyobb számot.')