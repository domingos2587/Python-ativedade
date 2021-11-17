'''Faça um Programa que leia dois vetores com 10 elementos cada. Gere um
terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos
elementos intercalados dos dois outros vetores.'''
import random

lista1 = []
lista2 = []
lista3 = []

for i in range(10):
	lista1.append(random.randint(1,100))
	lista2.append(random.randint(1,100))
	lista3.append(lista1[i])
	lista3.append(lista2[i])

print (lista1)
print (lista2)
print (lista3)
