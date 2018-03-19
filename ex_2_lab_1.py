print("THIS PROGRAM COMPUTE MANIPULATES STRINGS")
print("INPUT A GENERIC STRING")
str = input()
lenght = len(str)

if lenght<=2:
    str = ""
else:
    str = str[0]+str[1]+str[lenght-2]+str[lenght-1]

print(str)