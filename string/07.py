'''onta espaços e vogais. Dado uma string com uma frase informada pelo usuário
(incluindo espaços em branco), conte:
quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u.'''
tentativa=input("Digite aqui  a sua frase:").upper()
espaço=0
vogal=0
for i in tentativa:
    if i==" ":
        espaço+=1
    if i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
        vogal+=1
print('quantidade de espaço e de: 'espaço)
print('quantidade de vogal e de: 'vogal)
