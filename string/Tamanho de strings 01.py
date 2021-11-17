"""Faça um programa que leia 2 strings e informe o conteúdo delas seguido do
seu comprimento. Informe também se as duas strings possuem o mesmo comprimento
e são iguais ou diferentes no conteúdo."""
nome1=input("Digite um nome: ")
nome2=input("Digite um nome: ")
cont=0
cont2=0
for i in nome1:
    cont=cont+1
    
for i in nome2:
    cont2=cont2+1
if cont==cont2:
    print("As das tem mesmo tamanho")
if nome1!=nome2:
    print("As duas palavras tem nome diferentes")
else:
    print("As duas tem nome iguais")
print(" As string usada foi",nome1," tem tamanho e de ",cont)
print(" As string usada foi",nome2," tem tamanho e de ",cont2)

