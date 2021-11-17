"""Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é
idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e
OVO são palíndromos. Em textos mais complexos os espaços e pontuação são
ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde
os espaços foram ignorados. Faça um programa que leia uma seqüência de
caracteres, mostre−a e diga se é um palíndromo ou não."""
nome=input("digite o seu nome aqui").upper().replace(" ", "")
aocontrario=nome[::-1]
if aocontrario==nome:
    print('eles são palindromo')
else:
    print('eles não sao palindromo')
