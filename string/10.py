cont=('zero','um','dois', 'tres','quatro','cinco',
      'seis',' sete','oito',' nove',' dez', 'onze',' doze',' treze',
      'catorze',' quize','desseies',' dezessete' ,'dezoito ','dezenove','vinte',
      'Vinte e um','Vinte e dois','Vinte e tres','Vinte e quatro','Vinte e cinco'
      ,'Vinte e seis', 'Vinte e sete','Vinte e oito','Vinte e nove','trinta',
      'trinta e um','trinta e dois','trinta e tres','trinta e quatro','trinta e cinco'
      ,'trinta e seis', 'trinta e sete','trinta e oito','trinta e nove','quarenta',
      'quarenta e um','quarenta e dois','quarenta e tres','quarenta e quatro','quarenta e cinco'
      ,'quarenta e seis', 'quarenta e sete','quarenta e oito','quarenta e nove','cinquenta','Cinquenta e um','Cinquenta e dois','Cinquenta e tres',
      'Cinquenta e quatro','Cinquenta e cinco','Cinquenta e seis','Cinquenta e sete','Cinquenta e oito','Cinquenta e nove',
      'sessenta','sessenta e um','sessenta e dois','sessenta e tres','sessenta e quatro','sessenta e cinco','sessenta e seis','sessenta e sete',
      'sessenta e oito','sessenta e nove','setenta','setenta e um','setenta e dois','setenta e tres','setenta e quatro','setenta e cinco'
      ,'setenta e seis','setenta e sete','setenta e oito','setenta e nove','oitenta','oitenta e um','oitenta e dois','oitenta e tres','oitenta e quatro',
      'oitenta e cinco','oitenta e seis','oitenta e sete','oitenta e oito','oitenta e nove','noventa ','noventa e um ','noventa e dois ','noventa e tres ',
      'noventa e quatro ','noventa e cinco ','noventa e seis ','noventa e sete ','noventa e oito ','noventa e nove')
while True:
    num=int(input(' Digite numero entre 0 e 99: '))
    if 0<=num<=99:
        break
    print("tente novamente")
print(f'Voce digitou o numero {cont[num]}')
