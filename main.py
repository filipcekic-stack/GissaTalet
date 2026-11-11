import random

usr = input("vad är dit användarnamn?")
tur = input("hur många gånger vill du spela?")
valen=['sten', 'sax', 'påse']
spelar_val = input("sten, sax eller påse: ").lower()
if spelar_val not in valen:
    print("Finns inte välj ny ")
else:
    dator_val = random.choice(valen)
    print(f" Dator valde: {dator_val}")
    
    if spelar_val==dator_val:
        print("Blev oavgjort!")
    elif (spelar_val== "sten" and dator_val=="sax") or (spelar_val=="sax" and dator_val =="påse") or (spelar_val=="påse" and dator_val == "sten"):
        print("Du vann!")
    
    else:
        print("datorn vann! ")

    