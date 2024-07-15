kmRodado = float(input('Insira a Quilometragem rodada: '))

if(kmRodado < 5):
    valor = f'R${kmRodado * 5.00:.2f}'
    
elif(kmRodado >= 5) and (kmRodado <= 15):
   valor = f'R${kmRodado * 4.50:.2f}'
    
else:
    valor = f'R${kmRodado * 4.00:.2f}'
    
print(f'Foram rodados {kmRodado}km e o valor foi de {valor}')
