listanota=[]
num=0
media=0
soma=0
maior=[]
menor=[]
cont=0
cont2=0
print('Digite -1 para encerra o programa')
while cont2!=-1:
    if num>=0:
        num=float(input('Digite aqui a nota: '))
        cont=cont+1
        soma=num+soma
        listanota.append(num)
        cont2=int(input('para encerra o program digite-1: '))
    else:
        print('Fim do programa')
   

media=soma/cont
for i in listanota:
    if i<7:
        menor.append(i)
    else:
        maior.append(i)
print('As soma do veteros são: ',soma)
print('Os vetores são: ',listanota)
print('Os vetores na ordem inversa e: ',listanota[::-1])
print('A quantide de numero lidos foi: ',cont)
print('As Medio do veteros são: ',media)
print('As os numero que ficaram maior que media foi: ',maior)
print('As os numero que ficaram menor que media foi: ',menor)
