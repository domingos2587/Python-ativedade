palavra=input("Digite a  palavra chave: ").upper()
palavra_chave=[]
forca=[]
for i in palavra:
    palavra_chave.append(i)

for i in range(0,len(palavra_chave)):
    forca.append("_")
acertou=False
while acertou==False:
    letra=input("digte um litra: ").upper()
    for i in range (0,len(palavra_chave)):
        if letra==palavra_chave[i]:
            forca[i]=letra
        print(forca[i])
    acertou=True
    for x in range (0,len(forca)):
        if forca[x]=="_":
            acertou=False
    
