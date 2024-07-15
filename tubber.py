
kmRodado = float(input('Insira a Quilometragem rodada: '))

rodado5Km = f'R${kmRodado * 5.00:.2f}'
rodado5and15Km = f'R${kmRodado * 4.50:.2f}'
rodado15KmMais = f'R${kmRodado * 4.00:.2f}'

if(kmRodado < 5):
    print(f'Foram rodados {kmRodado}km e o valor total da viagem foi de {rodado5Km}')
    
if(kmRodado >= 5) and (kmRodado < 15):
    print(f'Foram rodados {kmRodado}km e o valor total da viagem foi de {rodado5and15Km}')
    
if(kmRodado >= 15):
    print(f'Foram rodados {kmRodado}km e o valor total da viagem foi de {rodado15KmMais}')
