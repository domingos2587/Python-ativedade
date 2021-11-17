'''Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números
IMPARES no vetor impar. Imprima os três vetores.'''
listapar=[]
listaimp=[]
lista=[]
for i in range(20):
    num=int(input('Digite aqui um numero'))
    lista.append(num)
    if num%2==0:
        listapar.append(num)
    else:
        listaimp.append(num)
print("Os numero digitados foram ",lista)
print('os numero par foi',listapar)
print('os numeros impares foi',listaimp)
    
    
