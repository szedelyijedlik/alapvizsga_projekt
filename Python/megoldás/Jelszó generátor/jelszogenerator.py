from random import randint

kisbetuk = "abcdefghijklmnopqrstuvwxyz"
nagybetuk = kisbetuk.upper()
szamok = "0123456789"
szimbolumok = "!@#$%^&*()_+-={}[]|:;'<>,.?/"


hossz = int(input("Írja be hány karakter hosszú jelszót szeretne generálni: "))
while hossz < 6:
    hossz = int(input("Írja be hány karakter hosszú jelszót szeretne generálni: "))

generalt = ""
for i in range(hossz):
    match randint(1,4):
        case 1:
            generalt += kisbetuk[randint(0, len(kisbetuk) - 1)]
        case 2:
            generalt += nagybetuk[randint(0, len(nagybetuk) - 1)]
        case 3:
            generalt += szamok[randint(0, len(szamok) - 1)]
        case 4:
            generalt += szimbolumok[randint(0, len(szimbolumok) - 1)]

print(f"A generált jelszó: {generalt}")
input("<ENTER>")