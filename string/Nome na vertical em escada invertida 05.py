"""Nome na vertical em escada invertida. Altere o programa anterior
de modo que a escada seja invertida."""
nome = input("Digite o seu nome: ").upper()
for i in range(0, len(nome)+1):
    print(nome[i:])
