# A Tuber, uma nova empresa de taxi entrou em operação no Brasil. Esta nova empresa opera da seguintes forma:

# - Viagem com menos de 5 km é cobrado R$ 5,00 por quilometro rodado
# - Viagem entre 5 e 15 km é cobrado R$ 4,50 por quilometro rodado
# - Viagem maiores de 15 km é cobrado R$ 4,00 por quilometro rodado

# Crie um programa que mostre quanto um passageiro vai pagar na viagem dele.

kmRodado = int(input('Insira a Quilometragem rodada: '))

rodado5Km = f'R${kmRodado * 5.00:.2f}'
rodado5and15Km = f'R${kmRodado * 4.50:.2f}'
rodado15KmMais = f'R${kmRodado * 4.00:.2f}'

if(kmRodado < 5):
    print(f'Foram rodados {kmRodado}km e o valor total da viagem foi de {rodado5Km}')
    
if(kmRodado >= 5) and (kmRodado < 15):
    print(f'Foram rodados {kmRodado}km e o valor total da viagem foi de {rodado5and15Km}')
    
if(kmRodado >= 15):
    print(f'Foram rodados {kmRodado}km e o valor total da viagem foi de {rodado15KmMais}')