'''Faça um Programa que leia um vetor A com 10 números inteiros,
calcule e mostre a soma dos quadrados dos elementos do vetor.'''
lista=[]
listaquadrada=[]
for i in range(5):
    num=int(input('digite aqui numero inteiro'))
    lista.append(num)
for i in lista:
    multi=0
    multi=i*i
    listaquadrada.append(multi)
print('aqui esta o quadrado da lista informada: ',listaquadrada)
    
