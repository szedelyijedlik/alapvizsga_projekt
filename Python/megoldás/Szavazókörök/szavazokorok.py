from szavazokor import Szavazokor

szavazokorok: list[Szavazokor] = []

f = open("Python/megoldás/Szavazókörök/szavazokor.csv", "r", encoding="utf-8")
f.readline()
for row in f:
    szavazokorok.append(Szavazokor(row))
f.close

print(f'1. feladat:\n\tÖsszesen {len(szavazokorok)} szavazókör van.')

db = 0
for sz in szavazokorok:
    if "Budapest" not in sz.telepules:
        db += 1
print(f'2. feladat:\n\t{db} szavazókör található vidéken.')

f = open("akadalymentesek.txt", "w", encoding="utf-8")
for sz in szavazokorok:
    if sz.akadalymentesseg == "Igen": #Vármegye;Település;Cím;Típus;Akadálymentesség;Választópolgárok száma
        f.write(f"{sz.varmegye};{sz.telepules};{sz.cim};{sz.akadalymentesseg};{sz.valasztokszama}\n")
print("3. feladat:\n\tFájl létrehozva.")

print("4. feladat:\t")
for sz in szavazokorok:
    if sz.valasztokszama >= 1550:
        print(f'\tCím: {sz.cim}')