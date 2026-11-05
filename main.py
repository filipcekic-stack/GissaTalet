import random as rand 

namn = input("vad heter du?")
print(f"hej {namn} och välkommen till spelet!")
 
i = rand.randint(1,10)

tal = input("gissa talet")
if tal == i:
    print(f"du gissade rätt!!!")
elif tal != i:
o = input("fel försök igen ")
elif tal != o:
    input("fel försök en gång till ")
else:
    print(f"du gissade fel")
print(f"Talet var {i}")

