"""Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma,
a multiplicação e os números."""
lista=[]
lista2=[]
listasoma=[]
listamultiplica=[]
for i in range(5):
    num=int(input('Digite aqui um numero: '))
    lista.append(num)
    num2=int(input('Digite aqui outro numero: '))
    lista2.append(num2)
for i in lista:
    soma=0
    for j in lista2:
        soma=i+j
        listasoma.append(soma)
for i in lista:
    multi=0
    for j in lista2:
        multi=i*j
        listamultiplica.append(multi)
print(lista)
print(lista2)
print(listasoma)
print(listamultiplica)

    
