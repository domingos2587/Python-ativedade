mes=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto'
     ,'setembro','outubro','novebro','dezembro']
mediatem=[]
temperatura=[]
media=0
for i in range(0,len(mes)):
    tem=float(input('digite aqui a temperatura de cada mes do ano: '))
    mediatem.append(tem)
    media=media+tem
mediaanual=media/12
for x in mediatem:
    if x>mediaanual:
        temperatura.append(x)

print('as temperatura que superou media anual foi',temperatura)
        
    
