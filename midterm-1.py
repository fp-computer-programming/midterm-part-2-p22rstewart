# Author RTS 12/15/21

import random

def clone_name():
    num = random.randint(1, 9999)
    while num <= 9:
        print("New clone trooper name: CT-" + "000" + int(num))
    while num <= 99:
        print("New clone trooper name: CT-" + "00" + int(num))
    while num <= 999:
        print("New clone trooper name: CT-" + "00" + int(num))


# Two difrent attempts


q = input("Would you like to name a new clone (Y or N): ")
if q == "y" or "Y":
    num = random.randint(1, 9999)
    while int(num) <= 9:
        print("New clone trooper name: CT-" + "000" + int(num))
    while int(num) <= 99:
        print("New clone trooper name: CT-" + "00" + int(num))
    while int(num) <= 999:
        print("New clone trooper name: CT-" + "00" + int(num))
elif q == "n" or "N":
    print("Come again")
