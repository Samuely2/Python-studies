distancia = float(input("Digite a distância em KM que você irá percorrer"))
velocidademedia = float(input("Digite a velocidade média esperada para a viagem em KM/H"))

tempo = distancia / velocidademedia

print(f"O tempo médio que você irá levar para chegar será: {tempo: .2f} ")
