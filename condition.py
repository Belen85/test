# age = input("quel est ton age? ")
# age = int(age)
# if age < 18 or age > 130:
#     print("Desole, vous etes hors age")
#     print("Au revoir!")
# else:
#     print("Bienvenue à Interface 3!!!")

age = input("quel est ton age? ")
age = int(age)
if age < 18:
    print("Desole, vous etes trop jeune.")
elif age > 130:
    print("Desole, vous etes trop vieux.")
else:
    print("Bienvenue à Interface 3!!!")

print("--Fin--")
