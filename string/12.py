print('Valida e corrige número de telefone')
numero = int(input('Telefone: '))
novoNumero = ''
if len(str(numero)) < 8:
    diferenca = 8 - len(str(numero))
    novoNumero = '3' * diferenca

numeroFormatado = novoNumero + str(numero)
numeroFormatado = numeroFormatado[0:4] + '-' + numeroFormatado[5:]

print('Telefone possui %d dígitos. Vou acrescentar o digito três na frente.' % len(str(numero)))
print('Telefone corrigido sem formatação: %d' % numero)
print('Telefone corrigido com formatação: %s' % numeroFormatado)
