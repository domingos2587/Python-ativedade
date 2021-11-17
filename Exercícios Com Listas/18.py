print('Enquete: Quem foi o melhor jogador?')


opcoes = ['Jogador 1', 'Jogador 2', 'Jogador 3', 'Jogador 4', 'Jogador 5', 'Jogador 6', 'Jogador 7',
'Jogador 8', 'Jogador 9', 'Jogador 10', 'Jogador 11', 'Jogador 12', 'Jogador 13', 'Jogador 14',
'Jogador 15', 'Jogador 16', 'Jogador 17', 'Jogador 18', 'Jogador 19', 'Jogador 20', 'Jogador 21',
'Jogador 22', 'Jogador 23']
sistemas = [0] * 23
while True:
    while True:
        opcao = int(input('Número do jogador (0=fim): '))
        if opcao > 23 or opcao < 0:
            print('Informe um valor entre 1 e 23 ou 0 para sair!')
        else:
            break
    if opcao == 0:
        break
    sistemas[opcao - 1] = sistemas[opcao - 1] + 1


print('JOGADORES  VOTOS    %')
print('----------------------------------')
cont = 0
melhor = 0
melhorSis = ''
perc = 0
for s in sistemas:
    print('%s   %d   %.2f%%' % (opcoes[cont], s,(s * 100) / sum(sistemas) ))
    if s > melhor:
        melhor = s
        melhorSis = opcoes[cont]
        perc = (s * 100) / sum(sistemas)
    cont += 1

print('----------------------------------')
print('Total   %d' % sum(sistemas))
print('O jogador mais votado foi o %s, com %d votos, correspondendo a %.2f dos votos.' % (melhorSis, melhor, perc))