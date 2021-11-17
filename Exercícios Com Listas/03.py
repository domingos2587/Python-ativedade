lista=[]
notas=0
medias=0
for i in range(4):
    num=float(input('Digite aqui a nota: '))
    lista.append(num)
    notas=num+notas
medias=notas/4
lista.append(medias)
print("As notas e media e: ",lista)
