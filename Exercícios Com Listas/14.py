pontos = 0

print("Responda apenas com sim ou não: ")

a=str(input("Telefonou para a vítima? "))

if a == 'sim':
 pontos = pontos + 1
else:
 pontos = pontos + 0

b=str(input("Esteve no local do crime?  "))

if b == 'sim':

 pontos = pontos + 1

else:

 pontos = pontos + 0

c=str(input("Mora perto da vítima?  "))

if c == 'sim':

 pontos = pontos + 1

else:

 pontos = pontos + 0

d=str(input("Devia para a vítima?  "))

if d == 'sim':

 pontos = pontos + 1

else:

 pontos = pontos + 0

e=str(input("Já trabalhou com a vítima?  "))

if e == 'sim':

 pontos = pontos + 1

else:

 pontos = pontos + 0

print()

print(f"você fez {pontos} pontos")

if pontos == 2:

 print("Classificado como: Suspeito")

if pontos == 3 or pontos == 4:

 print("Classificado como: Cúmplice")

if pontos == 5:

 print("Classificado como: Assassino")

elif pontos<=1:

 print("Classificado como: Inocente")

