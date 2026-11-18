import random

usr = input("Vad är ditt användarnamn? ")
tur = int(input("Hur många rundor vill du spela? "))

valen = ['sten', 'sax', 'påse']


spelar_poang = 0
dator_poang = 0

for i in range(tur):
    print(f"\n--- Runda {i + 1} ---")

    spelar_val = input("Sten, sax eller påse: ").lower()

    if spelar_val not in valen:
        print("Ogiltigt val! Försök igen.")
        continue

    dator_val = random.choice(valen)

    print(f"Datorn valde: {dator_val}")

    if spelar_val == dator_val:
        print("Det blev oavgjort!")

    elif (spelar_val == "sten" and dator_val == "sax") or \
         (spelar_val == "sax" and dator_val == "påse") or \
         (spelar_val == "påse" and dator_val == "sten"):

        print("Du vann!")
        spelar_poang += 1

    else:
        print("Datorn vann!")
        dator_poang += 1

    print(f"\n{usr}: {spelar_poang} poäng")
    print(f"Datorn: {dator_poang} poäng")


print("\n===== SPELET ÄR SLUT =====")
print(f"{usr}: {spelar_poang} poäng")
print(f"Datorn: {dator_poang} poäng")

if spelar_poang > dator_poang:
    print(f"Grattis {usr}, du vann hela spelet!")

elif dator_poang > spelar_poang:
    print("Datorn vann hela spelet!")

else:
    print("Hela spelet blev oavgjort!")