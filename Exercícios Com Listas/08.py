idade_lista=[]
altura_lista=[]
for i in range(5):
    idade=int(input('informe aqui a sua idade'))
    altura=float(input('informe aqui sua altura'))
    idade_lista.append(idade)
    altura_lista.append(altura)
print('A lista na ordem inversa em relaçao a idade e de: ',idade_lista[::-1])
print('A lista na ordem inversa em relaçao a altura e de: ',altura_lista[::-1])
    
