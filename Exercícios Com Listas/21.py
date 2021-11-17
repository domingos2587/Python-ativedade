problemas = [0] * 4
print('''1- necessita da esfera
2- necessita de limpeza
3- necessita troca do cabo ou conector
4- quebrado ou inutilizado ''')
while True:
    identificacao = int(input('Identificação: '))
    if identificacao == 0:
        break
    problema = int(input('Digite o número do problema: '))
    problemas[problema - 1] = problemas[problema - 1] + 1
                
print('Situação                        Quantidade              Percentual')
total = sum(problemas)
print('1- necessita da esfera                  %d              %.2f' % (problemas[0],  (100 * problemas[0]) / total))
print('2- necessita de limpeza                 %d              %.2f' % (problemas[1], (100 * problemas[1]) / total))
print('3- necessita troca do cabo ou conector  %d              %.2f' % (problemas[2], (100 * problemas[2]) / total))
print('4- quebrado ou inutilizado              %d              %.2f' % (problemas[3], (100 * problemas[3]) / total))
    