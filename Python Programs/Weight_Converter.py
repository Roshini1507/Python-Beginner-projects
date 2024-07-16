weight = float(input("Weight : "))
unit = input("L(bs) or (K)g : ")
if unit.upper() == "L":
    coverted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight/0.45
    print(f"You are {converted} pounds")


