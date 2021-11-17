import random
palavra=input("Digite a palavra que vc quer embaralhar: ")
embaralhar=[]
for i in palavra:
    embaralhar.append(i)
random.shuffle(embaralhar)
print(embaralhar)
