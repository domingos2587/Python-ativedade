import random

numeros = [0] * 6
for i in range(1, 100):
    n =  random.randint(1, 6)
    numeros[n -1] = numeros[n -1] + 1

cont = 1 
for n in numeros:
    print('%d teve %d lançamentos' % (cont, n))
    cont += 1