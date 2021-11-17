'''Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene
num vetor a média de cada aluno, imprima o número de alunos com média maior
ou igual a 7.0.'''
listanotas=[]
notasalunos=[]
medias2=0
for i in range(2):
    medias=0
    
    for j in range(4):
        nota=float(input("Digite aqui a nota"))
        notasalunos.append(nota)
        medias=medias+nota
    medias2=medias/4
    listanotas.append(medias2)
print("As notas foram",notasalunos)
print("As medias foram",listanotas)
