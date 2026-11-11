import random

i = random.randint(1,10)

for p in range(3):
    r = int(input("skriv ett tal "))
    if r == i:
        print("du har rätt")
    else:
        print("du har fel")
print(f"talet var {i}")
