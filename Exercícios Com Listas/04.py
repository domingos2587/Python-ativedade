"""Faça um Programa que leia um vetor de 10 caracteres,
e diga quantas consoantes foram lidas. Imprima as consoantes."""
lista=[]
listaconsonte2=[]
listaconsonte=[]
cont=0
print("digite  logo a baixo um caractere cada vez pedido apenas letras")
for i in range(10):
    num=input('Digite aqui o caractre')
    lista.append(num)
for X in lista:
    if X=='A' or X=='E' or X=='I' or X=='O' or X=='U' or X=='a' or X=='e' or X=='i' or X=='o' or X=='u':    
        listaconsonte2.append(X)
    else:
        listaconsonte.append(X)
        cont+=1
        
print('a quantidade de consonte e de: ',cont,'que são: ', listaconsonte)  
