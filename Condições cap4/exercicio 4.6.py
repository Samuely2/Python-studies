# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em KM. Calcule o preço da viagem, cobrando R$ 0,50 por km para viagens de até 200 km, e R$ 0,45 para viagens mais longas.

distancia = int (input("Digite a distância que você deseja correr em KM"))
valor = 0


if distancia <= 200:
    valor = distancia * 0.50
    print(f"O preço da viagem com essa distância ficou: R${valor:.2f}")
else:
    valor = distancia * 0.45
    print(f"O preço dessa viagem mais longa ficou: R${valor:.2f}")