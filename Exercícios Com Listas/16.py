salario=[200,250,320,413,516,680,791,677,999,1000,2000,3000]
contagem=[0]*9
for salario in salario:
    indice=salario//100-2
    indice_maximo=len(contagem)-1
    indice=min(indice,indice_maximo)
    contagem[indice]+=1
print(contagem)
