modelos = []
consumos = []

for i in range(1, 6):
    print('Veículo %d' % i)
    modelos.append(input('Nome: '))
    consumos.append(float(input('Km por litro: ')))

print('Relatório Final')
cont, custo = 0, 0
gasto = 0
menorModelo = ''
menor = gasto
for m in modelos:
    custo = 1000 / consumos[cont]
    gasto = custo * 2.25
    print('%s      - %.1f  -  %.1f litros  - R$ %.2f' % (m, consumos[cont], custo, gasto))
    if gasto > menor:
        menor = gasto
        menormodelo = m
    if menor > gasto:
        menor = gasto
        menorModelo = m
    cont += 1
print('O menor consumo é do %s.' % (menorModelo))