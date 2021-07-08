money = int(input())
chicken = money // 23
goat = money // 678
pig = money // 1296
cow = money // 3848
sheep = money // 6769
if 1 <= sheep <= cow:
    print(sheep, "sheep")
elif sheep < cow <= pig:
    if cow == 1:
        print(cow, "cow")
    else:
        print(cow, "cows")
elif cow < pig <= goat:
    if pig == 1:
        print(pig, "pig")
    else:
        print(pig, "pigs")
elif pig < goat <= chicken:
    if goat == 1:
        print(goat, "goat")
    else:
        print(goat, "goat")
elif goat < chicken and chicken >= 1:
    if chicken == 1:
        print(chicken, "chicken")
    else:
        print(chicken, "chickens")
else:
    print("None")
